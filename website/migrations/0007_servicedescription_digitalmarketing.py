# Generated by Django 4.1.1 on 2022-09-25 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_rename_servicedes_servicedescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedescription',
            name='DigitalMarketing',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
