# Python3 : RPG
## Créer un RPG en Python.
Rpg créer en équipe Fardid et Nicolas

## Présentation

Ce rpg est un project de  jeux représentant un rpg aux tour par tour 
nous l'avons créés avec une classes pour chaque  personnage 
nous avons aussi crée une classe commune et l'or de la creation d'un objet personnes c'est classe herite de 
la classe commune.

nous avons crée des object game pour les reutiliser lors du combat 
ansi que des objet pour la narratio et le time sleep clear pour effacer l'ecran comme transition .

## Déroulement

- Le joueur peut choisir le type de personnage qu'il souhaite incarner
- Trois classes sont disponibles pour le joueur (guerrier, archer, magicien)
- Le joueur peut nommer son personnage comme il le désire au début du jeu
- Trois classes sont disponibles pour les ennemis (orc, loup, zombie)
- Les personnages ont tous au minimum les caractéristiques suivantes (vie, attaque, défense, agilité, nom)
- Le magicien dispose en plus de mana représentant sa force magique
- Un personnage peut en attaquer un autre, la cible perd alors de la vie en proportion de sa valeur de défense et de la valeur d'attaque de l'assaillant
- Le magicien peut se soigner. Ce sort consomme du mana mais lui redonne de la vie. S'il n'a pas assez de mana, il ne peut pas le lancer
- Un combat est simulé entre le personnage du joueur et un ennemi de votre choix jusqu'à ce que l'un ou l'autre des personnages soit mort.
## Critères de qualité
Spécifications techniques :
- Langage Python 3
- Organisation du code en modules et packages
- Usage de la programmation orientée objet
- Respect du principe DRY
- Essayer de respecter certains des principes SOLID
- Programme exécutable par le lancement d'un fichier main.py
Ressources
https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232721-apprehendez-les-classes
