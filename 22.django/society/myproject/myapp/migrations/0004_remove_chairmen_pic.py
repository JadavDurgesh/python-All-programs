# Generated by Django 4.1.3 on 2022-12-13 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_chairmen_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chairmen',
            name='pic',
        ),
    ]
