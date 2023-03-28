## <p align='center'>Django Marvel</p>

![image](https://user-images.githubusercontent.com/92341570/228389137-d2f9e786-349b-40c2-895d-cb9aa2a95bf6.png)

### Technologies used

* Django 4.0.
* Bootstrap v5.1

## Features:
* User sign up
* User log out

* Checkout a comic book
* Like a comic book
* Gallery of all comic books
* Gallery of all characters
* Detail pages for comic books
* Detail pages for characters

## Data Model:
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

## Built with:

* Django 4.0.
* Bootstrap v5.1

## Todos:
1. ~~add ability to sort comics/characters~~
3. ~~add option to delete cart items~~
4. ~~add option to increment the count of cart items~~
5. ~~add overdue book message~~
6. ~~add ability to like comics~~
7. ~~add ability to like comics~~
8. ~~add paginations~~
