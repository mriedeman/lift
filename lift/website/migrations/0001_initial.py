# Generated by Django 3.2.8 on 2021-10-17 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pipe_length', models.DecimalField(decimal_places=2, max_digits=8)),
                ('material', models.CharField(choices=[(130, 'Acrylonite Butadiene Styrene'), (190, 'Aluminum'), (140, 'Asbestos Cement')], default='Aluminum', max_length=100)),
                ('inner_diameter', models.DecimalField(decimal_places=2, max_digits=8)),
                ('outlet_type', models.CharField(choices=[('suc', 'suction'), ('dis', 'discharge')], default='dis', max_length=100)),
            ],
        ),
    ]