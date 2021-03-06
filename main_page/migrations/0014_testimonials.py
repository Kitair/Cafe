# Generated by Django 3.2.4 on 2021-07-12 00:14

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0013_auto_20210712_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('role', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=main_page.models.Testimonials.get_file_name)),
                ('is_visible', models.BooleanField(default=True)),
                ('quote', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
