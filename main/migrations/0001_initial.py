# Generated by Django 3.2.6 on 2021-08-14 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Girlfriend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('number', models.CharField(max_length=12)),
                ('age', models.CharField(max_length=2)),
            ],
        ),
    ]
