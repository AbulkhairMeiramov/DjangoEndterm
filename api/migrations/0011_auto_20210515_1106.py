# Generated by Django 3.1.6 on 2021-05-15 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210515_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product_ptr',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
