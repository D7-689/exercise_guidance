"""authentication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.loginpage, name="login"),         #views.py <-homepage function 
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('facelogin/',views.face_login, name="facelogin"),
    path('logout/',views.logoutpage, name="logout"),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('home/', views.homepage, name="home"),
    path('profile/',views.profilepage, name="profile"),
    path('password_reset/',views.password_reset_page, name="password_reset"),
    path('dashboard/',views.dashboard),
    path('changepwd/',views.ChangePasswordPage,name="changepwd"),
    path('exercise/',views.Exercisepage,name="exercise"),
    path('exercise/video_stream/', views.video_stream, name='video_stream'),
    path('contact/', views.Contactpage, name='contact'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)