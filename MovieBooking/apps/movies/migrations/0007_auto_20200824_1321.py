# Generated by Django 3.0.9 on 2020-08-24 07:51

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20200823_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingTickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('gold_seats', models.IntegerField()),
                ('silver_seats', models.IntegerField()),
                ('show_time', models.CharField(choices=[('10AM-1PM', 'Morning'), ('2PM-5PM', 'Afternoon'), ('7PM-10PM', 'Evening'), ('11PM-3AM', 'Night')], max_length=30)),
                ('booking_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='listing',
            name='video',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]