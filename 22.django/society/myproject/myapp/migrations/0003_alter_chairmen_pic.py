# Generated by Django 4.1.3 on 2022-12-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_chairmen_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairmen',
            name='pic',
            field=models.FileField(default='media/set.png', upload_to='media/images/'),
        ),
    ]
