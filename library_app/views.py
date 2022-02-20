from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Character, Checkout, CheckoutItem
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import connection, reset_queries
import random
from django.contrib import messages 
# Create your views here.


def index(request):
    books = Book.objects.all()
    author = Author.objects.all()
  

    context = {
        'author_name': '',
        'books': books,

    }

    if 'error' in request.session:
        context['error'] = request.session['error']
        del request.session['error']

    if 'late_message' in request.session:
        context['late_message'] = request.session['late_message']
        del request.session['late_message']

    return render(request, 'catalog/index.html', context)


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    checkout_i = CheckoutItem.objects.all()

    checkout = Checkout.objects.get(owner=request.user)
    today = timezone.now()
    today_time = today.strftime("%m/%d/%Y, %H:%M:%S")
    due_date = today + timezone.timedelta(minutes=1)
    print(today_time)

    if not checkout_i.filter(checkout=checkout, book_id=book_id).exists():
        checkout_item, created = CheckoutItem.objects.get_or_create(
            book=book, checkout=checkout)

        checkout_item.quantity += 1
        checkout_item.due_date = due_date
        checkout_item.save()
        messages.success(request, "Cart updated!", extra_tags='success')
    
    elif due_date >= today:
        print(due_date)
        messages.warning(request, "You have overdue comicbooks", extra_tags='warning')

    else:
        messages.warning(request, "You can only checkout one of each comic", extra_tags='warning')

    return redirect(reverse('library_app:index'))

@login_required
def remove_from_cart(request, checkout_item_id):
    checkout_item = get_object_or_404(CheckoutItem, id=checkout_item_id)
    checkout_item.delete()
    return redirect(reverse('users_app:profile'))


def detail(request, book_id):

    books = get_object_or_404(Book, id=book_id)
    author = Author.objects.filter(books=books)[0]

    # author = get_object_or_404(Author, name=name)
    context = {
        'books': books,
        'author': author,
    }
    return render(request, 'catalog/details.html', context)

@login_required
def like(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    print(1)
    print(book_id)

    if request.user not in book.likes.all():
        book.likes.add(request.user)
    else:
        book.likes.remove(request.user)
    print(book_id)
    return JsonResponse({

        'isLiked': request.user in book.likes.all(),
        'likeCount': book.likes.count()
    })


def character(request, character_id):

    character = get_object_or_404(Character, id=character_id)
    # info = Character.objects.filter()
    # books = Book.objects.all().prefetch_related('books')
    context = {
        'character': character,
        # 'books' : books,
    }
    return render(request, 'catalog/character.html', context)
