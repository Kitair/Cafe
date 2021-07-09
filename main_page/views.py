from django.shortcuts import render
from .models import Category, Dish

# Create your views here.


def main_view(request):
    categories = Category.objects.filter(is_visible=True).order_by('-category_order')
    dish = Dish.objects.filter(is_visible=True).order_by('-dish_order')
    return render(request, 'index.html', context={'categories': categories, 'dish': dish})

