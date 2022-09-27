# ClimbUp

Repo for PDX Code guild captstone

## Overview
------

Django Marvel is an app where you can view, checkout & like various Marvel comic books.

### Technologies used

* Django 4.0.
* Bootstrap v5.1

## Features
------

- User System
  - [x] User sign up form
  - [x] User log out
  - [ ] Update profile
  - [ ] Delete Profile
  - [ ] Add User avatar
- Books
  - [x] Checkout a book
  - [x] Like a book
  - [ ] Add a book
  - [ ] Comment on a book
  - [x] Gallery of all books
  - [x] Gallery of all characters
  - [x] Detail pages for book
  - [x] Detail pages for characters

## Data Model
----
* City
  * name (charfield)
* Book
  * title (charfield)
  * price (Decimalfield)
  * description (CharField)
  * image_url (CharField)
  * stock (PositiveIntegerField)
  * likes (ManyToMany to User)
  * page_count (PositiveIntegerField)
  * issue_number (PositiveIntegerField)
  * date (DateField)
* Character
  * name (charfield)
  * description (charfield)
  * image (charfield)
  * books (ManyToManyFiled to Book)
  * gender (CharField)
  * race (CharField)
  * height (CharField)
  * weight (CharField)
  * alignment (CharField)
* Author
  * role (CharField)
  * name (CharField)
  * books (ManyTOManyField to Book)
* Checkout
  * owner (OneToOneField to User)
  * books (ManyToManyField to Book)
* CheckoutItem
  * checkout (ForeignKey to Checkout)
  * book (ForeignKey to Book)
  * quantity (PositiveInterField)
  * due_date (DateField)

## Pages
-------
- Index
  - list of comics
  - header
    - link to profile page
    - log-in link if not logged in
    - log-out link if logged in
    - link to characters
    - search bar to search for comic by name
- Comic Book Detail
  - like book
  - add book to cart
- Character Detail
  - view list of associated comics
  - bio of character
- Registration
  - user registration form using django forms
- Login
  - login form
  - redirect to users cart on login
- Cart page
  - display users cart items
  - user can change quantity of books and delete from cart
  - total price & price of each individual book
## Schedule
----
* Week 1
    * ~~create models for Book~~
    * ~~create models for Checkout~~
    * ~~create models for CheckoutItem~~
    * ~~create models for Users~~
    * ~~create index template and view~~
    * ~~show test books in page~~
    * ~~add forms login & signup~~
    * ~~add user checkout page with users cart items~~
* Week 2
    * find and api with more data for each character
    * add ability to sort comics/characters
    * ~~add option to delete cart items~~
    * ~~add option to increment the count of cart items~~
    * ~~add overdue book message~~
    * ~~add ability to like comics~~
    
* Week 3
    * ~~add ability to like comics~~
    * finish any styling on app
