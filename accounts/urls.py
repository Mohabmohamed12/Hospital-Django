from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
   path('doctors/',views.doctor_list , name='doctor_list'),
   path('signup/' , views.signup , name='signup'),
   path('login/',views.user_login , name='login'),
   path('logout/',views.log_out,name='logout'),
   path('requests/<slug:slug>/' , views.requests , name='requests'),
   path('myprofile/', views.myprofile ,name='myprofile'),
   path('appointment/<str:slug>/' , views.appointment , name='appointment'),
   path('update_profile/',views.update_profile,name='update_profile'),
   path('doctor_detail/<str:slug>',views.doctor_detail , name='doctor_detail'),
   path('requests_delete/<int:id>/' , views.requests_delete , name='requests_delete'),
]
