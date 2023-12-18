# Generated by Django 4.2.7 on 2023-12-06 15:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_alter_vidstream_duration_alter_vidstream_preview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='like',
            name='liked',
        ),
        migrations.AddField(
            model_name='vidstream',
            name='timestamp',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
