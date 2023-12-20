<h1 align="center">4A_ILC_CICD_PROJETs </h1>
<h2 align="center">Objectif : Créer une API Flask pour de la gestion CRUD d’un calendrier.</h2>


## Membres


Wissocq Maxime ILC


## Lien github


Lien: https://github.com/MaximeWq

Le contenu du TP de projet est dans le dossier projet_cicd

## Fonctionnement de l'API

Executer le fichier routes.py. On accède à l'affichage de l'API avec http://127.0.0.1:5000.

On peut alors utiliser des commandes curl pour utiliser les routes de type 'POST'. Par exemple: 

Route E1: 

curl -X POST -H "Content-Type: application/json" -d "{\"T1\": \"2023-12-03T15:30:00\", \"t\": 1800, \"p\": [\"person3\", \"person4\"], \"n\": \"Event 3\", \"d\": \"Description 3\"}" http://localhost:5000/add-events

Route E4:

curl -X POST -H "Content-Type: application/json" -d "{\"participant\": \"nouveau_participant\"}" http://localhost:5000/add-participants/event1/participants

Route E6:

curl -X POST -F "file=@events.csv" http://localhost:5000/import-csv

Pour les routes restantes, on peut également y accéder avec des curls, on simplement en modifiant l'url.

Pour E2: /add-events
E3: /display-events/<person>
E5: /display-next-event
E7: /time/<person>
E8: /time-left/<date>




## Documentation API REST

- E1 - Créer un évènement:
Pour cette route, on souhaite ajouter des éléments au dictionnaire d'évènement, on utilise donc la méthode POST. On récupère le contenu sous forme json passé via curl. On ajoute ensuite au dictionnaire le contenu récupéré.
  
- E2 - Afficher une liste de tous les événements dans l’ordre chronologique: On utilise la fonction sorted() de python sur la clé 'T1' pour trier le dictionnaire par ordre chronologique. On retourne ensuite ce dictionnaire au format json.

- E3 - Afficher une liste de tous les évènements dans l’ordre chronologique liées à une personne: Même principe que E2, on va en plus parcourir les personnes des evenements pour voir si certains correspondent à ce qu'on recherche.

- E4 - Ajouter un participant à un évènement: On récupère le participant passé par requête curl avec request.get_json() et on l'ajoute a notre tableau de participants pour touts les évènements correspondant à ce que l'on recherche.

- E5 - Afficher le détails du prochain cours: Pour trouver le dernier cours, on utilise la fonction python min pour trouver l'évènement avec la valeur de date la plus faible et donc la proche du présent.

- E6 - Importer des données depuis un fichier csv: On va lire le fichier en se basant sur le délimiteur ",". On peut alors simplement remplire le dictionnaire avec les valeurs lues dans le fichiers csv.

## Documentation des routes avec swagger

https://editor.swagger.io/

Utiliser le fichier swagger.yaml, pour accédéder à la description des routes.

## Technologies uilisées

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Dockerfile](https://img.shields.io/badge/Dockerfile-Yes-green.svg)](https://https://github.com/MaximeWq/4A_ILC_CICD_PROJET)


## Résulats des builds

[![Build on change](https://github.com/MaximeWq/4A_ILC_CICD_PROJET/actions/workflows/changeBuilder.yml/badge.svg)](https://github.com/MaximeWq/4A_ILC_CICD_PROJET/actions/workflows/changeBuilder.yml)


