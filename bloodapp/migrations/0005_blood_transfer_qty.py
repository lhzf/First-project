# Generated by Django 4.2.5 on 2023-10-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0004_bloodtype_donation_center_blood_transfer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood_transfer',
            name='qty',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
