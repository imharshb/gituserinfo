# Generated by Django 2.2.2 on 2019-06-20 09:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190620_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='fetched_data_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
