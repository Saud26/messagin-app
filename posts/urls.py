from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.homePage, name='homePage'),

    path('submit/', views.submit_post, name='submit_post'),
    path('update/<int:pk>', views.update_post, name='update_post'),
    path('d/<int:pk>', views.delete_post, name='delete_post'),
    
]
