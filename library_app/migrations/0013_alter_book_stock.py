# Generated by Django 4.0.1 on 2022-02-12 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0012_alter_book_stock_alter_checkoutitem_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
