from django.urls import path
from . import views


urlpatterns = [
    #path(URL, Function you want to execute, 'name of the url')
    path('', views.index, name='index')
]
