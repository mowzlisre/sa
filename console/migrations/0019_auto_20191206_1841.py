# Generated by Django 2.2 on 2019-12-06 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0018_semassign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semassign',
            name='semester',
            field=models.ManyToManyField(to='console.Subject'),
        ),
    ]
