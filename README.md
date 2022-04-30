## What is dJango --- High level python web framework

### Features of dJango
- Object-relational mapping (ORM)
- URL routing
- HTML templating
- Form handling
- Unit Testing

### dJango is not -
- A programming language
- A web server

### Create Project - 
- django-admin startproject projectName
- In created project file ---
  - manage.py --> Runs commands --> We'll not edit
  - projectName/__init__.py --> Tells Python that the folder contains Python code --> We'll not edit
  - projectName/wsgi.py or asgi.py --> Provide hooks for the web server such as --> appache or engineX in dJango running on live server --> We'll not edit
  - projectName/setting.py --> Configure the dJango project
  - projectName/urls.py --> Routes web requests based on URL

### Run Project -
- Go the project folder and run this command --> python3 manage.py runserver
- Create a APP --> python3 manage.py startapp appName
  - Migration Commands:
    - python3 manage.py makemigrations -->
      - Genarates migration files for later use
      - Uses Current model fields and current database tables
      - Creates numbered files in appname/migrations/

    - python3 manage.py showmigrations

    - python3 manage.py migrate -->
      - Runs alll migrations in the project to the current state
      - Can also run only7 migrations in a specific app to specific number using:
        Example: $python3 manage.py migrate <appname> <number>
                 $python3 manage.py migrate adoption 1 --> To migrate to the first migration for the adoption app

### dJango File -
- apps.py --> Control settings for specific to this app.
- models.py --> Provides data layer which is dJango uses to constract our database schema and queries.
- admin.py --> Defines the addministrative interface for the app that allow to see and edit the data related to this app.
- urls.py --> Can be used urls routing to specific to this app.
- views.py --> Defines the logic file and control flow for handling request and defines the http responses that retuned.
- tests.py --> Can be used for writting unit test for the funcitonality of this app.
- migrations/ --> Hold files which dJango uses to migrate the database as we create and change our database schema over time.

### Architecture of dJango -
- MVC Architecture --> Model-View-Controller (Probably dJango uses this)
- dJango uses some different name for this -->
  - dJango Architecture --> URL patterns, views, models, templates

### dJango Models -
- Create the data layer of a dJango app
- Define database structure
- Allow us to query the database

### dJango Admin (Create Super User) -
- python3 manage.py createsuperuser


### shortcut - 
- django-admin startproject projectName
- cd projectName
- python manage.py makemigrations
- python manage.py showmigrations // no need
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
- python manage.py startapp appName
- python manage.py makemigrations
- python manage.py migrate