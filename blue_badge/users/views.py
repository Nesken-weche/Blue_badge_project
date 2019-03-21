from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.core.paginator import Paginator
from . import models
from allrecipes import models

# Create your views here.

def register(request):
   if request.method == 'POST':
       form = UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f'Your account has been created! you are now able to log in')
           return redirect('login')
   else:
       form = UserRegisterForm()
   return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
   if request.method == 'POST':
       u_form = UserUpdateForm(request.POST, instance=request.user)
       p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
       if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request, f'Your account has been updated!')
           return redirect('myRecipe')

   else:
       u_form = UserUpdateForm(instance=request.user)
       p_form = ProfileUpdateForm(instance=request.user.profile)

   context = {
       'u_form': u_form,
       'p_form': p_form
   }

   return render(request, 'users/edit_profile.html', context)

def user_recipes(request, username):
    user1 = User.objects.get(username=username)
    if user1 == request.user:
        my_own_recipe_list = models.Recipe.objects.filter(user=request.user)
        paginator= Paginator(my_own_recipe_list, 5)
        page = request.GET.get('page')
        contacts=paginator.get_page(page)

        selfcontext = {
            'my_recipes_list': contacts,
            'contacts': contacts,
        }

        return render(request, 'users/profile.html', context=selfcontext)
    else:
        recipes_list = models.Recipe.objects.filter(publish=True, user=user1)  
        paginator= Paginator(recipes_list, 5)
        page = request.GET.get('page')
        contacts=paginator.get_page(page)

        context = {
            'user_recipes': contacts,
            'recipe_list': contacts,
            'contacts': contacts,
            'user1': user1,
        }

        return render(request, 'users/userprofilebase.html', context=context)
