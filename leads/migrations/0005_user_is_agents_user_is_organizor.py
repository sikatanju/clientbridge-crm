# Generated by Django 4.2.16 on 2024-11-09 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agents',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_organizor',
            field=models.BooleanField(default=True),
        ),
    ]
