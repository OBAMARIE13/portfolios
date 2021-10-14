# Generated by Django 3.2.7 on 2021-10-14 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('christelle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fonction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('niveau', models.CharField(max_length=50)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Fonction',
                'verbose_name_plural': 'Fonctions',
            },
        ),
        migrations.RemoveField(
            model_name='about',
            name='profession',
        ),
        migrations.AddField(
            model_name='about',
            name='fonction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fonction_about', to='christelle.fonction'),
            preserve_default=False,
        ),
    ]
