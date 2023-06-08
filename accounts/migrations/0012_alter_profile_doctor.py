# Generated by Django 4.1 on 2023-05-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0011_alter_profile_doctor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="doctor",
            field=models.CharField(
                choices=[
                    ("جراحة أطفال", "جراحة أطفال"),
                    ("أسنان", "أسنان"),
                    ("قلب وأوعيه دموية", "قلب وأوعيه دموية"),
                    ("جراحة سمنة ومناظير ", "جراحة سمنة ومناظير "),
                    ("جراحة أورام", "جراحة أورام"),
                    ("أمراض دم", "أمراض دم"),
                    ("مخ وأعصاب", "مخ وأعصاب"),
                    ("عظام", "عظام"),
                    ("جراحة تجميل", "جراحة تجميل"),
                    ("جراحة أوعيه دموية", "جراحة أوعيه دموية"),
                    ("أورام", "أورام"),
                    ("باطنة", "باطنة"),
                    ("جلدية", "جلدية"),
                    ("تخسيس وتغذية", "تخسيس وتغذية"),
                    ("أطفال حديثي الولادة", "أطفال حديثي الولادة"),
                    ("نساء وتوليد", "نساء وتوليد"),
                    ("نفسي", "نفسي"),
                    ("أنف وأذن وحنجرة", "أنف وأذن وحنجرة"),
                ],
                max_length=50,
                verbose_name="دكتور ؟",
            ),
        ),
    ]