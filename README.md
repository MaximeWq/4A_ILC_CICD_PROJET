<h1 align="center">4A_ILC_CICD_PROJETs </h1>
<h2 align="center">Objectif : Créer une API Flask pour de la gestion CRUD d’un calendrier.</h2>


## Membres


Wissocq Maxime ILC


## Lien github


Lien: https://github.com/MaximeWq

Le contenu du TP de projet est dans le dossier projet_cicd

## Documentation API REST

- E1 - Créer un évènement:
Pour cette route, on souhaite ajouter des éléments au dictionnaire d'évènement, on utilise donc la méthode POST. On récupère le contenu sous forme json passé via curl. On ajoute ensuite au dictionnaire le contenu récupéré.
  
- E2 - Afficher une liste de tous les événements dans l’ordre chronologique: On utilise la fonction sorted() de python sur la clé 'T1' pour trier le dictionnaire par ordre chronologique. On retourne ensuite ce dictionnaire au format json.

- E3 - Afficher une liste de tous les évènements dans l’ordre chronologique liées à une personne: Même principe que E2, on va en plus parcourir les personnes des evenements pour voir si certains correspondent à ce qu'on recherche.

- E4 - Ajouter un participant à un évènement: On récupère le participant passé par requête curl avec request.get_json() et on l'ajoute a notre tableau de participants pour touts les évènements correspondant à ce que l'on recherche.

- E5 - Afficher le détails du prochain cours: Pour trouver le dernier cours, on utilise la fonction python min pour trouver l'évènement avec la valeur de date la plus faible et donc la proche du présent.

- E6 - Importer des données depuis un fichier csv.

## Documentation des routes avec swagger

https://editor.swagger.io/

Utiliser le fichier swagger.yaml, pour accédéder à la description des routes.

## Technologies uilisées

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Dockerfile](https://img.shields.io/badge/Dockerfile-Yes-green.svg)](https://https://github.com/MaximeWq/4A_ILC_CICD_PROJET)


## Résulats des builds

[![Build on change](https://github.com/MaximeWq/4A_ILC_CICD_PROJET/actions/workflows/changeBuilder.yml/badge.svg)](https://github.com/MaximeWq/4A_ILC_CICD_PROJET/actions/workflows/changeBuilder.yml)


