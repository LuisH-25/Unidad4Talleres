"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from myapp.views import aula_view, form_view, index_view, vista1_view, vista2_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", index_view, name="home"),
    path('', index_view.as_view(), name="home"),
    path('vista1/', vista1_view.as_view(), name="home"),
    path('vista2/', vista2_view.as_view(), name="home"),
    # path('vista-inicio/', index_view, name="home2"),    # Para vistas como metodos
    #path('formulario/', form_view.as_view(), name="formulario"),    # Para vistas como clases
    #path('form/', form_view, name="formulario"),
    path('formulario/', include('myapp.urls')),
    
    path("formulario/<aula>/<horario>", aula_view, name="aula")

]
