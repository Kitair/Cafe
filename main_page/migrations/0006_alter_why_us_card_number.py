# Generated by Django 3.2.4 on 2021-07-11 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_why_us_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='why_us',
            name='card_number',
            field=models.CharField(max_length=2, unique=True),
        ),
    ]
