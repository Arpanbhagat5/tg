#!/bin/bash

cd backend

echo "Running migrations..."
python manage.py migrate

echo "Loading fixtures..."
python manage.py loaddata fixtures/prefectures.json  # Adjust path

echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000
