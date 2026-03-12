from django.urls import path

from .views import recipe_list, recipe_detail, recipe_add, recipe_add_image

urlpatterns = [
    path("recipes/list/", recipe_list, name="recipe-list"),
    path("recipe/<int:pk>/", recipe_detail, name="recipe-detail"),
    path("recipe/<int:pk>/add_image", recipe_add_image, name="recipe-add_image"),
    path("recipe/add/", recipe_add, name="recipe-add"),
]

app_name = "ledger"
