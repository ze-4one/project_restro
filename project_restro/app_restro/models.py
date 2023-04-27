from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        db_table = "app_categories"

    def __str__(self):
        return self.category_name

class Menu(models.Model):
    menu_title = models.CharField(max_length=50)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    menu_desc = models.CharField(max_length=80)
    menu_img = models.FileField(upload_to="menu/images/")
    menu_ingredient = models.CharField(max_length=80)
    menu_price = models.FloatField()

    class Meta:
        db_table = "app_menus"

    def __str__(self):
        return self.menu_title