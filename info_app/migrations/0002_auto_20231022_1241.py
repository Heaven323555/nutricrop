# Generated by Django 3.0.14 on 2023-10-22 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infomodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
