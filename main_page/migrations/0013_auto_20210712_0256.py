# Generated by Django 3.2.4 on 2021-07-11 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0012_auto_20210712_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='chefs',
            name='instagram_url',
            field=models.URLField(default='add instagram url'),
        ),
        migrations.AddField(
            model_name='chefs',
            name='linkedin_url',
            field=models.URLField(default='add linkedin url'),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='facebook_url',
            field=models.URLField(default='add facebook url'),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='twitter_url',
            field=models.URLField(default='add twitter url'),
        ),
    ]