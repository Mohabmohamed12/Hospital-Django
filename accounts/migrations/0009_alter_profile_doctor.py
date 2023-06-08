# Generated by Django 4.1 on 2023-05-24 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_alter_profile_doctor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="doctor",
            field=models.CharField(
                choices=[
                    ("نفسي", "نفسي"),
                    ("نساء وتوليد", "نساء وتوليد"),
                    ("أنف وأذن وحنجرة", "أنف وأذن وحنجرة"),
                    ("جلدية", "جلدية"),
                    ("أمراض دم", "أمراض دم"),
                    ("مخ وأعصاب", "مخ وأعصاب"),
                    ("باطنة", "باطنة"),
                    ("جراحة أوعيه دموية", "جراحة أوعيه دموية"),
                    ("أورام", "أورام"),
                    ("عظام", "عظام"),
                    ("جراحة سمنة ومناظير ", "جراحة سمنة ومناظير "),
                    ("جراحة أورام", "جراحة أورام"),
                    ("جراحة أطفال", "جراحة أطفال"),
                    ("قلب وأوعيه دموية", "قلب وأوعيه دموية"),
                    ("أطفال حديثي الولادة", "أطفال حديثي الولادة"),
                    ("أسنان", "أسنان"),
                    ("جراحة تجميل", "جراحة تجميل"),
                    ("تخسيس وتغذية", "تخسيس وتغذية"),
                ],
                max_length=50,
                verbose_name="دكتور ؟",
            ),
        ),
    ]
