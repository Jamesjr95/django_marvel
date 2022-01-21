# **Project Overview**
 - keep a record of all the books in the library books issued/returned by students and calculate fines.
 - manage the information related to the library members, students, books, addresses.
 - I will use django and try to implement vue also.
 - For now the only library that I will use is [django-haystack](https://github.com/django-haystack/django-haystack) which will help with spelling suggestions for user search queries. 



# **Functionality**
 The user will first see a catalog of the libraries books in different fields categorized by genre or popularity with a navbar that has links to various parts of the site (sign up, log in, account, book categories, etc.) and a [search bar](https://getbootstrap.com/docs/5.1/forms/input-group/#buttons-with-dropdowns) with a dropdown to filter the search. The user will have to register, or login if already registered. After user is registered they will be redirected to the catalog page. If the user clicks on a book they will be redirected to a page with the books details and I want the user to have the option to checkout or purchase a book (if not already checked out or out of stock) and be able to see other users reviews as well. I want a profile page for the logged in user and for it to show their history as well as an avatar for the user (if selected or a default one if not), like/dislike and comment on a book they've checkout out, list of their current books that are checked out, the due dates for those books and books that are overdue with fines. If the user has an overdue book they will be blocked from checking out until the fine is paid. 


# **Data Model**

![Diagram of models](https://github.com/Jamesjr95/Capstone_proj/blob/main/image.png)

## User table
- avatar,
- phone number,
- address

## Category table
- title

## Book table
- title,
- price,
- description,
- image,
- rating,
- stock, 
- likes,
  - many to many relationship to the User table
- categories
  - many to many relationship with Category table

## Author table
- name,
- books
  - many to many relationship with Book table

## Checkout Item table
- checkout,
  - foreignkey relationship to Checkout table
- book
  - foreignkey to Book table

## Checkout table
- owner,
  - one to one relationship to User table
- books,
  - many to many relationship with Book table

#  **Schedule**
- Milestone 1(1st week)
  - Focus on and complete the database for the user model and the library models.
  - Find a library api to pull book data from.
- Milestone 2(2nd week)
  - Start thinking about my views and the general layout of the site.
  - Create templates and CRUD to render all the data.
- Milestone 3(3rd & 4th week)
  - add a way to purchase and checkout book
  - add user avatar
  - Enhance the ux on the site by adding better styling and a system of liking and commenting on books.
- Milestone 4(after course)
  - Think of and implement even more complicated database relationships and continue improving ux with styling and js/vue.
