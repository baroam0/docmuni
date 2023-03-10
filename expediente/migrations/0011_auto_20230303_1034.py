# Generated by Django 3.2 on 2023-03-03 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0010_auto_20230303_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='decretoadjudicacion',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='obra',
            name='numeroprocedimiento',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montocertificado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.obra')),
            ],
            options={
                'verbose_name_plural': 'Certificado',
            },
        ),
    ]
