# Generated by Django 4.0.3 on 2022-03-30 03:10

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
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('isCE', models.BooleanField(default=False)),
                ('site', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='offreStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('datedebut', models.DateField(blank=True, null=True)),
                ('datefin', models.DateField(blank=True, null=True)),
                ('typeoffre', models.CharField(max_length=150, null=True)),
                ('domaine', models.CharField(blank=True, max_length=100)),
                ('is_archived', models.BooleanField(default=False)),
                ('auteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offrestage', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doc', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
