# Generated by Django 3.2.7 on 2021-10-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christelle', '0005_rename_nom_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolios',
            name='lien',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]