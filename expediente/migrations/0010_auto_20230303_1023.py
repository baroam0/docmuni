# Generated by Django 3.2 on 2023-03-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0009_alter_expediente_nomenclatura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='descripcion',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='nomenclatura',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]