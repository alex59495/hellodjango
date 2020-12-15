# Generated by Django 3.1.4 on 2020-12-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydevices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='form_factor',
            field=models.CharField(choices=[('phone', 'Phone'), ('tablet', 'Tablet')], default='phone', max_length=6),
        ),
        migrations.AlterField(
            model_name='device',
            name='os',
            field=models.CharField(choices=[('ios', 'iOS'), ('android', 'Android')], default='android', max_length=7),
        ),
    ]