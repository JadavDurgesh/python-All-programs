# Generated by Django 4.1.3 on 2022-12-13 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=30)),
                ('family_member', models.CharField(max_length=30)),
                ('job_location', models.CharField(max_length=30)),
                ('block_no', models.CharField(max_length=30)),
                ('house_no', models.CharField(max_length=30)),
                ('pic', models.FileField(default='media/set.png', upload_to='media/images/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
