# Generated by Django 3.1 on 2020-08-26 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_auto_20200826_2014'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CategoryDetail',
        ),
        migrations.DeleteModel(
            name='ProductDetail',
        ),
        migrations.DeleteModel(
            name='SubsectionDetail',
        ),
    ]
