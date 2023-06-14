## SQL SERVER 2019 DATABASE Z DJANGO
create conda environment with following packages:
django, pyodbc, djangorestframework, django-cors-headers, sqlite.

remember not to use sql server 2022, it is not supported by pyodbc yet.
also you neet to install proper odbc driver for sql server 2019. in my project its odbc 17.

before starting django project i made a database in sql server 2019 and created six tables: Rower (bike), 
Klient (customer), Wypożyczenie (rent order), Salon (salon), Pracownicy (workers), Opłata (fee). 
Made some triggers involving the tables i created previously.
Then filled the tables with some data in SQL queries.

Created Django project with command:
```
django-admin startproject rentbikes
```
Then i created an app with command:
```
python manage.py startapp rentApp
```
The most important thing was to establish connection between django and sql server 2019. 
I did it by adding following lines to settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'rentBikes2',
        'USER': 'user-created-in-sql-server
        'PASSWORD': 'password-created-in-sql-server',
        'HOST': 'AURELIUSZ\MSSQLSERVER03',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            #'extra_params': 'TrustServerCertificate=yes',
            'MARS_Connection': 'True',
        },
    },
}
The mos

Then i added my app to installed apps in settings.py. Then i added cors headers to settings.py.
Then i added my app urls to main urls.py. Then i run server and checked if it works.
Then i added my database to databases section in settings.py.
Then i created a model in models.py and made migrations. Then i created a serializer in serializers.py.
Then i created a view in views.py. Then i created a urls.py in app folder and added path to my view.
Then i run server and checked if it works.
then i created a django project and app. in settings.py i added my database to databases section.
then i created a model in models.py and made migrations. then i created a serializer in serializers.py.
then i created a view in views.py. then i created a urls.py in app folder and added path to my view.
then i added my app to installed apps in settings.py. then i added cors headers to settings.py.
then i added my app urls to main urls.py. then i run server and checked if it works.
then i added

