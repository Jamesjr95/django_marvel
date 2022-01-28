from django.contrib import admin
from .models import Book, Category, Checkout, Author, CheckoutItem

# Register your models here.
admin.site.register([Book, Category, Checkout, Author, CheckoutItem])