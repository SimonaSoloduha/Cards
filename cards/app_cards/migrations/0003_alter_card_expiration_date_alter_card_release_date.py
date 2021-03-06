# Generated by Django 4.0.6 on 2022-07-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cards', '0002_alter_card_activity_flag_alter_card_sum_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expiration_date',
            field=models.DateTimeField(verbose_name='Дата закінчення активності картки'),
        ),
        migrations.AlterField(
            model_name='card',
            name='release_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата випуску картки'),
        ),
    ]
