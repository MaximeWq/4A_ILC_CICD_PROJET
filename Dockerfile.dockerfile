# Utiliser l'image Python 3.8 comme image de base
FROM python:3.8

# Créer et définir le répertoire de travail
WORKDIR /app

# Installer les dépendances
RUN pip install Flask

# Copier le reste des fichiers dans le conteneur
COPY . .

# Exposer le port sur lequel Flask écoute
EXPOSE 5000

# Définir le point d'entrée du conteneur
CMD ["python", "td3.py"]
