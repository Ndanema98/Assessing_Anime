# Generated by Django 3.2.18 on 2023-03-15 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230313_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]
