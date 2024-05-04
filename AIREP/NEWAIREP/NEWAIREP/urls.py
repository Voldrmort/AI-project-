from django.urls import path
from NEWAIREP.airep_scripts import views

urlpatterns = [
    path('', views.index, name='index'),  # Map the index view to the root url
]