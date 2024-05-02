# Write up Admin Panel Login

# Exploration

Pendant notre phase d'exploration, nous avons trouvé le fichier **robots.txt** d'accessible.

Dans ce fichier étaient mentionnés 2 chemins, **/whatever** et **/.hidden**.

En naviguant sur le dossier **/whatever**, le listing du dossier est présent, et nous pouvons accéder à un fichier, **htpasswd:**

```bash
#Contenu de htpasswd
root:437394baff5aa33daa618be47b75cb49
```

Cela ressemble à un couple nom de compte/mot de passe d’un utilisateur root.

Nous avons aussi découvert un autre chemin assez commun, **/admin**, avec une page de login.

# Exploitation

Le mot de passe précédemment trouvé est en fait un hash md5. Nous avons facilement pu retrouver le mot de passe de base via un [outil en ligne](https://md5decrypt.net/), étant donné que c’était un mot de passe très commun (qwerty123@)

![Capture d’écran 2024-05-01 à 13.56.33.png](images/Capture_decran_2024-05-01_a_13.56.33.png)

En utilisant la combinaison root:qwerty123@ nous avons pu nous connecter depuis le panel admin et obtenir le flag.

# Remédiation

Le fichier htpasswd ne devrait jamais être exposé publiquement sur une application web. Il doit être stocké en dehors de l’arborescence servie par le serveur.

Il nous à aussi été possible de le trouver du au fait que le listing du répertoire était activé sur le chemin **/whatever**. Il est en général recommandé de toujours le désactiver, ce qui est la norme par défaut pour la plupart des serveurs web.

Dernièrement, il est important d’instaurer une forte politique de mot de passe. Nous avons facilement pu décrypter le mot de passe de l’utilisateur root avec un simple outil en ligne, du au fait que le mot de passe était très courant.

Les bonnes pratiques en terme de politique de mot de passe sont:

- Au moins 12 caractères
- Mélange de lettre majuscule et minuscule
- Inclure des caractères spéciaux
- Eviter des mots courants ou reliés à la personne
- Les changer régulièrement