# Generated by Django 4.0.5 on 2022-08-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to='content'),
        ),
    ]