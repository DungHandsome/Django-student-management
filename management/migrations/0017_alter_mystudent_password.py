# Generated by Django 5.0 on 2024-01-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0016_alter_mystudent_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystudent',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
