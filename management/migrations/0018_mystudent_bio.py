# Generated by Django 5.0 on 2024-02-08 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0017_alter_mystudent_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='mystudent',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
