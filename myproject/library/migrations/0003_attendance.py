# Generated by Django 5.1.4 on 2024-12-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_users_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100, null=True)),
                ('uname', models.CharField(max_length=60, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('in_time', models.TimeField(blank=True, null=True)),
                ('out_time', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
