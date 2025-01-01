from django.urls import path
from . import views


urlpatterns = [
    path('login_user', views.login_user,name='login_user'),
    path('', views.main,name='main'),
    path('signout', views.signout, name='signout'),
    path('signup',views.signup,name='signup'),

]