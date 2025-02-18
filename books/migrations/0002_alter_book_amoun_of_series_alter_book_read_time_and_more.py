# Generated by Django 5.1.3 on 2024-11-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='amoun_of_series',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='read_time',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
