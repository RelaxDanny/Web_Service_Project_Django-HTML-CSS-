# Generated by Django 2.2.7 on 2019-11-27 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191127_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='officeloc',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
