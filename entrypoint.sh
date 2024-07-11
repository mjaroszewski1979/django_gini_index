#!/bin/sh


# Run Django's manage.py command to create database migration files based on changes in models
python manage.py makemigrations 

# Apply the database migrations to synchronize the database schema with the current set of models
python manage.py migrate  

# Start the Django development server, binding it to all available IPs on port 8000
python manage.py runserver 0.0.0.0:8000
