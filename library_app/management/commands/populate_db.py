from django.core.management.base import BaseCommand
import requests

from library_app.models import Book, Category, Author

class Command(BaseCommand):
    def handle(self, *args, **kwargs):


        url = "https://gnikdroy.pythonanywhere.com/api/book/?format=json"
        response = requests.get(url)
        # print this to see whole dictionary with all fields
        books = response.json() 
        
        # url2 = f"https://en.wikipedia.org/api/rest_v1/page/summary/Frankenstein"
        # url2 = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
        # response2 = requests.get(url2)
        # summary = response2.json().get('extract')
        # print(summary)
        
        
        def query(title):
            if '; ' in title:
                summary = title.split('; ')[0]
                url2 = f"https://en.wikipedia.org/api/rest_v1/page/summary/{summary}"
                response2 = requests.get(url2)
                summary = response2.json().get('extract')
                print(summary)
            else:
                summary = title.replace(' ', '_')
                url2 = f"https://en.wikipedia.org/api/rest_v1/page/summary/{summary}"
                response2 = requests.get(url2)
                summary = response2.json().get('extract')
                print(summary)
            return summary
        
        
        
        books = books['results']
        # search = books['title']
        
        for book in books[0:5]:
            title = book['title']
            image_url = book['resources'][2]['uri']
            categories = book['subjects']
            description = query(title)
        print(description)
        