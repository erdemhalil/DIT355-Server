# Generated by Django 3.2.9 on 2021-12-02 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentists', '0003_alter_openinghours_timestaken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openinghours',
            name='friday',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='monday',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='thursday',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='tuesday',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='wednesday',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]