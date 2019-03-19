from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery
from . import models


# Create your views here.
def all(request):
    if request.method == "POST":
        all_recipes = models.Recipe.objects.get(id=request.POST['id'])
        all_recipes.save()

    recipes_list = models.Recipe.objects.filter(publish=True)
    paginator= Paginator(recipes_list, 5)
    page = request.GET.get('page')
    contacts=paginator.get_page(page)

    for r in recipes_list:
        print(r.image)

    context = {
        'recipe_list': contacts,
        'contacts': contacts,
    }

    return render(request, 'allrecipes/allrecipes.html', context=context)

def add(request):
    if request.method == "POST":
        if request.FILES:
            image = request.FILES['upload']
            print(image)
            my_recipe = models.Recipe(name=request.POST["name"], ingredients=request.POST["ingredients"], instructions=request.POST["instructions"], user=request.user, image=request.FILES['upload'])
        my_recipe = models.Recipe(name=request.POST["name"], ingredients=request.POST["ingredients"], instructions=request.POST["instructions"], user=request.user)
        
        if 'publish' in request.POST:
            my_recipe.publish = True
        my_recipe.save()
        return redirect('myRecipe')
    return render(request, 'allrecipes/addrecipe.html')       
        
def myrecipe(request):
    my_own_recipe_list = models.Recipe.objects.filter(user=request.user)
    paginator= Paginator(my_own_recipe_list, 5)
    page = request.GET.get('page')
    contacts=paginator.get_page(page)

    context = {
        'my_recipes_list': contacts,
        'contacts': contacts,
    }

    return render(request, 'users/profile.html', context=context)

def delete(request):
    if request.method == 'POST':
        my_recipe = models.Recipe.objects.get(id=request.POST['id'])
        my_recipe.delete()

        return redirect('myRecipe')

def update(request, id):
    if request.method == 'POST':
        my_recipe = models.Recipe.objects.get(id=id)
        my_recipe.name = request.POST["name"]
        my_recipe.ingredients = request.POST["ingredients"]
        my_recipe.instructions = request.POST["instructions"]
        # my_recipe.image = request.FILES["image"]
        if 'upload' in request.FILES:
            my_recipe.image = request.FILES['upload']
        if 'publish' in request.POST:
            my_recipe.publish = True
        else:
            my_recipe.publish = False
        my_recipe.save()
        
        return redirect('myRecipe')
    
    else:
        my_recipe = models.Recipe.objects.get(id=id)
        if my_recipe.user != request.user:
            return redirect('homePage')
        name = my_recipe.name
        ingredients = my_recipe.ingredients
        instructions = my_recipe.instructions
        image = my_recipe.image
        publish = my_recipe.publish

        context = {
            'name': name,
            'ingredients': ingredients,
            'instructions': instructions,
            'image': image,
            'id': id,
            'publish': publish
        }
        print(id)
        return render(request, 'allrecipes/updaterecipe.html', context=context)

def querysearch(request):
    querset = models.Recipe.objects.filter(publish=True)
    keywords = request.GET.get('search')

    if request.method == "POST":
        query = SearchQuery(keywords)
        vector = SearchVector('name', weight='A') + SearchVector('ingredients', weight='B') + SearchVector('instructions', weight='C')
        querset = querset.annotate(search=vector).filter(search=query)
        querset = querset.annotate(rank=SearchRank(vector, query))

    paginator= Paginator(querset, 5)
    page = request.GET.get('page')
    contacts=paginator.get_page(page)
    
    context = {
        'querset': querset,
        'contacts': contacts,
    }
    return render(request, 'allrecipes/searchresults.html', context=context)

