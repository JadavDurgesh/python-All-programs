# Generated by Django 4.1.3 on 2022-12-12 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='chairmen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('contac', models.CharField(max_length=30)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
