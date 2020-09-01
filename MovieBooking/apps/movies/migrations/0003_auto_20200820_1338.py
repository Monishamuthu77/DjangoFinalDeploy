# Generated by Django 3.0.9 on 2020-08-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200816_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='desc',
            field=models.TextField(default='A very good movie', max_length=300),
        ),
        migrations.AddField(
            model_name='listing',
            name='teaser',
            field=models.URLField(default='URL'),
        ),
    ]
