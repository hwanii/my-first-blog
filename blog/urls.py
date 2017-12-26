from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('post/<int:pk>/',views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('join/', views.signup, name='signup'),
    path('login/',views.signin, name='signin'),
    path('logout/',auth_views.logout, {'next_page':'/'}), #로그아웃 기능
]
