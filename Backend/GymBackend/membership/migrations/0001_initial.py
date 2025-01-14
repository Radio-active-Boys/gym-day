# Generated by Django 5.1.3 on 2024-11-24 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.CharField(blank=True, max_length=15, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_joining', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipType',
            fields=[
                ('membership_type_id', models.CharField(blank=True, max_length=15, primary_key=True, serialize=False)),
                ('duration', models.PositiveIntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendance_id', models.CharField(blank=True, max_length=25, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('check_in_time', models.TimeField()),
                ('check_out_time', models.TimeField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.member')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='membership_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='membership.membershiptype'),
        ),
    ]
