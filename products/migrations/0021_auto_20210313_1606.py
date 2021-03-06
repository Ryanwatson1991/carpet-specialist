# Generated by Django 3.1.7 on 2021-03-13 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20210313_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='backing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.backing'),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.manufacturer'),
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.material'),
        ),
        migrations.AddField(
            model_name='product',
            name='style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.style'),
        ),
    ]
