# Generated by Django 4.2.6 on 2023-10-07 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_log_location_alter_log_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('tags', models.CharField(default='', max_length=100)),
                ('link', models.CharField(default='', max_length=100)),
            ],
        ),
    ]