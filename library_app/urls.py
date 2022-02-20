import imp
from unicodedata import name
from django.urls import path

from . import views

app_name='library_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:book_id>', views.detail, name='detail'),
    path('add-to-cart/<int:book_id>', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:checkout_item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('character/<int:character_id>', views.character, name='character'),
    path('like/<int:book_id>', views.like, name='like'),

]