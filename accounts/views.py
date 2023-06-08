from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile , Appointment 
from .forms import Login_Form , UserCreationForms,UpdateUserForm,UpdateProfileForm,AppointmentForm
from django.contrib.auth import authenticate , login,logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import  login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404

# import http responser 
from django.http import HttpResponse , HttpResponseRedirect
# import  get_object_or_404


def doctor_list(request):

    doctors = Profile.objects.all()

    return render(request,'user/doctor_list.html',{
        'doctors' : doctors,
    })

def doctor_detail(request,slug):

    doctor_detail=Profile.objects.get(slug=slug)

    return render(request,'user/doctor_detail.html',{
        'doctor_detail' : doctor_detail,
    })

def user_login(request):
    if request.method == 'POST':
        form = Login_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request ,username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('accounts:doctor_list')
        
    else:
        form = Login_Form()

    return render(request , 'user/login.html' , {
        'form' : form,
    
    })
def log_out(request):
    
    logout (request)
    return redirect('accounts:login')
    
    
def signup(request):
    if request.method=='POST':    
        form = UserCreationForms(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            login(request, user)
            return redirect('accounts:doctor_list')
    else:
        form=UserCreationForms()
    return render(request , 'user/signup.html',{
                'form' : form,
                'title' : 'تسجيل الدخول'
            } )
                
                
@login_required
def myprofile(request):
    return render(request,'user/myprofile.html', {
        'title' : 'الصفحه الشخصيه', 
        
    }
    )
    
def update_profile(request):
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)
    
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST , instance=request.user)
        profile_form = UpdateProfileForm(request.POST , request.FILES , instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            return redirect('accounts:myprofile')

    return render(request , 'user/update_profile.html' , {
        'title' : 'الصفحه الشخصيه',
        'user_form' : user_form,
        'profile_form' : profile_form,
    })  
    
def appointment(request , slug):
    doctor1 = get_object_or_404(Profile , slug=slug)
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.doctor = doctor1
            user_form.save()
            return redirect('accounts:myprofile')
        else:
            messages.error(request, "تأكيد من رقم الهاتف والاسم")

    else:
        form = AppointmentForm()
    return render(request , 'user/appointment.html' , {
        'form' : form
    })
def requests(request,slug):
    doctor = get_object_or_404(Profile , slug=slug)
    requests = Appointment.objects.filter(doctor=doctor)
    
    if request.method == 'POST':
        user_id = request.POST['user_id']
        print(user_id)
        r_read = get_object_or_404(Appointment, doctor_id=user_id)
        if r_read.read :
            r_read.read = False
            r_read.save()
        else:
            r_read.read = True
            r_read.save()

    return render(request , 'user/requests.html' , {
        'requests' : requests,
    })

def requests_delete(request , id):
    # user = User.objects.filter(id=request.user.id)
    requests_delete = Appointment.objects.get(id=id).delete()
    return redirect('accounts:requests', slug=request.user.profile.slug)

    
    
    
    

'''
def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        if search:
            match = Profile.objects.filter(Q(name__icontains=search) | Q(specialist_doctor__icontains=search))
            if match:
                return render(request , 'user/search.html' , {
                    'search' : search,
                    'match' : match,
                })
            else:
                messages.error(request , 'لا يوجد نتائج مطابقه')
                return redirect('accounts:doctor_list')
        else:
            return redirect('accounts:doctor_list')
    return redirect('accounts:doctor_list')
    '''
