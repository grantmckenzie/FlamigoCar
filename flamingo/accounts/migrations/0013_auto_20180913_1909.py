# Generated by Django 2.1 on 2018-09-13 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20180913_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='book_end_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='book_start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]