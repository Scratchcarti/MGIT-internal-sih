from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('',views.index, name='index'),
    path('application/',views.application, name='application'),
    path('upload/', views.upload, name='upload'),
    path('status/', views.status, name='status'),
    path('sag/',views.sag,name='sag'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
]
