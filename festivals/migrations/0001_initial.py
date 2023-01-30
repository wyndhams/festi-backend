# Generated by Django 4.1.5 on 2023-01-24 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0001_initial'),
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cover_image', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=30)),
                ('capacity', models.CharField(max_length=30)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='festivals', to='artists.artist')),
                ('genres', models.ManyToManyField(blank=True, related_name='festivals', to='genres.genre')),
            ],
        ),
    ]
