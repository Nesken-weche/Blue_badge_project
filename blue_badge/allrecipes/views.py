from django.shortcuts import render, redirect
from . import models
# from django.views.generic import UpdateView
# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def all(request):
    if request.method == "POST":
        all_recipes = models.Recipe.objects.get(id=request.POST['id'])
        all_recipes.save()

    recipes_list = models.Recipe.objects.all()
    context = {
        'recipe_list': recipes_list,
    }

    return render(request, 'allrecipes/allrecipes.html', context=context)


def add(request):
    if request.method == "POST":
        my_recipe = models.Recipe(name=request.POST["name"], ingredients=request.POST["ingredients"], instructions=request.POST["instructions"], user=request.user)
        my_recipe.save()

        return redirect('myRecipe')

    return render(request, 'allrecipes/addrecipe.html')

def myrecipe(request):
    my_own_recipe_list = models.Recipe.objects.filter(user=request.user)
    context = {
        'my_recipes_list': my_own_recipe_list,
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
        my_recipe.save()
        
        return redirect('myRecipe')
    
    else:
        my_recipe = models.Recipe.objects.get(id=id)
        name = my_recipe.name
        ingredients = my_recipe.ingredients
        instructions = my_recipe.instructions

        context = {
            'name': name,
            'ingredients': ingredients,
            'instructions': instructions,
            'id': id
        }
        print(id)
        return render(request, 'allrecipes/updaterecipe.html', context=context)


# class Update(UpdateView, LoginRequiredMixin):
#     def Update(request):
#         if request.method == 'POST':
#             model = models.Recipe.objects.get(id=request.POST['id'])
#             fields = ['name', 'ingredients', 'instructions']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

