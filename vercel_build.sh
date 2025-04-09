#!/bin/bash

echo "Running migrations..."
python manage.py migrate

echo "Creating superuser if doesn't exist..."
python manage.py shell -c "
from django.contrib.auth.models import User;
User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
"

echo "Build script completed successfully!" 