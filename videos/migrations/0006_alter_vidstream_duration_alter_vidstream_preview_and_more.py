# Generated by Django 4.2.7 on 2023-12-08 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_remove_comment_comment_remove_like_liked_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vidstream',
            name='duration',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vidstream',
            name='preview',
            field=models.FileField(blank=True, default='', null=True, upload_to='preview'),
        ),
        migrations.AlterField(
            model_name='vidstream',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vidstream',
            name='views',
            field=models.PositiveBigIntegerField(blank=True, default=0),
        ),
    ]
