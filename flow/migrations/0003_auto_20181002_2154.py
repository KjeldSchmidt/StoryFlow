# Generated by Django 2.1.1 on 2018-10-02 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0002_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
