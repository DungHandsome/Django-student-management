# Generated by Django 5.0 on 2023-12-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_remove_announcement_student_mystudent_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystudent',
            name='student',
            field=models.BooleanField(default=False, null=True),
        ),
    ]