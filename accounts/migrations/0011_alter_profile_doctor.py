# Generated by Django 4.1 on 2023-05-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_alter_profile_doctor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="doctor",
            field=models.CharField(
                choices=[
                    ("أسنان", "أسنان"),
                    ("أطفال حديثي الولادة", "أطفال حديثي الولادة"),
                    ("جراحة أوعيه دموية", "جراحة أوعيه دموية"),
                    ("أورام", "أورام"),
                    ("تخسيس وتغذية", "تخسيس وتغذية"),
                    ("باطنة", "باطنة"),
                    ("عظام", "عظام"),
                    ("جراحة أورام", "جراحة أورام"),
                    ("جلدية", "جلدية"),
                    ("أنف وأذن وحنجرة", "أنف وأذن وحنجرة"),
                    ("جراحة أطفال", "جراحة أطفال"),
                    ("نفسي", "نفسي"),
                    ("نساء وتوليد", "نساء وتوليد"),
                    ("مخ وأعصاب", "مخ وأعصاب"),
                    ("قلب وأوعيه دموية", "قلب وأوعيه دموية"),
                    ("أمراض دم", "أمراض دم"),
                    ("جراحة سمنة ومناظير ", "جراحة سمنة ومناظير "),
                    ("جراحة تجميل", "جراحة تجميل"),
                ],
                max_length=50,
                verbose_name="دكتور ؟",
            ),
        ),
    ]
