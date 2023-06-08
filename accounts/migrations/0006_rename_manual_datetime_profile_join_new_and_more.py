# Generated by Django 4.1 on 2023-05-23 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_remove_profile_rating"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="manual_datetime",
            new_name="join_new",
        ),
        migrations.AddField(
            model_name="profile",
            name="rating",
            field=models.PositiveIntegerField(default=0, verbose_name="التقييم"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="doctor",
            field=models.CharField(
                choices=[
                    ("جلدية", "جلدية"),
                    ("جراحة تجميل", "جراحة تجميل"),
                    ("نساء وتوليد", "نساء وتوليد"),
                    ("تخسيس وتغذية", "تخسيس وتغذية"),
                    ("مخ وأعصاب", "مخ وأعصاب"),
                    ("جراحة أطفال", "جراحة أطفال"),
                    ("أطفال حديثي الولادة", "أطفال حديثي الولادة"),
                    ("أورام", "أورام"),
                    ("جراحة أوعيه دموية", "جراحة أوعيه دموية"),
                    ("جراحة أورام", "جراحة أورام"),
                    ("أنف وأذن وحنجرة", "أنف وأذن وحنجرة"),
                    ("أسنان", "أسنان"),
                    ("قلب وأوعيه دموية", "قلب وأوعيه دموية"),
                    ("أمراض دم", "أمراض دم"),
                    ("جراحة سمنة ومناظير ", "جراحة سمنة ومناظير "),
                    ("عظام", "عظام"),
                    ("باطنة", "باطنة"),
                    ("نفسي", "نفسي"),
                ],
                max_length=50,
                verbose_name="دكتور ؟",
            ),
        ),
    ]
