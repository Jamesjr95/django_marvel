from cgitb import text
from django.db import models
from django.contrib.auth import get_user_model
import random

from django.forms import Textarea

# Create your models here.


def get_upload_path(instance, filename):
    return f'images/avatars/{filename}'


class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.CharField(max_length=2000, null=True, blank=True)
    image_url = models.CharField(max_length=200)
    stock = models.PositiveIntegerField(default=random.randint(1, 5))
    likes = models.ManyToManyField(
        get_user_model(), related_name='users', blank=True)
    page_count = models.PositiveIntegerField()
    issue_number = models.PositiveIntegerField()
    date = models.DateField()

    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return f"{self.title}"

class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    image = models.CharField(max_length=500)
    books = models.ManyToManyField(Book, related_name='characters')
    gender = models.CharField(max_length=100, null=True, blank=True)
    race = models.CharField(max_length=100, null=True, blank=True)
    height = models.CharField(max_length=100, null=True, blank=True)
    weight = models.CharField(max_length=100, null=True, blank=True)
    alighnment = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'

class Author(models.Model):
    role = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='authors')
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"



class CheckoutItem(models.Model):
    checkout = models.ForeignKey(
        'Checkout', on_delete=models.CASCADE, related_name='checkout_items')
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='checkout_items')
    quantity = models.PositiveIntegerField(default=0)
    due_date = models.DateField(null=True, blank=True)

    def item_total_price(self):
        return self.quantity * self.book.price

    def __str__(self):
        return f'{self.quantity} {self.book}'

class Checkout(models.Model):
    owner = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name='checkout')
    books = models.ManyToManyField(
        Book, through=CheckoutItem, related_name='user_checkout', blank=True)

    def item_count(self):
        count = 0
        for checkout_item in self.checkout_items.all():
            count += checkout_item.quantity
        return count

    def total_price(self):
        total = 0
        for checkout_item in self.checkout_items.all():
            total += checkout_item.item_total_price()
        return total
    class Meta:
        verbose_name = ('Checkout')
        verbose_name_plural = ('Checkout')

    def __str__(self):
        return f"{self.owner}'s cart"
