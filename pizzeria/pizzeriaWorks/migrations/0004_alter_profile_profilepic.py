# Generated by Django 4.0.2 on 2023-05-14 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeriaWorks', '0003_alter_profile_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение профиля'),
        ),
    ]
