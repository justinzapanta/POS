from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=('home')),

    #Auth
    path('login/', views.login_view, name=('home')),
]