# Generated by Django 2.1 on 2018-09-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0053_auto_20180920_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='icon',
            field=models.IntegerField(blank=True, null=True, verbose_name='Car Image Icon'),
        ),
    ]