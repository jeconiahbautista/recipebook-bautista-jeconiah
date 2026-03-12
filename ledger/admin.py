from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeImage


class RecipeInline(admin.TabularInline):
    model = RecipeIngredient


class ImageInline(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)
    inlines = [RecipeInline, ImageInline]

    fieldsets = [
        (
            "Details",
            {
                "fields": [
                    ("name",),
                ]
            },
        )
    ]


admin.site.register(RecipeIngredient)
admin.site.register(Recipe, RecipeAdmin)
