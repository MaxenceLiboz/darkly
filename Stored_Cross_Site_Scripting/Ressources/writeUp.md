# Write up Reflected XSS Media

# Exploration

Durant notre exploration, nous somme tombés sur un formulaire de feedback, ou nous pouvions laissé un commentaire, qui était ensuite stocké et reflété sur cette page:

![Capture d’écran 2024-05-02 à 21.04.31.png](images/Capture_decran_2024-05-02_a_21.04.31.png)

# Exploitation

Nous avons rapidement pensé à la possibilité d’une stored XSS, ce genre de fonctionnalité étant souvent vulnérable.

Nous avons donc rentrés des payloads classiques de xss, et avons remarqué que nos balises **\<script\>** étaient trimées de nos commentaires:

![Capture d’écran 2024-05-02 à 21.06.17.png](images/Capture_decran_2024-05-02_a_21.06.17.png)

![Capture d’écran 2024-05-02 à 21.06.25.png](images/Capture_decran_2024-05-02_a_21.06.25.png)

En revanche, une XSS stockée à fonctionné dans le name, avec comme payload:

**\<img src=a onerror=alert(1)\>**

![Capture d’écran 2024-05-02 à 21.10.11.png](images/Capture_decran_2024-05-02_a_21.10.11.png)

Après beaucoup de payloads utilisés (6000) (merci Intruder), et plusieurs tests de plus en plus étranges, il semble qu’il suffisait simplement d’écrire **script** en tant que commentaire pour obtenir le flag. Pourquoi pas.

Et c’est ainsi que nous l’avons obtenu:

![Capture d’écran 2024-05-02 à 21.18.42.png](images/Capture_decran_2024-05-02_a_21.18.42.png)

# Remédiation

Nous sommes ici face à une Stored XSS. L’impact d’une telle vulnérabilité peut avoir de grosses conséquences, étant donné que l’injection est enregistrée dans la base de donnée, et sera exécuté dans le navigateur de chaque personne ou elle sera exposée.

Les conséquences peuvent être multiples:

- Vol de cookie de session
- Escalade de privilèges
- Defacing
- etc..

Pour remédier à cette vulnérabilité, voici quelques précautions à suivre:

- Validation de l’input utilisateur, et encoder ou supprimer les caractères spéciaux. Des librairies sont spécialement conçues pour ca
- Encoder les sorties des caractères spéciaux en HTML, surtout quand l’input de l’utilisateur est reflété
- Configurer des des en têtes de sécurités appropriés, tels que les CSP (Content Security Policy) pour atténuer l’impact XSS