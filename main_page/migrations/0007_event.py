# Generated by Django 3.2.4 on 2021-07-11 22:52

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_alter_why_us_card_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('desc', models.CharField(max_length=500, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('photo', models.ImageField(upload_to=main_page.models.Event.get_file_name)),
            ],
        ),
    ]
