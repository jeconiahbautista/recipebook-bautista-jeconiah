from django.shortcuts import render
from django.http import HttpResponse

def recipe_list(request):
    return HttpResponse("Recipe Book")

def recipe_1(request):
    return HttpResponse("Recipe 1")

def recipe_2(request):
    return HttpResponse("Recipe 2")

# Create your views here.
