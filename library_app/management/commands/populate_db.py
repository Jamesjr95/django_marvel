from django.core.management.base import BaseCommand
import requests
import json
import hashlib
from hidden import *


from library_app.models import Book, Category, Author, Character, get_user_model


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        
        Book.objects.all().delete()
        Author.objects.all().delete()

        url = f'https://gateway.marvel.com:443/v1/public/comics?format=comic&formatType=comic&dateRange=2017-01-01%2C2019-01-02&limit=10&ts={ts}&apikey={pub_key}&hash={hasht}'
        
        index = 0
        response = requests.get(url)
        comics = response.json().get('data').get('results')
        # print(comics)
        

        for comic in comics:
        
            title = comics[index]['title']
            print(title)
            image_url = comics[index]['thumbnail']['path']+'/portrait_xlarge.jpg'
            description = comics[index]['textObjects']
            page_count = comics[index]['pageCount']
            issue_number = comics[index]['issueNumber']
            if description == []:
                description = None
            else:
                description = description[0]['text']
                # print(description)
            

            
            comic = Book.objects.create(
                title = title,
                image_url = image_url,
                description = description,
                page_count = page_count,
                issue_number = issue_number,
            )
            for hero in comics[index]['characters']['items']:
                hero = hero['name']
                hero_url = f'https://gateway.marvel.com:443/v1/public/characters?name={hero}&ts={ts}&apikey={pub_key}&hash={hasht}'
                response = requests.get(hero_url)
                hero_info = response.json().get('data').get('results')
                name = hero_info[0]['name']
                if description == []:
                    description = None
                else:
                    description = hero_info[0]['description']
                thumbnail = hero_info[0]['thumbnail']['path']+'/portrait_xlarge.jpg'
                
                hero, created = Character.objects.get_or_create(
                    name=hero,
                    image=thumbnail,
                    description=description,
                )
                hero.books.add(comic)
            
            for creator in comics[index]['creators']['items']:
                name = creator['name']
                role = creator['role']
                author, created = Author.objects.get_or_create(
                    name=name,
                    role=role,
                )
                comic.authors.add(author)

        

            index += 1
            # characters, created = 
            # for category in map(str, category):
            #     category = category_query(category)
            #     category, created = Category.objects.get_or_create(
            #         title=category)
            #     book.category.add(category)
            
