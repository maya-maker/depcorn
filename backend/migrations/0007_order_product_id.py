# Generated by Django 4.1.7 on 2023-03-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_id',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
