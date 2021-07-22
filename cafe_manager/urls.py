from django.urls import path
from .views import *





urlpatterns = [
    path('reserve/', list_of_reserves, name='list_of_reserves'),
    path('reserve/update/<int:pk>/', update_reserve, name='update_reserve'),
    path('categories/', list_of_categories, name='list_of_categories'),
    path('categories/add', CategoryAddView.as_view(), name='categories_add'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='categories_update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='categories_delete'),
]