# Generated by Django 4.1.1 on 2022-11-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refeitorio', '0004_alter_falta_aluno_faltante'),
    ]

    operations = [
        migrations.AddField(
            model_name='falta',
            name='justificativa',
            field=models.TextField(blank=True, null=True),
        ),
    ]
