# Generated by Django 4.0.6 on 2022-07-13 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(blank=True, max_length=100, verbose_name='Серія картки')),
                ('number', models.CharField(blank=True, max_length=16, verbose_name='Номер картки')),
                ('release_date', models.DateField(auto_now_add=True, verbose_name='Дата випуску картки')),
                ('expiration_date', models.DateField(verbose_name='Дата закінчення активності картки')),
                ('cvv', models.CharField(blank=True, max_length=16, verbose_name='CVV')),
                ('sum_card', models.FloatField(blank=True, null=True)),
                ('activity_flag', models.CharField(blank=True, choices=[('Active', 'Активована'), ('NotActive', 'Не активована'), ('Stitched', 'Прострочена')], default='NotActive', max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Карта',
            },
        ),
    ]