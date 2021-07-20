from django.urls import path
from .views import *

urlpatterns = [
    path('reserve/', list_of_reserves, name='list_of_reserves'),
    path('reserve/update/<int:pk>/', update_reserve, name='update_reserve')
]