# Generated by Django 4.2.7 on 2023-11-25 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicians',
            name='gender',
            field=models.CharField(max_length=50),
        ),
    ]
