# Generated by Django 4.1.7 on 2023-03-02 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='desription',
            new_name='description',
        ),
    ]
