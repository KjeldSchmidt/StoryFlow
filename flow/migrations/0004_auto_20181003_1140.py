# Generated by Django 2.1.1 on 2018-10-03 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0003_auto_20181002_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='first_text',
        ),
        migrations.AddField(
            model_name='game',
            name='first_story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='flow.Story'),
        ),
    ]
