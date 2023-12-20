## Dossier contenant les workflows créés pour les TDs et le projet.

Action déclenchée à chaque changement pour builder l’application: changeBuilder.yml

Action déclenchée manuellement pour utiliser le fichier Dockerfile pour créer une image: dockerfile-to-image.yml

Action déclenchée pour chaque tag semver pour utiliser le fichier Dockerfile pour créer et
pousser l’image de l’API avec en tag la version semver spécifiée: semVerBuilder.yml
