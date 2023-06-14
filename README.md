## SQL SERVER 2019 DATABASE WITH DJANGO WEB APP

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
```

The most important thing was the engine and in this case, using Microsoft SQL Server 2019, engine is mssql. Name is the
name of the database created in SSMS. User and password was made in the security section of properties of the database.
SQL Server and Windows Authentication mode should be set in security page in properties of the server.
Port should be set to ''. Next important thing is setting the driver options ODBC Driver 17 for SQL Server with the
params 'TrustServerCertificate' set to yes. Also in database should be added parameter.



