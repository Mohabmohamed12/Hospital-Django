from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile , Appointment 


class UserCreationForms(UserCreationForm):
    username    = forms.CharField(label = 'الإسم' )
    email       = forms.EmailField(label = 'البريد الالكترونى' )
    first_name  = forms.CharField(label = 'الإسم الاول' )
    last_name   = forms.CharField(label = 'الإسم الاخير' )
    password1   = forms.CharField(label='كلمه السر', widget=forms.PasswordInput() , min_length=8)
    password2   = forms.CharField(label='تأكيد كلمه السر ', widget=forms.PasswordInput() , min_length=8)

    class Meta:
        model   = User
        fields  = ( 'username' ,'first_name' , 'last_name' , 'email' , 'password1' , 'password2' )

class Login_Form(forms.ModelForm):
    username=forms.CharField(label='الاسم')
    password=forms.CharField(label='كلمه السر',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','password')
        
class UpdateUserForm(forms.ModelForm):
    first_name  = forms.CharField(label='الاسم الاول ')
    last_name   = forms.CharField(label='الاسم الاخير ')
    email       = forms.EmailField(label= 'البريد الاليكترونى ')
    class Meta:
        model   = User
        fields  = ('first_name' , 'last_name' , 'email')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model   = Profile
        fields  = ('who_i','name' ,'surname',
                    'subtitle','address','address_detail',
                    'price','number_phone','working_hours',
                    'Waiting_hours', 'facebook', 'twitter',
                    'google', 'doctor','image',  'specialist_doctor') 


class AppointmentForm(forms.ModelForm):
    class Meta:
        model   = Appointment
        fields  = ('name' , 'number' , 'email','Receipt' )
        

        