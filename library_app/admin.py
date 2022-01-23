from django.contrib import admin
from .models import Book, Category, Checkout

# Register your models here.
admin.site.register([Book, Category, Checkout])