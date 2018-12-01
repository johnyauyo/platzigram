"""platzigram URL Configuration
Punto de entrada para todas las peticiones que lleguen 
al proyecto de Django

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse
from platzigram import views as local_views
from posts import views as posts_views

#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

#esto en django se constituye como una vista, pero es recomendable que este fuera
#para que la aplicacion sea escalable

#def hello_world(request):
#    return HttpResponse('<p><b>Hello World</b></>')

urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('hi/', local_views.hi),
    path('sort/', local_views.sort_integers),
    path('hi2/<str:name>/<int:age>/',local_views.say_hi),
    path('posts/',posts_views.list_posts),
]