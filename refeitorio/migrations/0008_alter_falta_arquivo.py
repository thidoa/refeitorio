# Generated by Django 4.1.1 on 2022-11-23 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refeitorio', '0007_alter_falta_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='falta',
            name='arquivo',
            field=models.FileField(blank=True, default='null', upload_to='uploads/'),
        ),
    ]
