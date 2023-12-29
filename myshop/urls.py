"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from .import index
#from shop.views import home_view
from register import views as v
from contact import views as p
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/login/', auth_views.LoginView.as_view(),name='login'),
    #path('accounts/logout/', auth_views.LogoutView.as_view(),name='logout'),
    #path('',home_view,name='home'),
    #path('',index.home),
    #path('', views.home, name='home')
    #path('register/', include('register.urls', namespace='register')),
    
    path('register/', v.register, name='register'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include("django.contrib.auth.urls")),
    #path("register/",include('register.urls', namespace="register")),
    path('', include('shop.urls', namespace='shop')),
    #path('contact/', include('contact.urls', namespace='contact'))
    path('index', p.index, name='index'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
