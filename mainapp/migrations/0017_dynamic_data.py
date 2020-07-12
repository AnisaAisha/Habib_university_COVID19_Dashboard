# Generated by Django 2.2.7 on 2020-07-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20200621_0429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dynamic_Data',
            fields=[
                ('entry_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('province', models.CharField(choices=[('Sindh', 'Sindh'), ('Punjab', 'Punjab'), ('KP', 'KP'), ('KPTD', 'KPTD'), ('GB', 'GB'), ('AJK', 'AJK'), ('ICT', 'ICT'), ('Taftan_mobile_lab', 'Taftan_mobile_lab'), ('Balochistan', 'Balochistan')], max_length=20)),
                ('confirmed_cases', models.IntegerField(default=0)),
                ('active_cases', models.IntegerField(default=0)),
                ('deaths', models.IntegerField(default=0)),
                ('recoveries', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Daily Cases',
                'verbose_name_plural': 'Daily Cases',
                'unique_together': {('date', 'province')},
            },
        ),
    ]
