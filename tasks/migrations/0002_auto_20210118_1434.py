# Generated by Django 3.1.5 on 2021-01-18 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dotask',
            options={'ordering': ['completaed', 'data']},
        ),
    ]
