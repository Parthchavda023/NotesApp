# Generated by Django 5.0 on 2024-02-14 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('M_Appp', '0002_notesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbachModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctrated', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=51)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=108)),
                ('msg', models.TextField()),
            ],
        ),
    ]
