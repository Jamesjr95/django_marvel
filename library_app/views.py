from datetime import timedelta, date
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Character, Checkout, CheckoutItem
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.utils import timezone
import requests
from django.contrib import messages 
from django.core.paginator import Paginator

#list view for all comic books
def index(request, page_num=1, per_page=12):
    page_num = request.GET.get('page_num') or page_num
    per_page = request.GET.get('per_page') or per_page
    # books = Book.objects.all()
    books = Book.objects.all().prefetch_related('characters')
    
    books = books.order_by('-date')
    
    
    products_page = Paginator(books, per_page).get_page(page_num)
    context = {
        'products_page': products_page

    }
    
    return render(request, 'catalog/index.html', context)

#list view for all characters
def characters(request,  page_num=1, per_page=12):
    page_num = request.GET.get('page_num') or page_num
    per_page = request.GET.get('per_page') or per_page
    characters = Character.objects.all()
    products_page = Paginator(characters, per_page).get_page(page_num)
    context = {
        'products_page': products_page
    }
    return render(request, 'catalog/characters.html', context)

#add item to logged in user's cart
@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    checkout_item = CheckoutItem.objects.all()
    checkout = Checkout.objects.get(owner=request.user)
    today = timezone.now()
    today_time = today.strftime("%m/%d/%Y, %H:%M:%S")
    due_date = today + timezone.timedelta(days=7)
    checkout_item, created = CheckoutItem.objects.get_or_create(
        book=book, checkout=checkout)
    checkout_item.quantity += 1
    checkout_item.due_date = due_date
    checkout_item.save()
    messages.success(request, "Cart updated!", extra_tags='success')
    return redirect(reverse('library_app:index'))

#update logged in user's cart
@login_required
def update_cart(request, checkout_item_id):
    checkout_item = get_object_or_404(CheckoutItem, id=checkout_item_id)
    new_quantity = request.POST.get('quantity')
    checkout_item.quantity = new_quantity
    checkout_item.save()
    return redirect(reverse('users_app:profile', kwargs= {'username': request.user.username}))

#delete item from logged in user's cart
@login_required
def remove_from_cart(request, checkout_item_id):
    checkout_item = get_object_or_404(CheckoutItem, id=checkout_item_id)
    checkout_item.delete()
    return redirect(reverse('users_app:profile', kwargs={'username': request.user.username}))

#detail view for a book
def detail(request, book_id):
    books = get_object_or_404(Book, id=book_id)
    author = Author.objects.filter(books=books)[0]
    context = {
        'books': books,
        'author': author,
    }
    return render(request, 'catalog/details.html', context)

#view to toggle if a user logged in user likes a book
@login_required
def like(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.user not in book.likes.all():
        book.likes.add(request.user)
    else:
        book.likes.remove(request.user)
    return JsonResponse({

        'isLiked': request.user in book.likes.all(),
        'likeCount': book.likes.count()
    })

#detail view for a character
def character(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    context = {
        'character': character,
    }
    return render(request, 'catalog/character.html', context)

#list view for a search 
def search_query(request):
    books = Book.objects.all()
    search_query = request.POST.get('search-query')
    if search_query:
        search_query = books.filter(
            Q(title__icontains=search_query)
        )
        print(search_query)
  
    context = {
        'search_query': search_query,
    }
    return render(request, 'catalog/search_query.html', context)