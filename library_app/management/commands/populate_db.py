from django.core.management.base import BaseCommand
import requests, json

'''make for loop for 'agents' which are the authors because there can be multiple authors'''

from library_app.models import Book, Category, Author

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        Book.objects.all().delete()
        Category.objects.all().delete()
        Author.objects.all().delete()
        
        
        def query(title):
            if '; ' in title:
                summary = title.split('; ')[0]
                # print(summary)
                url2 = f"https://en.wikipedia.org/api/rest_v1/page/summary/{summary}"
                response2 = requests.get(url2)
                summary = response2.json().get('extract')
                if summary == None:
                    summary = 'No description available'
            elif ' ' or ',' or '-' in title:
                summary = title.replace(' ', '_').replace(',', '').replace('-', '')
                # print(summary)
                url2 = f"https://en.wikipedia.org/api/rest_v1/page/summary/{summary}"
                response2 = requests.get(url2)
                summary = response2.json().get('extract')
                if summary == None:
                    summary = 'No description available'
            return summary

        def category_query(category):
            if '--' in category:
                category = category.replace('--', '')
            else:
                category = category
            return category
        
        
        def image_search(image_url):
            for data in image_url:
                if '.cover.medium.jpg' in data['uri']:
                    image_url = data['uri']
            return image_url

        def author_search(author):
            index = 0
            if author[0]['type'] == 'Author':
                author = author[0]['person']
            index += 1
            return author
        loop = 1
        
        while loop < 2:
            loop_str = str(loop)
            url = f"https://gnikdroy.pythonanywhere.com/api/book/?format=json&page={loop_str}"
            response = requests.get(url)
            books = response.json().get('results')
            
            
            for book in books:
                title = book['title']
                image_url = book['resources']
                image_url = image_search(image_url)
                category = book['subjects']
                description = query(title)
                author = book['agents']
                author = author_search(author)
                print(author)
                

                
                book = Book.objects.create(
                    title = title,
                    image_url = image_url,
                    description = description,
                    
                )

                author, created = Author.objects.get_or_create(name=author)
                author.books.add(book)
                
                for category in map(str, category):
                    category = category_query(category)
                    category, created = Category.objects.get_or_create(title=category)
                    book.category.add(category)
            loop += 1