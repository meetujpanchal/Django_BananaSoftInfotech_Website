# Generated by Django 4.0.4 on 2022-06-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_banana', '0002_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='slider_image',
            field=models.FileField(blank=True, null=True, upload_to='slid_imgs'),
        ),
    ]
