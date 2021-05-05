# Generated by Django 3.0.2 on 2021-05-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covercall', '0014_auto_20210501_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackTestCover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enddateBt', models.DateField()),
                ('timerange', models.FloatField(null=True)),
                ('rate', models.FloatField(null=True)),
                ('strikePrice', models.FloatField(null=True)),
                ('symbol', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='BackTestCovered',
        ),
    ]
