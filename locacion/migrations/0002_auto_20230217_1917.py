# Generated by Django 2.2 on 2023-02-17 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrio',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='calle',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]