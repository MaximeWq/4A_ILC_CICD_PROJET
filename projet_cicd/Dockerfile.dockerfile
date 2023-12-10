FROM python:3.8
WORKDIR /app
RUN pip install Flask
COPY . .
EXPOSE 5000
CMD ["python", "routes.py"]