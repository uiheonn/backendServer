# Generated by Django 3.2.16 on 2023-02-11 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmaillistUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_email', models.CharField(max_length=64, null=True)),
                ('g_password', models.CharField(max_length=128, null=True)),
                ('g_key', models.CharField(max_length=64, null=True)),
                ('n_email', models.CharField(max_length=64, null=True)),
                ('n_password', models.CharField(max_length=64, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
