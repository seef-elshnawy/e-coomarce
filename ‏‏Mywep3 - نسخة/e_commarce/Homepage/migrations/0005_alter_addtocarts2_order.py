# Generated by Django 3.2.7 on 2021-11-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0004_addtocarts2_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtocarts2',
            name='order',
            field=models.ManyToManyField(blank=True, to='Homepage.cart'),
        ),
    ]
