# ProjetBackendDev
Exercice de développement backend (Python/Django)
# Plateforme de recrutement

## Description

Cette plateforme de recrutement permet de gérer les candidats et les recruteurs via une API REST.

## Prérequis

- Python 3.8+
- PostgreSQL
- pip
- Django
- Django REST framework
- drf-yasg
- psycopg2-binary

## Installation

1. Clonez le dépôt :

   Entrer sur votre terminal bash
   ```
   git clone https://github.com/Mohammed-BJ/ProjetBackendDev
   cd ProjetBackendDev
```
2.Creez et activez l'environnement virtuel
```
  python -m venv env
  source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
```
3.Installez les dépendances :
  ```pip install -r requirements.txt```

4.Configurer votre base de données dans settings.py
  ```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name', #A remplacer par la votre
        'USER': 'postgres',  #A remplacer
        'PASSWORD': 'your_password', #A remplacer
        'HOST': 'localhost'
        'PORT': '5432',
    } 
  }
```

5.Appliquez les migrations
``` 
  python manage.py makemigrations
  python manage.py migrate
```
6.Créez un superutilisateur pour accéder à l'interface d'admin
```  python manage.py createsuperuser ```

7.Démarrez le serveur de développement
```  python manage.py runserver ```

Utilisation
Accédez à la page d'acceuil : http://127.0.0.1:8000/
Utilisez les endpoints API pour gérer les candidats et les recruteurs.
Accédez à l'API des candidat : http://127.0.0.1:8000/api/candidates/
Accédez à l'API des recruteurs : http://127.0.0.1:8000/api/recruiters/
Accédez à l'interface d'administration : http://127.0.0.1:8000/admin/
Accédez à la documentation Swagger : http://127.0.0.1:8000/swagger/

