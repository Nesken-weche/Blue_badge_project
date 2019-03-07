from django.urls import path

from . import views 

urlpatterns = [
    path('', views.all, name='mylist'),
    path('add/', views.add, name='addRecipe'),
    path('delete/', views.delete, name='deleteRecipe'),
]