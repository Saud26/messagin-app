from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

app_name = 'authsystem'

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('settings/<int:pk>', views.settings_view, name='settings'),

    # path('reset_password/',
    #     auth_views.PasswordResetView.as_view(),
    #     name='password_reset'),

    # path('reset_password_sent/', 
    #     auth_views.PasswordResetDoneView.as_view(), 
    #     name='password_reset_done'),

    # path('reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(), 
    #     name='password_reset_confirm'),

    # path('reset_password_complete/', 
    #     auth_views.PasswordResetCompleteView.as_view(), 
    #     name='password_reset_complete'),
    
]



# template_name="authsystem/password_reset.html"
# template_name="authsystem/password_reset_sent.html"
# template_name="authsystem/password_reset_form.html"
# template_name="authsystem/password_reset_done.html"