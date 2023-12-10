# Utiliser l'image Python pour Windows
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Créer et définir le répertoire de travail
WORKDIR /app

# Installer les dépendances
RUN pip install Flask

# Copier le reste des fichiers dans le conteneur
COPY . .

# Exposer le port sur lequel Flask écoute
EXPOSE 5000

# Définir le point d'entrée du conteneur
CMD ["python", "routes.py"]
