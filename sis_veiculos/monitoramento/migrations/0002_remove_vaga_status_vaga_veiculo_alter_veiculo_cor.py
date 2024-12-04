# Generated by Django 5.1.3 on 2024-12-03 23:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoramento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaga',
            name='status',
        ),
        migrations.AddField(
            model_name='vaga',
            name='veiculo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='monitoramento.veiculo'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='cor',
            field=models.CharField(max_length=20),
        ),
    ]
