# Generated by Django 2.1.3 on 2018-11-09 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_machine_modified_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=100)),
                ('api_address', models.CharField(max_length=100)),
            ],
        ),
    ]
