# Write up Open Redirect

# Exploration

Sur la page d’accueil du site, en bas de pages, il y a 3 logos faisant respectivement référence à facebook, twitter et instagram.

Si l’on clique dessus, nous sommes redirigés sur la page correspondante:

![Capture d’écran 2024-05-02 à 19.21.06.png](images/Capture_decran_2024-05-02_a_19.21.06.png)

# Exploitation

En regardant le lien qui permet de nous rediriger, on remarque qu’une page est chargée, **redirect**, avec un paramètre qui correspond à la redirection. Sur l’image ci dessus, on peut voir **facebook** comme valeur.

En modifiant cette valeur, nous obtenons le flag:

![Capture d’écran 2024-05-02 à 19.24.05.png](images/Capture_decran_2024-05-02_a_19.24.05.png)

# Remédiation

Un open redirect est une vulnérabilité qui permet à un acteur malveillant de rediriger une victime vers un site web qu’il contrôle sans s’en rendre compte. Les conséquences peuvent être multiples:

- Phishing: L’attaquant redirige la victime vers un site de phishing pour voler des identifiants
- Vol de cookie si passé en paramètres GET
- XSS: exploitation de la vulnérabilité pour injecter du code Javascript sur la page
- Utilisation pour d’autres attaques, comme du déni de service

Pour remédier à cette vulnérabilités, plusieurs étapes sont nécessaires:

- Whitelist: mettre en place une whitelist de domaine autorisés pour la redirection
- Validation de l’input utilisateur, pour s’assure qu’il s’agit d’une URL valide
- Ne pas passer de token d’identification en paramètre GET