# Generated by Django 4.2 on 2023-05-17 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeriaWorks', '0004_alter_profile_profilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='isAlive',
            field=models.BooleanField(default=True),
        ),
    ]
