# Generated by Django 5.0.1 on 2024-02-07 05:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RobotCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('currency', models.CharField(choices=[('INR', 'Indian Rupee'), ('USD', 'US Dollar'), ('EUR', 'Euro')], default='INR', max_length=3)),
                ('price', models.IntegerField()),
                ('manufacturing_date', models.DateTimeField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='robots', to='robots.manufacturer')),
                ('robot_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='robots', to='robots.robotcategory')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]