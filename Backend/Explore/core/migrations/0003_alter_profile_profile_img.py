# Generated by Django 4.0.5 on 2022-07-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='default.png', upload_to='profile_images'),
        ),
    ]
