# Generated by Django 3.2 on 2024-08-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20240731_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiate_ai_model',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
