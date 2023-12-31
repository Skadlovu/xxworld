# Generated by Django 4.2.7 on 2023-12-04 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=600)),
                ('upload_date', models.TimeField(auto_now_add=True)),
                ('content', models.ImageField(upload_to='', verbose_name='photos')),
                ('views', models.IntegerField(blank=True, default=0)),
                ('likes', models.IntegerField(blank=True, default=0)),
                ('dislikes', models.IntegerField(blank=True, default=0)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
