from django.urls import path

from . import views 

urlpatterns = [
    path('update/<int:id>', views.update, name="updateRecipe"),
    path('mine/', views.myrecipe, name="myRecipe"), 
    path('all/', views.all, name="allRecipes"),
    path('add/', views.add, name="addRecipe"),
    path('delete/', views.delete, name="delRecipe"),
]