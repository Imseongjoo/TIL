# Generated by Django 3.2.18 on 2023-03-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.CharField(default='일반', max_length=20),
        ),
    ]
