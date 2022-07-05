# Generated by Django 4.0.4 on 2022-07-02 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_banana', '0020_category_story'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='body',
        ),
        migrations.RemoveField(
            model_name='story',
            name='des',
        ),
        migrations.AddField(
            model_name='story',
            name='description',
            field=models.TextField(default='hello', help_text='enter product description', max_length=100),
        ),
        migrations.AddField(
            model_name='story',
            name='navigatelink',
            field=models.CharField(default='hello', help_text='enter product navigate link', max_length=100),
        ),
        migrations.AddField(
            model_name='story',
            name='portfol_img',
            field=models.FileField(default='hh', upload_to='portfolio/'),
        ),
    ]
