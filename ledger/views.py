from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm


def recipe_list(request):
    recipes = Recipe.objects.all()

    ctx = {"recipes": recipes}

    return render(request, "recipe-list.html", ctx)


@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    ctx = {"recipe": recipe}

    return render(request, "recipe.html", ctx)


@login_required
def recipe_add(request):
    form = RecipeForm()

    if request.method == "POST":
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save()
            recipe.save()

            return redirect("ledger:recipe-add")

    ctx = {"form": form}

    return render(request, "recipe_add.html", ctx)
