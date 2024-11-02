"""
URL configuration for pjt_back project.

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
from django.urls import path, include
from accounts.views import CustomRegisterView, UserDetailView, update_user
from products.views import update_click_deposit, update_click_saving

urlpatterns = [
    path('admin/', admin.site.urls),
    path('interest_rate/', include('interest_rate.urls')),
    path('api/v1/', include('articles.urls')),
    path('products/', include('products.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', CustomRegisterView.as_view(), name='account_signup'),
    path('accounts/api/user/', UserDetailView.as_view(), name='user_detail'),
    path('accounts/api/update-user/', update_user, name='update_user'),
    path('products/update-click-deposit/<int:pk>/', update_click_deposit, name='update_click_deposit'),
    path('products/update-click-saving/<int:pk>/', update_click_saving, name='update_click_saving'),
]
