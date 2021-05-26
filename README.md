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

### Request Response Flow

![](images/req-res-flow.png)

### Simple View and URL

How do views and urls (and apps) all work together?

Below are code snippets of a simple view/url pairing

1. We crated a challenges app in the 02-monthly-challenges project
   - So at this point, we have the challenges and monthly_challenges apps
1. Inside the challenges app we created a simple view and url
1. ```urls.py``` (we had to manually add this)
   ```py
   from django.urls import path
   from . import views

   urlpatterns = [
      path("january", views.index)
   ]
   ```
   - This will route to /challenges/january
   - We don't need the /challenges portion here
1. ```views.py```
   ```py
   from django.shortcuts import render
   from django.http import HttpResponse

   # Create your views here.


   def index(request):
      return HttpResponse("This works!")
   ```
   - We can return an html page as well here!
1. Linking the apps together
   - monthly_challenges > ```urls.py```
   ```py
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
      path('admin/', admin.site.urls),
      path("challenges/", include("challenges.urls"))
   ]
   ```
   - This is why we didn't need to include the challenges/ in the above url def
   