from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeImageForm


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
            recipe = form.save(commit=False)
            recipe.author = request.user.profile
            recipe.save()

            return redirect("ledger:recipe-list")

    ctx = {"form": form}

    return render(request, "recipe_add.html", ctx)


@login_required
def recipe_add_image(request, pk):

    form = RecipeImageForm()
    recipe = Recipe.objects.get(pk=pk)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()

            return redirect("ledger:recipe-detail", pk=recipe.pk)

    ctx = {"form": form, "recipe": recipe}

    return render(request, "recipe-add_image.html", ctx)
