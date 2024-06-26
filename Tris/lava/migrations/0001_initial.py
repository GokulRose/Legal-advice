# Generated by Django 5.0.3 on 2024-03-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('DOB', models.DateField()),
                ('language', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('mobile', models.IntegerField()),
                ('Education', models.CharField(choices=[('S', 'School'), ('C', 'College')], max_length=1)),
                ('pan', models.BooleanField()),
                ('d_license', models.BooleanField()),
                ('passport', models.BooleanField()),
                ('voter', models.BooleanField()),
            ],
            options={
                'db_table': 'info',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
