# Generated by Django 2.1.7 on 2019-03-26 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
        ('module', '0002_auto_20190321_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='resource',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.Resource'),
        ),
    ]
