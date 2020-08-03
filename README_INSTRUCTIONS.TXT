TO CREATE A NEW DJANGO PROJECT:
  - create a new env first
  > python -m pip install django
  > python -m django --version  // just to make sure
  > django-admin startproject django_proj_name

TO RUN THE SERVER:
  > python manage.py runserver

TO CREATE NEW APP INSIDE THE PROJECT:
  > python manage.py startapp blog
  > tree (to see the hierarchy)

TO ADD APPS INTO SETTINGS:
  - look inside blogs/apps.py and grab the 'BlogConfig' name
  - then open django_blog/settings.py and add a path to that path configuration
  - INSTALLED_APPS = [
    'blog.apps.BlogConfig',