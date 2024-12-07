# Space-Invador-Compan-Fels-24-25-
Règles du jeu:
    Tirez sur les Sucreries afin de les faire disparaître avant que celles-ci n'atteignent votre Dent. Protégez-vous à l'aide des tablettes de chocolat !
Votre dent possède trois vies et en perd une à chaque contact avec une sucrerie ennemie. De plus l'élimination d'une sucrerie classique vous octroiera
100 points, celle d'une sucrerie spéciale le DOUBLE. Mais faites attention les sucreries n'en finissent pas d'apparaître et elles deviennent de plus
en plus savoureuses ! A chaque vague détruite le nombre de vie des sucreries classiques augmente, à vous de voir jusqu'où vous pourrez protéger votre
dent.
    Commandes:
        - utiliser les flèches directionnelles pour vous déplacer (le joueur ne se déplace que vers la gauche ou vers la droite)
        - utiliser la barre espace pour tirer
        - utiliser la touche entrée (Return pour tkinter) pour lancer le jeu ou le mettre en pause

    Bonus: Pour plus de difficulté un bug est laissé en commentaire dans le programme dans la classe visuel.
        Si vous voulez rendre plus dures les nouvelles parties lancées par le bouton NewGame décommentez la ligne 158.
        Cela augmente le nombre de fonctions gérant le tour, c'est-à-dire, la vitesse de toutes les entités autres que le joueur.

Bonne chance !

Particularité:
    - les ennemis ne tirent pas

Implémentations demandées:
    - utilisation de listes pour stocker et gérer les entités autres que le joueur dans leur généralité. De même, chaque type d'entité est aussi géré dans une liste qui lui est propre (dans la classe Jeu des lignes 36 à 40, dans la classe Visuel ligne 80)
    - justification: La liste permet une plus grande liberté d'accès aux données que les files et les piles et nous permet de stocker nos entités et d'y accéder rapidement. Les listes nous permettent aussi de travailler d'un seul coup sur toutes nos entités non joueur, par exemple pour les collisions.


GitHub:
    -lien: https://github.com/NicolasFels/Space-Invaders-Compan-Fels-24-25- 
    -branche principale: MainVisuelAndAfter