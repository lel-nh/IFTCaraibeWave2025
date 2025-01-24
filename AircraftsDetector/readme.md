# Aircrafts Data Collection

Ce projet Python utilise une API pour collecter des informations sur les avions aux alentours de l'aéroport de Pointe-à-Pitre (TFFR). Dans le cadre de CaraibeWave2025 réalisé à l'IFT sous la supervisions de Gaël Musquet 

## Description

Le script `aircrafts.py` permet de récupérer des informations sur les avions dans une zone géographique spécifique en utilisant l'API de Flight Radar. Les données collectées sont ensuite enregistrées dans un fichier CSV.

## Fonctionnalités

- Récupération des informations des avions dans une zone géographique définie.
- Enregistrement des données dans un fichier CSV.
- Gestion des erreurs et des réponses vides.

## Informations Récupérées

Les informations récupérées pour chaque avion incluent :

- `ICAO`: Code ICAO de l'avion
- `Callsign`: Indicatif d'appel de l'avion
- `lat`: Latitude de l'avion
- `lon`: Longitude de l'avion
- `alt`: Altitude de l'avion
- `direction`: Direction de l'avion en degrés
- `type`: Type d'avion
- `postime`: Timestamp de la position

Ces informations sont ensuite enregistrées dans un fichier CSV avec les colonnes suivantes : `A`, `ICAO`, `Callsign`, `lat`, `lon`, `alt`, `direction`, `type`, `postime`.

## API Utilisée

L'API utilisée est l'API de Flight Radar, qui permet de récupérer des informations sur les vols dans une zone géographique définie. Les paramètres de la requête incluent les coordonnées de la zone (latitude et longitude) et une clé API pour l'authentification.
