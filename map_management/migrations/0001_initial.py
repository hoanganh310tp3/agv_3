# Generated by Django 5.0.3 on 2024-10-22 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='station_data',
            fields=[
                ('station_id', models.IntegerField(primary_key=True, serialize=False)),
                ('station_node', models.IntegerField(default=0)),
                ('station_type', models.CharField(blank=True, choices=[('HOME', 'Parking station'), ('BAT', 'Charging station'), ('PICK', 'Pick up'), ('DROP', 'Drop')], max_length=64)),
                ('load_transfer', models.CharField(blank=True, choices=[('AUTO', 'Automatic'), ('MAN', 'Manual')], max_length=64)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
