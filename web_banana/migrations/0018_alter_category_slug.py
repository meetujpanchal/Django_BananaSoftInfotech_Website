# Generated by Django 4.0.4 on 2022-07-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_banana', '0017_category_story'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
