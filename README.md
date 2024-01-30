# Marketyy_NextDjango

## Initial Steps

```bash
cd backend
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
```

```python
pip install django djangorestframework markdown django-filter
django-admin startproject backend .
```

```bash
cd ./backend
```

```python
django-admin startapp reviews
```

```python
python .\manage.py migrate
python .\manage.py createsuperuser
```

We can check out the functionality of server by:
```python
python .\manage.py runserver
```

When the new app is started (eg reviews) in the setting.py add the app name in the installed apps list:
```python
INSTALLED_APPS = [
    'reviews',
    'rest_framework',
    'django.contrib.admin',
...
]
```

Also, when the app (eg review) is updated, create and conduct the migration as below:
```python
python .\manage.py makemigrations
python .\manage.py migrate

```
