# Generated by Django 2.2.2 on 2019-06-17 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190617_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='location',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
