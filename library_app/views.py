from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Category, Checkout, CheckoutItem
from django.db.models import Q
from django.contrib.auth import get_user_model
# Create your views here.
import random


def index(request):
    books = Book.objects.all()
    author = Author.objects.all()
    author_name = ''
    
    for book in books:
        author_name = author.filter(books=book)[0]
        print(author_name)
    
    category_options = {
        'categories': [category.title for category in Category.objects.all()]
    }

    def filter_list(category):
        return list(dict.fromkeys(category))
    book_category = Category.objects.all()
    psychological = filter_list(books.filter(
        category__title__icontains='Psychological'))
    historical = filter_list(books.filter(
        category__title__icontains='historical'))
    politics = filter_list(books.filter(
        category__title__icontains='political'))
    poetry = filter_list(books.filter(category__title__icontains='poetry'))
    comedy = filter_list(books.filter(category__title__icontains='Humorous'))
    drama = filter_list(books.filter(category__title__icontains='drama'))

    context = {
        'category_options': category_options,
        'author_name': '',
        'books': books,
        'psychological': psychological,
        'historical': historical,
        'politics': politics,
        'poetry': poetry,
        'comedy': comedy,
        'drama': drama,
    }

    if 'error' in request.session:
        context['error'] = request.session['error']
        del request.session['error']

    return render(request, 'catalog/index.html', context)


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    checkout_i = CheckoutItem.objects.all()

    checkout = Checkout.objects.get(owner=request.user)

    if not checkout_i.filter(checkout=checkout, book_id=book_id).exists():
        checkout_item, created = CheckoutItem.objects.get_or_create(
            book=book, checkout=checkout)

        checkout_item.quantity += 1
        checkout_item.save()
    else:
        request.session['error'] = 'Can only checkout one of each book'

    return redirect(reverse('library_app:index'))


def detail(request, book_id):

    books = get_object_or_404(Book, id=book_id)
    author = Author.objects.filter(books=books)[0]

    # author = get_object_or_404(Author, name=name)
    context = {
        'books': books,
        'author': author,
    }
    return render(request, 'catalog/details.html', context)
