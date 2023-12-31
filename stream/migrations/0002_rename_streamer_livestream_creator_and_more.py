# Generated by Django 4.2.7 on 2023-12-12 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livestream',
            old_name='streamer',
            new_name='creator',
        ),
        migrations.RemoveField(
            model_name='livestream',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='livestream',
            name='stream_key',
        ),
        migrations.AddField(
            model_name='livestream',
            name='video',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stream.video'),
        ),
    ]
