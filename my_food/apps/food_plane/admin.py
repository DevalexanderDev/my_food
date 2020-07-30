from django.contrib import admin
from .models import Recipe, Ingredient, StepMaking, TypeEating, MenuOnDay

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(StepMaking)
admin.site.register(TypeEating)
admin.site.register(MenuOnDay)