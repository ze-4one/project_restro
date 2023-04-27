from .models import Category, Menu
from django import forms

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        fields = ("category_name",)
        model = Category

class MenuCreateForm(forms.ModelForm):
    class Meta:
        fields = ("menu_title", "category_id", "menu_desc", "menu_ingredient", "menu_price")
        model = Menu