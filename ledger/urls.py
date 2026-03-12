from django.urls import path

from .views import recipe_list, recipe_detail, recipe_add

urlpatterns = [
    path("recipes/list/", recipe_list, name="recipe-list"),
    path("recipe/<int:pk>/", recipe_detail, name="recipe-detail"),
    path("recipe/add/", recipe_add, name="recipe-add"),
]

app_name = "ledger"
