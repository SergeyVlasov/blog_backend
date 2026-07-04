#!/bin/sh
echo "Waiting for DB..."
python manage.py shell -c "
from django.db import connections
import time
while True:
    try:
        connections['default'].cursor()
        break
    except Exception:
        print('DB not ready...')
        time.sleep(1)
"
echo "DB is ready"
echo "Applying migrations..."
python manage.py migrate --noinput
echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000