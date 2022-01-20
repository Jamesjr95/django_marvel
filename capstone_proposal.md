# **Project Overview**
## - keep a record of all the books in the library books issued/returned by students and calculate fines.
## - manage the information related to the library members, students, books, addresses.
## - I will use django and try to implement vue also.
## - For now the only library that I will use is [django-haystack](https://github.com/django-haystack/django-haystack) which will help with spelling suggestions for user search queries. 



# **Functionality**
## The user will first see a catalog of the libraries books in different fields categorized by genre or popularity with a navbar that has links to various parts of the site (sign up, log in, account, book categories, etc.) and a [search bar](https://getbootstrap.com/docs/5.1/forms/input-group/#buttons-with-dropdowns) with a dropdown to filter the search. The user will have to register, or login if already registered. After user is registered they will be redirected to the catalog page. If the user clicks on a book they will be redirected to a page with the books details and I want the user to have the option to checkout or purchase a book (if not already checked out or out of stock) and be able to see other users reviews as well. I want an a profile page for the logged in user and for it to show their history as well as an avatar for the user (if selected or a default one if not), like/dislike and comment on a book they've checkout out, list of their current books that are checked out, the due dates for those books and books that are overdue with fines. If the user has an overdue book they will be blocked from checking out until the fine is paid. 


# **Data Model**
```
def get_upload_path(instance, filename):
    return f'images/avatars/{filename}'

class User(AbstractUser):
    avatar = models.ImageField(upload_to=get_upload_path, default='images/avatars/default_avatar.jpg')
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=300)

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0)
    stock = models.PositiveIntegerField(default=random.randint(10,20))
    likes = models.ManyToManyField(get_user_model(), related_name='users', blank=True)

    categories = models.ManyToManyField(Category, related_name='books')

    def __str__(self):
        return f"{self.title}"

class Author(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='authors')



class CheckoutItem(models.Model):
    checkout = models.ForeignKey('Checkout', on_delete=models.CASCADE, related_name='checkout_items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='checkout_items')
    quantity = models.PositiveIntegerField(default=0)



class Checkout(models.Model):
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='checkout')
    books = models.ManyToManyField(Book, through=CheckoutItem, related_name='user_checkout', blank=True)

    def __str__(self):
        return f"{self.owner}"
```

#  **Schedule**
- Milestone 1(1st week)
  - Focus on and complete the database for the user model and the library models.
  - Find a library api to pull book data from.
- Milestone 2(2nd week)
  - Start thinking about my views and the general layout of the site.
  - Create very barebones templates to render all the data.
- Milestone 3(3rd & 4th week)
  - add a way to purchase and checkout book
  - add user avatar
  - Enhance the ux on the site by adding better styling and a system of liking and commenting on books.
- Milestone 4(after course)
  - Think of and implement even more complicated database relationships and continue improving ux with styling and js/vue.
