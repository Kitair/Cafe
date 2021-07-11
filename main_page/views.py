from django.shortcuts import render
from .models import Category, Dish, About

# Create your views here.


def main_view(request):
    categories = Category.objects.filter(is_visible=True).order_by('-category_order')
    dish = Dish.objects.filter(is_visible=True).filter(is_special=False).order_by('-dish_order')
    dishes_special = Dish.objects.filter(is_special=True)
    about = About.objects.all()
    return render(request, 'index.html', context={'categories': categories, 'dish': dish,
                                                  'dishes_special': dishes_special, 'about': about[0]})

