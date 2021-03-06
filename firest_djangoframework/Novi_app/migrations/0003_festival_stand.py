# Generated by Django 2.1.5 on 2019-01-21 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Novi_app', '0002_item_storage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=100)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three')])),
                ('stand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Novi_app.Festival')),
            ],
        ),
    ]
