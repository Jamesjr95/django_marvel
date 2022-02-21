from django.contrib import admin
from .models import Book, Character, Checkout, Author, CheckoutItem, Character

# Register your models here.
admin.site.register([Book, Checkout, Author, CheckoutItem, Character])