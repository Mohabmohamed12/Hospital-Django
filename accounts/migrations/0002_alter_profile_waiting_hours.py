# Generated by Django 4.0.3 on 2023-05-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Waiting_hours',
            field=models.IntegerField(blank=True, null=True, verbose_name='عدد دقائق الانتظار :'),
        ),
    ]