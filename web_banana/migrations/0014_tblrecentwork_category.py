# Generated by Django 4.0.4 on 2022-06-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_banana', '0013_tblrecentwork_delete_portfol'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblrecentwork',
            name='category',
            field=models.CharField(default='enter caegory', max_length=100),
        ),
    ]
