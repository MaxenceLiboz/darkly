# Write up SQL Injection page member

# Exploration

Durant notre exploration de l’application web, nous sommes tombés sur une fonctionnalité pour retrouver des informations sur les membres à partir de leur ID:

![Capture d’écran 2024-05-02 à 19.32.58.png](images/Capture_decran_2024-05-02_a_19.32.58.png)

# Exploitation

Etant donné que cette fonctionnalité permet de retrouver des utilisateurs, nous avons déduis qu’elle avait une interaction avec la base de donnée et était donc potentiellement vulnérable aux injections SQL. Pour s’en convaincre, une simple quote comme ID permet de trigger une erreur:

![Capture d’écran 2024-05-02 à 19.34.34.png](images/Capture_decran_2024-05-02_a_19.34.34.png)

A priori, notre input n’est pas vérifié avant de faire la requête en base de donnée.

Notre objectif est donc d’essayer de récupérer le contenu de la base de donnée à partir de cette injection SQL.

On peut imaginer que la requête SQL de base ressemble à ca:

```php
#Le premier ? correspond au nombre de colonnes renvoyées que nous devons déterminer
#Nous pouvons penser qu'il y en à 2 correspondant à first name et surname

#Le deuxième est à vérifier, est ce que la table se nomme users
SELECT ? FROM users? WHERE id=<notre_payload>;
```

Nous allons tout d’abord s’assurer du nombre de colonnes renvoyées avec ce payload, en se basant sur une injection UNION based:

**1 UNION SELECT null,null**

Il fonctionne. Pour s’en assurer, on supprime un null et on renvoie la requête, on obtient une erreur SQL:

![Capture d’écran 2024-05-02 à 19.42.52.png](images/Capture_decran_2024-05-02_a_19.42.52.png)

Pour comprendre le payload, il faut comprendre comment fonctionne UNION en sql. Il permet de lier à la requête d’autre données mais dois renvoyé le même nombre de donnée que la première query. Les types doivent aussi correspondre, c’est pourquoi utiliser **null** est le candidat idéal, il correspond à tous les types.

Le payload suivant va nous permettre de récupérer tout les noms de tables de la base de donnée:

**1 UNION SELECT null,table_name FROM information_schema.tables**

On obtient beaucoup d’output, mais confirmons que la table **users** existe:

![Capture d’écran 2024-05-02 à 19.46.57.png](images/Capture_decran_2024-05-02_a_19.46.57.png)

La prochaine étape est d’obtenir les noms des colonnes de cette tables. Nous allons utiliser ce payload:

**1 UNION SELECT null,column_name FROM information_schema.columns**

Nous obtenons encore une fois beaucoup d’output, mais trouvons un ensemble de colonnes qui on l’air liées au user:

![Capture d’écran 2024-05-02 à 19.54.00.png](images/Capture_decran_2024-05-02_a_19.54.00.png)

On va donc récupérer l’ensemble de ces valeurs en les concaténants:

**1 UNION SELECT null,CONCAT(first_name,0x0a,last_name,0x0a,town,0x0a,country,0x0a,planet,0x0a,Commentaire,0x0a,countersign) FROM users**

Et on obtient ce qu’on cherchait:

![Capture d’écran 2024-05-02 à 19.59.27.png](images/Capture_decran_2024-05-02_a_19.59.27.png)

On decrypte la valeur **5ff9d0165b4f92b14994e5c685cdce28** en utilisant cet [outil en ligne](https://md5decrypt.net/), qui nous donne la valeur **FortyTwo**.

En suivant les conseils donnés, on le passe en lowercase et on le convertit en sha256, on obtient le flag:

```php
echo -n "fortytwo" | openssl dgst -sha256
SHA2-256(stdin)= 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
```

# Remédiation

Les injections SQL sont des vulnérabilités encore très fréquentes sur les applications web si l’on se refère au [top 10 OWASP](https://owasp.org/Top10/fr/). En 2021, les injections (tout types confondus) se classent encore en 3ème place:

![Capture d’écran 2024-05-02 à 20.04.09.png](images/Capture_decran_2024-05-02_a_20.04.09.png)

Cela mène souvent à de terribles conséquences pour les sites vulnérables, incluant:

- Altération ou suppression des données présentes
- Élévation de privilèges
- Leak d’information
- Éxecution de commande à distance

Pour s’en protéger, voici plusieurs étapes à suivre:

- Utilisation d’ORM permettant d’utiliser des requêtes préparées
- Validation de l’input de l’utilisateur
- Ne jamais utiliser de la donnée contrôlable par l’utilisateur dans des requêtes SQL
- Suivre le principe du moindre privilège
- Chiffrer les données sensibles en base de donnée