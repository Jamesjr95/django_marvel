# Generated by Django 4.0.1 on 2022-02-21 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0021_remove_book_category_book_date_alter_book_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
