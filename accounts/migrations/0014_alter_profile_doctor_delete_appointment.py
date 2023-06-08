# Generated by Django 4.1 on 2023-05-28 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0013_alter_profile_doctor_appointment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="doctor",
            field=models.CharField(
                choices=[
                    ("أطفال حديثي الولادة", "أطفال حديثي الولادة"),
                    ("نفسي", "نفسي"),
                    ("أورام", "أورام"),
                    ("باطنة", "باطنة"),
                    ("جراحة أورام", "جراحة أورام"),
                    ("أسنان", "أسنان"),
                    ("أنف وأذن وحنجرة", "أنف وأذن وحنجرة"),
                    ("نساء وتوليد", "نساء وتوليد"),
                    ("جراحة أوعيه دموية", "جراحة أوعيه دموية"),
                    ("عظام", "عظام"),
                    ("جلدية", "جلدية"),
                    ("جراحة تجميل", "جراحة تجميل"),
                    ("قلب وأوعيه دموية", "قلب وأوعيه دموية"),
                    ("مخ وأعصاب", "مخ وأعصاب"),
                    ("تخسيس وتغذية", "تخسيس وتغذية"),
                    ("جراحة سمنة ومناظير ", "جراحة سمنة ومناظير "),
                    ("أمراض دم", "أمراض دم"),
                    ("جراحة أطفال", "جراحة أطفال"),
                ],
                max_length=50,
                verbose_name="دكتور ؟",
            ),
        ),
        migrations.DeleteModel(
            name="Appointment",
        ),
    ]
