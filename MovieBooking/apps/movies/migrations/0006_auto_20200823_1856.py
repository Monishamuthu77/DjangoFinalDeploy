# Generated by Django 3.0.9 on 2020-08-23 13:26

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20200823_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='teaser',
        ),
        migrations.AddField(
            model_name='listing',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]
