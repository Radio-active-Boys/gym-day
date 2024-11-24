# Generated by Django 5.1.3 on 2024-11-24 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('trainer_id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('specialty', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerSchedule',
            fields=[
                ('schedule_id', models.CharField(editable=False, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('date', models.DateField()),
                ('is_leave', models.BooleanField(default=False)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='workout.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('workout_plan_id', models.CharField(editable=False, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout_plans', to='membership.member')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workout_plans', to='workout.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('workout_id', models.CharField(editable=False, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('reps', models.PositiveIntegerField()),
                ('duration', models.PositiveIntegerField()),
                ('rest_period', models.PositiveIntegerField()),
                ('workout_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='workout.workoutplan')),
            ],
        ),
    ]
