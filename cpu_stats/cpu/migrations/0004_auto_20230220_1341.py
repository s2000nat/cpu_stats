# Generated by Django 3.1.4 on 2023-02-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpu', '0003_auto_20230220_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='cpu_load',
            field=models.FloatField(),
        ),
    ]
