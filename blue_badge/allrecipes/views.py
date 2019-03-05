from django.shortcuts import render, redirect
from . import models

# Create your views here.
def all(request):
    if request.method == "POST":
        my_recipe = models.Recipe.objects.get(id=request.POST['id'])
        my_recipe.save()

    recipes_list = models.Recipe.objects
    context = {
        'recipe_list': recipes_list,
    }

    return render(request, 'allrecipes/allrecipes.html', context=context)

def add(request):
    if request.method == "POST":
        my_recipe = models.Item(name=request.POST["name"], ingredients=request.POST["ingredients"], instructions=request.POST["instructions"])
        my_recipe.save()

        # return redirect('myList')
        return redirect('allRecipes')

    return render(request, 'allrecipes/addrecipe.html')

