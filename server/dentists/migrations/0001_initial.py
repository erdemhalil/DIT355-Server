# Generated by Django 3.2.9 on 2022-01-06 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(blank=True)),
                ('latitude', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Openinghours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.CharField(blank=True, max_length=150)),
                ('tuesday', models.CharField(blank=True, max_length=150)),
                ('wednesday', models.CharField(blank=True, max_length=150)),
                ('thursday', models.CharField(blank=True, max_length=150)),
                ('friday', models.CharField(blank=True, max_length=150)),
                ('timestaken', models.CharField(blank=True, default=None, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dentist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('owner', models.CharField(max_length=150)),
                ('dentists', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('coordinate', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dentists.coordinate')),
                ('openinghours', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dentists.openinghours')),
            ],
        ),
    ]
