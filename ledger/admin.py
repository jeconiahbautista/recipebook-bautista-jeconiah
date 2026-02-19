from django.contrib import admin

from .models import Recipe, RecipeIngredient
# Register your models here.

class RecipeInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    inlines = [RecipeInline,]

    fieldsets = [
        ('Details', {
            'fields': [
                ('name',),
            ]
        })
    ]

admin.site.register(RecipeIngredient)
admin.site.register(Recipe, RecipeAdmin)
