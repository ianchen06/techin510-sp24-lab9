# Mobile Web App

## Getting Started

```
python -m venv venv
source venv venv
pip install -r requirements.txt

cp .env.sample .env

# Make changes in .env

# If it is the first time
flask db upgrade

./start.sh
```

## Topics

1. Layout
1. Data fetching and rendering
1. Data visualization
1. Forms
1. Authentication
1. JavaScript

## Deploy to Production

This app uses [gunicorn](http://gunicorn.org) as the production [wsgi](https://www.fullstackpython.com/wsgi-servers.html) server

Put the following command in Azure Web App, Settings > Configuration > Startup Command

```
gunicorn -b :5001 --access-logfile - --error-logfile - app:app
```
