# Generated by Django 4.2.5 on 2023-11-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0005_blood_transfer_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='donor_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
