# Generated by Django 3.1 on 2020-08-27 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tweet_important'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='media',
        ),
    ]
