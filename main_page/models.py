from django.db import models
from uuid import uuid4
from os import path
from django.core.validators import RegexValidator
# Create your models here.


class Hero(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/hero', filename)

    title = models.CharField(unique=True, max_length=50)
    desc = models.CharField(max_length=500, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class About(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/about', filename)

    title = models.CharField(unique=True, max_length=50)
    desc = models.CharField(max_length=500, unique=True)
    media_url = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Why_us(models.Model):
    card_number = models.CharField(unique=True, max_length=2)
    title = models.CharField(unique=True, max_length=20)
    desc = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f'{self.title}'



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
        return path.join('images/dishes', filename)

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

class Event(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/event', filename)

    title = models.CharField(unique=True, max_length=50)
    desc = models.CharField(max_length=700, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Gallery(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/gallery', filename)

    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.photo}'


class Chefs(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/chefs', filename)

    title = models.CharField(unique=True, max_length=30)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)
    role = models.CharField(max_length=20)
    twitter_url = models.URLField(default='add twitter url')
    facebook_url = models.URLField(default='add facebook url')
    instagram_url = models.URLField(default='add instagram url')
    linkedin_url = models.URLField(default='add linkedin url')

    def __str__(self):
        return f'{self.title}'


class Testimonials(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/testimonials', filename)

    title = models.CharField(unique=True, max_length=30)
    role = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)
    quote = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.title}'


class Reservations(models.Model):
    mobile_regex = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')

    user_name = models.CharField(max_length=30)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=12, validators=[mobile_regex])
    user_date = models.DateField()
    user_time = models.TimeField()
    number_of_person = models.PositiveIntegerField()
    user_message = models.CharField(max_length=300)

    is_processed = models.BooleanField(default=False)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name} : {self.user_email} : {self.user_message[:20]}'


class Contact(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField()
    user_subject = models.CharField(max_length=40)
    user_message = models.CharField(max_length=500)

    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_name} : {self.user_email} : {self.user_message[:20]}'