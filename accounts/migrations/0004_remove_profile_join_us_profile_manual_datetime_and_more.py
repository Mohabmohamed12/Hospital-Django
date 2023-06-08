# Generated by Django 4.0.3 on 2023-05-23 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='join_us',
        ),
        migrations.AddField(
            model_name='profile',
            name='manual_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='وقت الانضمام'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=50, verbose_name='المحافظه :'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_detail',
            field=models.CharField(max_length=50, verbose_name='العنوان بالتفصيل :'),
        ),
    ]