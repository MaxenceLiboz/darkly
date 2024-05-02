# Write up Source code comments

# Exploration

En naviguant sur le site, si nous cliquons sur le logo [© BornToSec](http://192.168.64.36/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f) en bas de page, nous sommes redirigés sur une autre page:

![Capture d’écran 2024-05-02 à 19.01.47.png](images/Capture_decran_2024-05-02_a_19.01.47.png)

A première vue, il n’est pas possible d’exploiter de vulnérabilité.

# Exploitation

En inspectant le code source de la page, nous sommes tombés sur 1 commentaire plus ou moins explicites:

![Capture d’écran 2024-05-02 à 19.02.55.png](images/Capture_decran_2024-05-02_a_19.02.55.png)

Par déduction, nous avons envoyé une nouvelle requête à cette page, mais en ajoutant le header HTTP "**Referer: https://www.nsa.gov/**"

![Capture d’écran 2024-05-02 à 19.06.16.png](images/Capture_decran_2024-05-02_a_19.06.16.png)

Une fois envoyé, un deuxième commentaire apparaît:

![Capture d’écran 2024-05-02 à 19.10.47.png](images/Capture_decran_2024-05-02_a_19.10.47.png)

Encore une fois, en réfléchissant un peu, nous avons pensé que cela faisait référence au header User-Agent.

Nous l’avons donc aussi remplacé avec la valeur **ft_bornToSec**, et nous avons ainsi obtenu le flag.

# Remédiation

Il arrive souvent que des commentaires soient laissés dans le code source en phase de développement d’une application. Ces commentaires peuvent contenir une grande variété d’informations intéressantes du point de vue d’un attaquant, allant même parfois jusqu’à des mots de passes de compte administrateur.

Pour remédier à cette vulnérabilité, il suffit simplement de s’assurer que des commentaires sois laissé dans le code source sur une application de production.