# Generated by Django 3.1.5 on 2021-02-25 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210225_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportarpostagem',
            name='contact_phone',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
