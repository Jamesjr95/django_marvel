from django.core.management.base import BaseCommand
import requests
import json
import hashlib
from hidden import *


from library_app.models import Book, Category, Author, Character, get_user_model


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        
        # Book.objects.all().delete()
        # Category.objects.all().delete()
        # Author.objects.all().delete()

        url = f'https://gateway.marvel.com:443/v1/public/comics?format=comic&formatType=comic&ts={ts}&apikey={pub_key}&hash={hasht}'
        
        index = 0
        response = requests.get(url)
        comics = response.json().get('data').get('results')
        print(comics)
        
        char_url = f'https://gateway.marvel.com:443/v1/public/characters?&ts={ts}&apikey={pub_key}&hash={hasht}'
        response = requests.get(char_url)
        char = response.json().get('data').get('results')
        # print(char)
        # for hero in char:

        
        # characters = comics[index]['characters']['items']
        # print(characters)
        character_list = comics[index]['characters']['items']['name']
        print(character_list)
        # for comic in comics:
        
        #     title = comics[index]['title']
        #     image_url = comics[index]['thumbnail']['path']+'/portrait_xlarge.jpg'
        #     description = comics[index]['textObjects']
        #     # character_list = comics[index]['CharacterList']
        #     if description == []:
        #         description = None
        #     else:
        #         description = description[0]['text']
        #         print(description)
            
        #     comic = Book.objects.create(
        #         title = title,
        #         image_url = image_url,
        #         description = description,
        #     )
        #     print(comic)
            
        #     # character, created = Character.objects.get_or_create(

        #     # )
            
        #     for creator in comics[index]['creators']['items']:
        #         name = creator['name']
        #         print(name)
        #         role = creator['role']
        #         author, created = Author.objects.get_or_create(
        #             name=name,
        #             role=role,
        #         )
        #         comic.authors.add(author)

        
        #         # author.books.add(book)
        #     # characters = comics[index]['characters']['items']
        #     # characters = characters_search(characters)
            
        #     # print(summary)

        #     index += 1
            # characters, created = 
            # for category in map(str, category):
            #     category = category_query(category)
            #     category, created = Category.objects.get_or_create(
            #         title=category)
            #     book.category.add(category)
            
