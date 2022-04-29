from ctypes import alignment
from django.core.management.base import BaseCommand
import requests
from library_proj.hidden import *


from library_app.models import Book, Author, Character, get_user_model


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        
        Book.objects.all().delete()
        Author.objects.all().delete()
        Character.objects.all().delete()

        # print(comics)
        loop = 0
        limit = 100
        limit = str(limit)
        offset = 0
        offset = str(offset)

        
        while True:
            offset = str(offset)
           
            url = f'https://gateway.marvel.com:443/v1/public/comics?format=comic&formatType=comic&dateDescriptor=thisMonth&limit={limit}&offset={offset}&ts={ts}&apikey={pub_key}&hash={hasht}'
            response = requests.get(url)
            comics = response.json().get('data').get('results')
            for comic in comics:
            
                title = comic['title']
                image_url = comic['thumbnail']['path']+'/detail.jpg'
                description = comic['textObjects']
                page_count = comic['pageCount']
                issue_number = comic['issueNumber']
                price = comic['prices'][0]['price']
                date = comic['dates'][0]['date'].split('T')[0]
                if description == []:
                    description = None
                else:
                    description = description[0]['text']
                

                
                comic_instance = Book.objects.create(
                    title = title,
                    image_url = image_url,
                    price = price,
                    description = description,
                    page_count = page_count,
                    issue_number = issue_number,
                    date = date
                )
                for hero in comic['characters']['items']:
                    hero = hero['name']
                    hero_url = f'https://gateway.marvel.com:443/v1/public/characters?name={hero}&ts={ts}&apikey={pub_key}&hash={hasht}'
                    response = requests.get(hero_url)
                    hero_info = response.json().get('data').get('results')
                    name = hero_info[0]['name']
                    if description == []:
                        description = 'TBA'
                    else:
                        description = hero_info[0]['description']
                    thumbnail = hero_info[0]['thumbnail']['path']+'/landscape_xlarge.jpg'
                
                    
                    
                    hero, created = Character.objects.get_or_create(
                        name=name,
                        image=thumbnail,
                        description=description,
                    )
                    
                    hero.books.add(comic_instance)
                
                for creator in comic['creators']['items']:
                    name = creator['name']
                    role = creator['role']
                    author, created = Author.objects.get_or_create(
                        name=name,
                        role=role,
                    )
                    comic_instance.authors.add(author)

            loop += 1
            offset = int(offset)
            offset += 100
            if loop == 3:
                return False