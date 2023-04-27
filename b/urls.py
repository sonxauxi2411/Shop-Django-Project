"""
URL configuration for b project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app_a import views
urlpatterns = [
    
    path('', views.shopPage, name='shop'),
    path('admin/', admin.site.urls),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('create-product', views.createProducts, name='create-product'),
    path('product/<int:id>/', views.productDetail, name='productDetail'),
    path('add-to-cart/<int:id>/', views.addToCart, name='addToCart'),
    path('cart/', views.carts, name='cart'),
    path('cart/<int:id>/<int:qty>/<int:total>/', views.updateCart, name='updateCart'),
    path('cart/<int:id>/', views.deleteCart, name='deleteCart'),
]
