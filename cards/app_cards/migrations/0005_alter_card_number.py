# Generated by Django 4.0.6 on 2022-07-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cards', '0004_alter_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.CharField(max_length=16, verbose_name='Номер картки'),
        ),
    ]
