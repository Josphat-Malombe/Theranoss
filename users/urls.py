
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('login/',views.signin, name='login'),
    path('home/', views.home, name='home'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('Disclaimer/', views.disclaimer, name='disclaimer'),
    path('Terms-and-conditions/', views.terms, name='terms'),

    #path('users/', include("django.contrib.auth.urls")),


    path('password_reset', auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
    
    
]