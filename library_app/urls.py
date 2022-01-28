import imp
from unicodedata import name
from django.urls import path

from . import views

app_name='library_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('add-to-cart/<int:book_id>', views.add_to_cart, name='add_to_cart'),

]