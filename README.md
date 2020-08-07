# WhatsWeather_Now

# Screenshots.
![whatweather](https://user-images.githubusercontent.com/50301680/89639854-fe062e00-d8cb-11ea-9d2f-055896225783.png)








# Create a Virtual Environment
It’s common practice to use a virtual environment for your Python projects in order to create self-contained development environments. The goal of pyenv is to prevent different versions of Python and libraries/packages from messing with each other. It’s like an isolated, soundproof room within your home where you can scream as loud as you want, about anything you want, and nobody else outside that room can hear it.

# Use pyenv-virtualenv to create a virtual environment for your project:

pyenv virtualenv [project-name]
pyenv activate [project-name]
Create environment variables file - .env
This file will serve as environment variables that will serve our project. Django and Docker mostly will use this file.

Here is an example of .env file:

SECRET_KEY=[secret-key]

DEBUG=true

DJANGO_SETTINGS_MODULE=django_config.settings.local

ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0

DATABASE_URL=postgres://django:[password]@localhost:5432/[project-name]


MAILGUN_API_KEY=[mailgun-api-key]

MAILGUN_DEFAULT_FROM_EMAIL=[email]

POSTGRES_PASSWORD=[password]

POSTGRES_USER=django

POSTGRES_DB=[project-name]

EMAIL_PORT=1025

EMAIL_HOST=localhost

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend

DEFAULT_FROM_EMAIL=[email]



# Installing an official release with pip¶
This is the recommended way to install Django.

Install pip. The easiest is to use the standalone pip installer. If your distribution already has pip installed, you might need to update it if it’s outdated. If it’s outdated, you’ll know because installation won’t work.

Take a look at venv. This tool provides isolated Python environments, which are more practical than installing packages systemwide. It also allows installing packages without administrator privileges. The contributing tutorial walks through how to create a virtual environment.

After you’ve created and activated a virtual environment, enter the command:

$ python -m pip install Django


## Creating a project¶
If this is your first time using Django, you’ll have to take care of some initial setup. Namely, you’ll need to auto-generate some code that establishes a Django project – a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

From the command line, cd into a directory where you’d like to store your code, then run the following command:

$ django-admin startproject mysite




#  Let’s look at what startproject created:

mysite/

    manage.py
    
    mysite/
    
        __init__.py
        
        settings.py
        
        urls.py
        
        asgi.py
        
        wsgi.py
        
        
        
        
# The development server¶
### Let’s verify your Django project works. Change into the outer mysite directory, if you haven’t already, and run the following commands:


$ python manage.py runserver
You’ll see the following output on the command line:

Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

August 07, 2020 - 15:50:53

Django version 3.1, using settings 'mysite.settings'

Starting development server at http://127.0.0.1:8000/

Quit the server with CONTROL-C.






# Developed By  

SHIVANT KUMAR PANDEY

Email: shivant47@gmail.com

[LinkedIn!](https://www.linkedin.com/in/shivant-kumar-pandey-6469a1164/)


























