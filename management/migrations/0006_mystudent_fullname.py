# Generated by Django 5.0 on 2023-12-07 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_remove_mystudent_image_mystudent_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='mystudent',
            name='fullname',
            field=models.CharField(max_length=500, null=True),
        ),
    ]