# Generated by Django 2.1.1 on 2018-10-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0005_auto_20181015_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='editor_panel_x',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='editor_panel_y',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
    ]
