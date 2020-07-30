from django.db import models
from django.contrib.auth.models import User
from apps.files.models import File 


class Recipe(models.Model):
	name = models.CharField(name="name", max_length=30)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	create_date = models.DateField()
	description = models.TextField()
	calories = models.IntegerField(default=0)
	protein = models.IntegerField(default=0)
	fat = models.IntegerField(default=0)
	carbohydrates = models.IntegerField(default=0)
	img = models.ForeignKey(File, on_delete=models.CASCADE)

	class Meta:
		db_table = 'recipe'

class Ingredient(models.Model):
	name = models.CharField(max_length=30)
	calories = models.IntegerField(default=0)
	protein = models.IntegerField(default=0)
	fat = models.IntegerField(default=0)
	carbohydrates = models.IntegerField(default=0)
	unit_size = models.IntegerField()
	img = models.ForeignKey(File, on_delete=models.CASCADE)

	class Meta:
		db_table = 'ingredient'

class IngredientToRecipe(models.Model):
	count = models.IntegerField(default=1)
	recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

	class Meta:
		db_table = 'ingredient_to_recipe'

class StepMaking(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=30)
	img = models.ForeignKey(File, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	class Meta:
		db_table = 'step_making'

class StepMakingToRecipe(models.Model):
	step_making_id = models.ForeignKey(StepMaking, on_delete=models.CASCADE)
	recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)

	class Meta:
		db_table = 'step_making_to_recipe'

class TypeEating(models.Model):
	time = models.TimeField()
	name = models.CharField(max_length=30)
	description = models.TextField()
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	class Meta:
		db_table = 'type_eating'

class MenuOnDay(models.Model):
	type_eat = models.ForeignKey(TypeEating, on_delete=models.SET_NULL, null=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	recipe_id = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)
	date = models.DateField()

	class Meta:
		db_table = 'menu_on_day'

class StatisticCaloriesToMenuOnDay(models.Model):
	calories = models.IntegerField(default=0)
	fat = models.IntegerField(default=0)
	carbohydrates = models.IntegerField(default=0)
	protein = models.IntegerField(default=0)
	menu_on_day_id = models.ForeignKey(MenuOnDay, on_delete=models.CASCADE)

	class Meta:
		db_table = 'statistic_calories_to_menu_on_day'


