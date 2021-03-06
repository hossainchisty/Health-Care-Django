# Generated by Django 3.2.4 on 2021-06-10 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('speciality', models.CharField(max_length=120)),
                ('picture', models.ImageField(upload_to='doctors/')),
                ('experience', models.TextField()),
                ('twitter', models.CharField(blank=True, max_length=120, null=True)),
                ('facebook', models.CharField(blank=True, max_length=120, null=True)),
                ('instagram', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='feedback/')),
            ],
        ),
    ]
