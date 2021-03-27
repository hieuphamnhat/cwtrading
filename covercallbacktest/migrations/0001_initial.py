# Generated by Django 3.1.7 on 2021-03-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoverCallBacktest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('volatility', models.FloatField(null=True)),
                ('callPrice', models.FloatField(null=True)),
                ('strikePrice', models.FloatField(null=True)),
            ],
        ),
    ]