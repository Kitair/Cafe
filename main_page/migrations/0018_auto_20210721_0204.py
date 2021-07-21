# Generated by Django 3.2.4 on 2021-07-20 23:04

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0017_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('desc', models.CharField(max_length=500, unique=True)),
                ('media_url', models.ImageField(upload_to=main_page.models.Hero.get_file_name)),
            ],
        ),
        migrations.AddField(
            model_name='about',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
