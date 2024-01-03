"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from back import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index, name = "index" ),
    path('',views.home, name = "home" ),
    path('home/',views.home, name = "home" ),

    path('login/',views.login, name = "login" ),
    path('singapore/',views.singapore, name = "singapore" ),
    path('empRegis/',views.empRegis, name = "empRegis" ),
    path('about/',views.about, name = "about" ),
    path('Terms/',views.Terms, name = "Terms" ),
    path('contact/',views.contact, name = "contact" ),
    path('signin/',views.signin, name = "signin" ),
    path('loginin/',views.loginin, name = "loginin" ),
    path('privacy/',views.privacy, name = "privacy" ),

    path('dubai/',views.dubai, name = "dubai" ),
    path('seychelles/',views.seychelles, name = "seychelles" ),
    path('thailand/',views.thailand, name = "thailand" ),
    

    # path('contact/',views.singapore, name = "singapore" ),
    # path('contact/',views.home, name = "home" )

]
