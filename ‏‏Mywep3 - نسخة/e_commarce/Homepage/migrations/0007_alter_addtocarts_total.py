# Generated by Django 3.2.7 on 2021-11-02 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0006_addtocarts2_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtocarts',
            name='Total',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
