# Generated by Django 4.1.3 on 2023-01-02 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_notice_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notice',
        ),
    ]
