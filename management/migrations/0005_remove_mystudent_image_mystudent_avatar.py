# Generated by Django 5.0 on 2023-12-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_mystudent_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mystudent',
            name='image',
        ),
        migrations.AddField(
            model_name='mystudent',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]