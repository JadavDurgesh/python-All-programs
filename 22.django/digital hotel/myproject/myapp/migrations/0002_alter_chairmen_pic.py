# Generated by Django 4.1.3 on 2022-12-29 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairmen',
            name='pic',
            field=models.FileField(default='set.jpg', upload_to='media/images/'),
        ),
    ]
