# Generated by Django 3.2 on 2023-02-16 22:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0002_auto_20230216_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]