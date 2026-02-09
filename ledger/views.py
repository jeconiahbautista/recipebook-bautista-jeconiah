from django.shortcuts import render
from .context import recipe_list_context, recipe_1_context, recipe_2_context

def recipe_list(request):
    return render(request, "recipe-list.html", recipe_list_context())

def recipe_1(request):
    return render(request, "recipe-1.html", recipe_1_context())

def recipe_2(request):
    return render(request, "recipe-2.html", recipe_2_context())

