#!/bin/bash
if [ "$1" == "dev" ]; then
    FLASK_DEBUG=1 flask --app app run -p 5001
elif [ "$1" == "prod" ]; then
    gunicorn -b :5001 --access-logfile - --error-logfile - app:app
else
    echo "Invalid argument. Please use 'dev' or 'prod'."
    exit 1
fi