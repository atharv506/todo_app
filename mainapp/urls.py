from django.urls import path
from . import views


urlpatterns = [
    path('', views.demo,name='demo'),
    path('login_user', views.login_user,name='login_user'),
    path('signup',views.signup,name='signup'),

]