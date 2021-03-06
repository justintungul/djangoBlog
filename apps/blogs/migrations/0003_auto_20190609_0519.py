# Generated by Django 2.1.8 on 2019-06-09 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_user_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hero_image',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to='blogs.User'),
        ),
    ]
