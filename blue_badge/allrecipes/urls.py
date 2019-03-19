from django.urls import path

from . import views 

urlpatterns = [
    path('update/<int:id>', views.update, name="updateRecipe"),
    path('profile/', views.myrecipe, name="myRecipe"), 
    path('all/', views.all, name="allRecipes"),
    path('add/', views.add, name="addRecipe"),
    path('delete/', views.delete, name="delRecipe"),
    path('search/', views.querysearch, name="searchRecipes"),
]
