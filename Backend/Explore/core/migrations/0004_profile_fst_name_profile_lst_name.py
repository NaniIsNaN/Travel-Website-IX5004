# Generated by Django 4.0.5 on 2022-07-21 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fst_name',
            field=models.CharField(default='mAaLol', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='lst_name',
            field=models.CharField(default='MINAUNGHLAING', max_length=100),
        ),
    ]
