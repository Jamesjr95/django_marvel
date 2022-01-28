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

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    checkout = Checkout.objects.get(owner=request.user)

    checkout_item, created = CheckoutItem.objects.get_or_create(book=book, checkout=checkout)

    checkout_item.quantity += 1
    checkout_item.save()

    return redirect(reverse('library_app:index'))
