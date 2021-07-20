# Generated by Django 3.2.4 on 2021-07-13 16:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0014_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Phone in format xxx xxx xxxx', regex='^(\\d{3}[- .]?){2}\\d{4}$')])),
                ('user_date', models.DateField(auto_now=True)),
                ('user_time', models.DateTimeField(auto_now=True)),
                ('number_of_person', models.PositiveIntegerField()),
                ('user_message', models.CharField(max_length=300)),
                ('is_processed', models.BooleanField(default=False)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
