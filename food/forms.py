from django import forms
from .models import Meal, Food

class MealForm(forms.ModelForm):

	class Meta:

		model = Meal
		fields = "__all__"


