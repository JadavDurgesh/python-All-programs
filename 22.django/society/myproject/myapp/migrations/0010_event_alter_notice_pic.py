# Generated by Django 4.1.3 on 2023-01-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pic', models.FileField(blank=True, default='media/soceity.mp4', null=True, upload_to='media/video/')),
            ],
        ),
        migrations.AlterField(
            model_name='notice',
            name='pic',
            field=models.FileField(blank=True, default='media/set.png', null=True, upload_to='media/images/'),
        ),
    ]
