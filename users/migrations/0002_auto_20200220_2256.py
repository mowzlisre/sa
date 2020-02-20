# Generated by Django 3.0.3 on 2020-02-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_of_joining',
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year'), ('Completed', 'Completed')], max_length=30),
        ),
    ]
