#from .views import form_view
from . import views
from django.urls import path

urlpatterns = [
    # Nueva url a form
    path('form/', views.form_view)
    ]