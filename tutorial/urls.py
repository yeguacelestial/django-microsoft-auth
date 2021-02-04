from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('signin', views.sign_in, name='signin'),
    path('signout', views.home, name='signout'),
    path('calendar', views.home, name='calendar'),
    path('callback', views.callback, name='callback'),
]
