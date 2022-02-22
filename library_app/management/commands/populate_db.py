from ctypes import alignment
from django.core.management.base import BaseCommand
import requests
from hidden import *


from library_app.models import Book, Author, Character, get_user_model


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        
        Book.objects.all().delete()
        Author.objects.all().delete()
        Character.objects.all().delete()

        # print(comics)
        loop = 0
        limit = '100'
        offset = '0'
        
    
        url = f'https://gateway.marvel.com:443/v1/public/comics?format=comic&formatType=comic&dateDescriptor=thisMonth&limit={limit}&offset={offset}&ts={ts}&apikey={pub_key}&hash={hasht}'
        index = 0
        response = requests.get(url)
        print(response)
        comics = response.json().get('data').get('results')
        for comic in comics:
        
            title = comic['title']
            image_url = comic['thumbnail']['path']+'/detail.jpg'
            description = comic['textObjects']
            page_count = comic['pageCount']
            issue_number = comic['issueNumber']
            date = comic['dates'][0]['date'].split('T')[0]
            if description == []:
                description = None
            else:
                description = description[0]['text']
                # print(description)
            

            
            comic_instance = Book.objects.create(
                title = title,
                image_url = image_url,
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
                thumbnail = hero_info[0]['thumbnail']['path']+'/detail.jpg'
                # print('create hero', name)
                # print(thumbnail)
                # print(description)

                # hero_stats = {} 

                # stats = f'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
                # stat_response = requests.get(stats)
                # stat_response = stat_response.json()
                # stat_response = stat_response
                
                print(hero)
                # for item in stat_response:
                    
                #     if hero in item.values():
                #         appearance = item.get('appearance')
                #         hero_stats['gender'] = appearance.get('gender')
                #         hero_stats['race'] = appearance.get('race')
                #         hero_stats['height'] = appearance.get('height')[0]
                #         hero_stats['weight'] = appearance.get('weight')[0]
                #         alignment = item.get('biography')
                #         hero_stats['alighnment'] = alignment.get('alignment')
                
                
                hero, created = Character.objects.get_or_create(
                    name=name,
                    image=thumbnail,
                    description=description,
                    # gender = hero_stats['gender'],
                    # race = hero_stats['race'],
                    # height = hero_stats['height'],
                    # weight = hero_stats['weight'],
                    # alighnment = hero_stats['alighnment']
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

            
                # loop += 1
                # offset += 100
                # limit += 100
            # characters, created = 
            # for category in map(str, category):
            #     category = category_query(category)
            #     category, created = Category.objects.get_or_create(
            #         title=category)
            #     book.category.add(category)
            
