# Generated by Django 4.1.1 on 2022-09-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infocounter',
            name='clients',
            field=models.CharField(max_length=50),
        ),
    ]
