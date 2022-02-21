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

        url = f'https://gateway.marvel.com:443/v1/public/comics?format=comic&formatType=comic&dateRange=2018-01-01%2C2020-12-25&limit=100&ts={ts}&apikey={pub_key}&hash={hasht}'
        
        index = 0
        response = requests.get(url)
        print(response)
        comics = response.json().get('data').get('results')
        # print(comics)
        

        for comic in comics:
        
            title = comics[index]['title']
            image_url = comics[index]['thumbnail']['path']+'/detail.jpg'
            description = comics[index]['textObjects']
            page_count = comics[index]['pageCount']
            issue_number = comics[index]['issueNumber']
            date = comics[index]['dates'][0]['date'].split('T')[0]
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
                date = date
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
            
