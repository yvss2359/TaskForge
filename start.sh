#!/bin/bash

# Stop script en cas d'erreur
set -e

echo "🚀 Lancement de TaskForge 🚀"

# --- 1️⃣ Lancer la base de données ---
echo "🟢 Démarrage de la base de données..."
docker compose up -d db

# --- 2️⃣ Lancer le backend ---
echo "🟢 Démarrage du backend FastAPI..."
cd backend
# On utilise uvicorn en mode reload
uvicorn app.main:app --reload &
BACK_PID=$!
cd ..

# --- 3️⃣ Lancer le frontend Angular ---
echo "🟢 Démarrage du frontend Angular..."
cd frontend/taskforge-frontend
ng serve --open &
FRONT_PID=$!
cd ../..

echo "✅ TaskForge est lancé !"
echo "CTRL+C pour tout arrêter"

# --- 4️⃣ Gestion CTRL+C ---
trap "echo '⛔ Arrêt...'; kill $BACK_PID $FRONT_PID; docker compose down; exit 0" SIGINT

# Boucle pour garder le script vivant
while true; do
    sleep 1
done
