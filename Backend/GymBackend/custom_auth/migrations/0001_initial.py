# Generated by Django 5.1.3 on 2024-11-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordResetRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('member', 'Member'), ('trainer', 'Trainer')], max_length=20)),
                ('new_password', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('member', 'Member'), ('trainer', 'Trainer')], max_length=20)),
                ('hashed_password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('member', 'Member'), ('trainer', 'Trainer')], max_length=20)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
