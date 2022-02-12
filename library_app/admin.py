from django.contrib import admin
from .models import Book, Category, Character, Checkout, Author, CheckoutItem, Character

# Register your models here.
admin.site.register([Book, Category, Checkout, Author, CheckoutItem, Character])