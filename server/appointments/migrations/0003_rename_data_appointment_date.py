# Generated by Django 3.2.9 on 2021-12-02 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20211201_1002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='data',
            new_name='date',
        ),
    ]