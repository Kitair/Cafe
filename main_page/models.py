from django.db import models
from uuid import uuid4
from os import path
# Create your models here.

class Category(models.Model):
    title = models.CharField(unique=True, max_length=50)
    is_visible = models.BooleanField(default=True)
    category_order = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.title}: {self.category_order}'

class Dish(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('media/images/dishes', filename)

    title = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    dish_order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=100)
    desc = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}: {self.price}'
