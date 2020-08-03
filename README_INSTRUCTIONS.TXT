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

TO CREATE ADMIN USER TO LOGIN TO /ADMIN PAGE:
  > python manage.py createsuperuser
  - returns error though: django.db.utils.OperationalError: no such table: auth_user
  - so we need to create an 'auth_user' table
  > python manage.py makemigrations
  - nothing to see here though so we want to run
  > python manage.py migrate
  > python manage.py createsuperuser
  - vannachan/testing123
  - TestUser/testing321

TO CREATE NEW MODEL AND MIGRATE:
  - add your table to models.py
  > python manage.py makemigrations
  - that will output the migrations file
  - to see the SQL that will actually run:
    > python manage.py sqlmigrate blog 0001
    - that's why Object Relational Mappers are so useful
  > python manage.py migate

TO INTERACT WITH MODELS USING CMD:
  > python manage.py shell
  > from blog.models import Post
  > from django.contrib.auth.models import User
  > User.objects.all()
  <QuerySet [<User: vannachan>, <User: TestUser>]>
  > User.objects.filter(username='vannachan').first()
  > user = User.objects.filter(username='vannachan').first()
  > user.id

CREATE NEW POST:
  > Post.objects.all()
  > post_1 = Post(title='Blog1', content='First Post content!', author=user)
  > post_1.save()
  > Post.objects.all()
  > post_2 = Post(title='Blog1', content='First Post content!', author_id=user.id)
  > user.post_set.all()
  TO CREATE USING post_set, DON'T NEED TO SAVE():
    > user.post_set.create(title='Blog 3', content='Third post content!')

THIRD PARTY APP TO MAKE FORMS NICER:
  - deactivate virtual env
  > pip install django-crispy-forms
  - activate virtual env
  - add in settings.py for INSTALLED_APPS
  - change to bootstrap4 for css: 
  CRISPY_TEMPLATE_PACK = 'bootstrap4'