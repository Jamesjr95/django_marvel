from datetime import timedelta, date
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Character, Checkout, CheckoutItem
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.utils import timezone
# from django.db import connection, reset_queries
import random
import requests
from django.contrib import messages 
from django.core.paginator import Paginator
# Create your views here.


def index(request, page_num=1, per_page=24):
    
    page_num = request.GET.get('page_num') or page_num
    per_page = request.GET.get('per_page') or per_page

    books = Book.objects.all()
    books = books.order_by('-date')
    
    products_page = Paginator(books, per_page).get_page(page_num)
    
    # results = books.filter(Q(title_icontains=your_search_query))

    
    # startdate = date.today()
    # enddate = startdate - timedelta(days=7)
    
    # newest_comics = books.filter(date__range=[startdate, enddate])
    
    context = {
        # 'newest_comics' : newest_comics,
        'products_page': products_page

    }

    return render(request, 'catalog/index.html', context)

def characters(request,  page_num=1, per_page=24):
    page_num = request.GET.get('page_num') or page_num
    per_page = request.GET.get('per_page') or per_page
    characters = Character.objects.all()
    
    products_page = Paginator(characters, per_page).get_page(page_num)
    
    context = {
        'products_page': products_page
    }
    return render(request, 'catalog/characters.html', context)

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    checkout_item = CheckoutItem.objects.all()

    checkout = Checkout.objects.get(owner=request.user)
    today = timezone.now()
    today_time = today.strftime("%m/%d/%Y, %H:%M:%S")
    due_date = today + timezone.timedelta(minutes=1)
    print(today_time)

    
    checkout_item, created = CheckoutItem.objects.get_or_create(
        book=book, checkout=checkout)

    checkout_item.quantity += 1
    checkout_item.due_date = due_date
    checkout_item.save()
    messages.success(request, "Cart updated!", extra_tags='success')
    
    # elif due_date >= today:
    #     print(due_date)
    #     messages.warning(request, "You have overdue comicbooks", extra_tags='warning')

    # else:
    #     messages.warning(request, "You can only checkout one of each comic", extra_tags='warning')

    return redirect(reverse('library_app:index'))

@login_required
def remove_from_cart(request, checkout_item_id):
    checkout_item = get_object_or_404(CheckoutItem, id=checkout_item_id)
    checkout_item.delete()
    return redirect(reverse('users_app:profile', kwargs={'username': request.user.username}))


def detail(request, book_id):

    books = get_object_or_404(Book, id=book_id)
    author = Author.objects.filter(books=books)[0]
    
    context = {
        'books': books,
        'author': author,
        # 'writer': writer
    }
    return render(request, 'catalog/details.html', context)

@login_required
def like(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    print(1)
    print(book)

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
  
    context = {
        'character': character,
        # 'books' : books,
    }
    return render(request, 'catalog/character.html', context)

def search_query(request):
    books = Book.objects.all()
    # book_id = get_object_or_404(Book, id=book_id)
    # print(book_id)
    
    search_query = request.POST.get('search-query')
    
    if search_query:
        search_query = books.filter(
            Q(title__icontains=search_query)
        )
        print(search_query)
        # for book in search_query:
        #     ids = get_object_or_404(Book, id=book.pk)
        #     print(ids)
    context = {
        'search_query': search_query,
        # 'book': book,
    }

    return render(request, 'catalog/search_query.html', context)