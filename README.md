# Django Bootcamp

1. Python web development framework
1. Python 3.x
1. Customizable and extensible

## Django Setup

1. Install [Python](https://www.python.org/downloads/)
1. Install Django
   ```
   pip install Django
   ```
1. Confirm Django installed
   ```
   django-admin
   ```
1. Create a Django project
   ```
   django-admin startproject
   ```
1. Formatting and Linting
   ```
   pip install pylint
   ```
   ```
   pip install autopep8
   ```
   - I ran into issues w/ prettier and autopep
   - Had to disable prettier and make sure autopep was the formatter for python
1. Launch development server
   ```
   python manage.py runserver
   ```
1. In Django, modules are called **Apps**
   ```
   python manage.py startapp challenges
   ```
   ![](images/django-apps.png)
   - Can scale up and down in terms of size
1. [Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
   - It is recommended to use a virutal environment when developing in Django (and python in general)

## URLs and Views

### URLs/Routes

![](images/urls.png)

### Views

![](images/views.png)