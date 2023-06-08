from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


TYPE_OF_PERSON = (
    ('M', "Male"),
    ('F', "Female"),
)

DOCTOR_IN={
        ( "جلدية" , "جلدية"),
        ( "أسنان" , "أسنان"),
        ( "نفسي" , "نفسي"),
        ( "أطفال حديثي الولادة"  , "أطفال حديثي الولادة"),
        ( "مخ وأعصاب"  , "مخ وأعصاب"),
        (  "عظام" , "عظام"),
        ( "نساء وتوليد"  , "نساء وتوليد"),
        ( "أنف وأذن وحنجرة"   , "أنف وأذن وحنجرة"),
        ( "قلب وأوعيه دموية"   , "قلب وأوعيه دموية"),
        ( "أمراض دم" , "أمراض دم"),
        ( "أورام" , "أورام"),
        ( "باطنة" , "باطنة"),
        ( "تخسيس وتغذية"  , "تخسيس وتغذية"),
        ( "جراحة أطفال"  , "جراحة أطفال"),
        ( "جراحة أورام"  , "جراحة أورام"),
        ( "جراحة أوعيه دموية"   , "جراحة أوعيه دموية"),
        ( "جراحة تجميل"  , "جراحة تجميل"),
        ( "جراحة سمنة ومناظير "   , "جراحة سمنة ومناظير "),
    }

class Profile(models.Model):

    user = models.OneToOneField(User, verbose_name="user", on_delete=models.CASCADE)
    name = models.CharField(" : الاسم", max_length=80)
    surname = models.CharField(" : اللقب", max_length=80)
    subtitle = models.CharField("نبذه عنك :", max_length=100)
    address = models.CharField("المحافظه :", max_length=50)
    address_detail = models.CharField("العنوان بالتفصيل :", max_length=50)
    number_phone = models.CharField("الهاتف :", max_length=50)
    working_hours = models.CharField("عدد ساعات العمل :", max_length=10)
    Waiting_hours = models.IntegerField("عدد دقائق الانتظار :", null=True, blank=True)
    who_i = models.TextField(": من انا", max_length=250)
    price = models.DecimalField(": سعر الكشف", max_digits=8, decimal_places=2, null=True, blank=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    google = models.CharField(max_length=100, blank=True, null=True)
    type_doctors = models.CharField("gender", choices=TYPE_OF_PERSON, default='M', max_length=20)
    #join_us = models.DateTimeField(verbose_name="وقت الانضمام", auto_now_add=True)
    join_new = models.DateTimeField(verbose_name="وقت الانضمام", null=True, blank=True)
    image = models.ImageField("الصوره الشخصيه", upload_to='profile')
    specialist_doctor = models.CharField("متخصص في ؟", max_length=100, blank=True, null=True)
    doctor = models.CharField("دكتور ؟",choices=DOCTOR_IN, max_length=50)
    slug = models.SlugField("slug", blank=True, null=True)
    rating = models.PositiveIntegerField("التقييم", default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
            print(self.user.username)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        

        
class Appointment(models.Model):
    doctor      = models.ForeignKey('Profile',related_name="doc" , verbose_name=("doctor"), on_delete=models.CASCADE  , blank=True, null=True)
    name        = models.CharField(("الإسم") , max_length=100)
    number      = models.CharField(("رقم الهاتف") , max_length=20)
    email       = models.EmailField(("الإيميل"), max_length=50)
    read        = models.BooleanField(("تمت القراءة"), blank=True, null=True)
    Receipt     = models.CharField(("رقم الايصال") , max_length=20)

    def __str__(self):
        return self.name