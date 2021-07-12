from django.shortcuts import render
from .models import Why_us, Category, Dish, About, Event, Gallery, Chefs, Testimonials
# Create your views here.


def main_view(request):
    categories = Category.objects.filter(is_visible=True).order_by('-category_order')
    dish = Dish.objects.filter(is_visible=True).filter(is_special=False).order_by('-dish_order')
    dishes_special = Dish.objects.filter(is_special=True)
    about = About.objects.all()
    why_us = Why_us.objects.all()
    event = Event.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    chefs = Chefs.objects.filter(is_visible=True)
    testimonials = Testimonials.objects.filter(is_visible=True)
    return render(request, 'index.html', context={'categories': categories, 'dish': dish,
                                                  'dishes_special': dishes_special, 'about': about[0],
                                                  'why_us': why_us, 'event': event, 'gallery': gallery,
                                                  'chefs': chefs, 'testimonials': testimonials})

