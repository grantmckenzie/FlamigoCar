# Generated by Django 2.1 on 2018-09-12 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20180913_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='id',
        ),
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='car_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Car'),
        ),
        migrations.AddField(
            model_name='booking',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]