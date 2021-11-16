# Generated by Django 3.2.7 on 2021-11-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0016_auto_20211103_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product2',
        ),
        migrations.AddField(
            model_name='productmen',
            name='mainType',
            field=models.CharField(choices=[('a', 'men'), ('b', 'women')], default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productmen',
            name='Type',
            field=models.CharField(choices=[('c', 'Coat'), ('j', 'Jacket'), ('b', 'Balzer'), ('o', 'Other'), ('b', 'jambsoat'), ('o', 'badboy'), ('d', 'dress'), ('a', 'accsesoris'), ('s', 'other')], max_length=1),
        ),
        migrations.DeleteModel(
            name='Productwomen',
        ),
    ]
