# Space-Invador-Compan-Fels-24-25-
Règles du jeu:
    Tirez sur les Sucreries afin de les faire disparaître avant que celles-ci atteignent votre Dent. Protégez-vous à l'aide des tablettes de chocolat !
Votre dent possède trois vies et en perd une a chaque contact avec une sucrerie ennemi. De plus l'élimination d'une sucrerie classique vous ocroiera
100 points, celle d'une sucrerie spéciale le DOUBLE. Mais faites attention les sucreries n'en finissent pas d'apparaître et elle deviennent de plus
en plus savoureuse ! A chauqe vague détruite le nombre de vie des sucreries classiques augmentent, à vous de voir jusqu'où vous pourrez protéger votre
dent.
    Commandes:
        - utiliser les flèches directionnelles pour vous déplacer (le joueur ne se déplace que à gauche ou à droite)
        - utiliser la barre espace pour tirer
        - utiliser la touche entrée (Return pour tkinter) pour mettre le jeu en pause et le lancer au début

    Bonus: Pour plus de difficulté un bug est laisser en commentaire dans le programme dans la classe visuel.
        Si vous voulez rendre plus dur les nouvelles parties lancer par le bouton NewGame décommenter la ligne 158.
        Cela augmente le nombre de fonction gérant le tour, donc la vitesse de toutes les entitées autres que le joueur.

Bonne chances !

Particularité:
    - les ennemis ne tirent pas

Implémentations demandées:
    - utilisation de listes pour stocker et gérer les entitées autre que le joueur dans leur généralité. De même chaque type d'entitée est aussi gérer dans une liste qui lui est propre (dans la classe Jeu des lignes 36 à 40, dans la classe Visuel ligne 80)
    - justification: La liste permet une plus grande liberté d'accès au données que les files et les piles et nous permet de stocker nos entitées et d'y accéder rapidement. Les listes nous permettent aussi de travailler d'un seul coup sur toutes nos entitées non joueur, par exepmple pour les collisions.


GitHub:
    -lien: https://github.com/NicolasFels/Space-Invaders-Compan-Fels-24-25- 
    -branche principale: MainVisuelAndAfter