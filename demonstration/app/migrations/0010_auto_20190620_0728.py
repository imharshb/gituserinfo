# Generated by Django 2.2.2 on 2019-06-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_userinfo_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='id',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_id',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]
