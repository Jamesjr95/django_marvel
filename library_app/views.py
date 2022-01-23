from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Category, Checkout, CheckoutItem
from django.db.models import Q

# Create your views here.
def index(request):
    book = Book.objects.all()

    category_options = {
        'categories': [category.title for category in Category.objects.all()]
        
    }

    context = {
        'category_options': category_options,
        'book': book
    }

    return render(request, 'catalog/index.html', context)