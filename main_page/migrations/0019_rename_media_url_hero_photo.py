# Generated by Django 3.2.4 on 2021-07-20 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0018_auto_20210721_0204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hero',
            old_name='media_url',
            new_name='photo',
        ),
    ]