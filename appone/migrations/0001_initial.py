# Generated by Django 3.1.4 on 2020-12-16 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your in-game name', max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('birth_date', models.DateField()),
                ('character_class', models.CharField(choices=[('human', 'Human'), ('hobbit', 'Hobbit'), ('elf', 'Elf'), ('orc', 'Orc')], max_length=20)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.region')),
            ],
        ),
    ]
