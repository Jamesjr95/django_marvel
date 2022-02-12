from cgitb import text
from django.db import models
from django.contrib.auth import get_user_model
import random

from django.forms import Textarea

# Create your models here.


def get_upload_path(instance, filename):
    return f'images/avatars/{filename}'


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.title

# add a system of holds to the model for the book (many to many to Users),
# keep track of which user has a book on hold

# add library cards model if you finish early

class Book(models.Model):
    title = models.CharField(max_length=50)
    # price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.CharField(max_length=2000, null=True, blank=True)
    image_url = models.CharField(max_length=200)
    stock = models.PositiveIntegerField(default=random.randint(1, 5))
    likes = models.ManyToManyField(
        get_user_model(), related_name='users', blank=True)
    category = models.ManyToManyField(Category, related_name='books')
    def __str__(self):
        return f"{self.title}"

class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    image = models.CharField(max_length=500)
    books = models.ManyToManyField(Book, related_name='characters')

class Author(models.Model):
    role = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return f"{self.name}"



class CheckoutItem(models.Model):
    checkout = models.ForeignKey(
        'Checkout', on_delete=models.CASCADE, related_name='checkout_items')
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='checkout_items')
    quantity = models.PositiveIntegerField(default=0)
    due_date = models.DateField()

    def __str__(self):
        return f'{self.quantity} {self.book}'

class Checkout(models.Model):
    owner = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name='checkout')
    books = models.ManyToManyField(
        Book, through=CheckoutItem, related_name='user_checkout', blank=True)

    class Meta:
        verbose_name = ('Checkout')
        verbose_name_plural = ('Checkout')

    def __str__(self):
        return f"{self.owner}'s cart"
