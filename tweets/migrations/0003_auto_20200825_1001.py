# Generated by Django 3.1 on 2020-08-25 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20200825_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet_id',
            field=models.TextField(blank=True, null=True),
        ),
    ]
