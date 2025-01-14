# Generated by Django 5.1.3 on 2024-11-24 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('purchase_date', models.DateField()),
                ('condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('maintenance_id', models.CharField(blank=True, max_length=12, primary_key=True, serialize=False)),
                ('due_date', models.DateField()),
                ('next_date', models.DateField()),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.equipment')),
            ],
        ),
    ]
