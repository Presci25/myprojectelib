# Generated by Django 5.1.4 on 2024-12-18 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_booksubjects_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcategory',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
