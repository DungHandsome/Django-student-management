# Generated by Django 5.0 on 2023-12-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_remove_assignment_assignment_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=1000)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='class_note',
            field=models.TextField(null=True),
        ),
    ]