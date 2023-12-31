# Generated by Django 4.1.5 on 2023-06-20 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('contact_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contents', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('information_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('contents', models.TextField()),
                ('time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('people', models.IntegerField()),
                ('price', models.IntegerField()),
                ('filename', models.CharField(max_length=100)),
                ('contents', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sightseeing',
            fields=[
                ('sightseeing_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contents', models.TextField()),
                ('filename', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone_num', models.IntegerField(null=True)),
                ('birth', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('reserve_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stay_people', models.IntegerField()),
                ('check_in', models.DateField()),
                ('chack_out', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fukumitsu.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fukumitsu.user')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('family_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('relationship', models.CharField(max_length=100, null=True)),
                ('birth', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fukumitsu.user')),
            ],
        ),
    ]
