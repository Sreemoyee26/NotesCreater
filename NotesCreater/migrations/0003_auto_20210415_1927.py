# Generated by Django 3.1.7 on 2021-04-15 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NotesCreater', '0002_auto_20210415_1845'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='note',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
    ]
