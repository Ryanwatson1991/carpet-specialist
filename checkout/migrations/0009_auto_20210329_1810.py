# Generated by Django 3.1.7 on 2021-03-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20210327_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='carpet_length',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='carpet_width',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
