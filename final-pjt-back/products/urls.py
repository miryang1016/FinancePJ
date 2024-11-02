from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('get_deposit/', views.get_deposit, name = 'get_deposit'), # 예금 데이터 가져오기
    path('get_saving/', views.get_saving, name = 'get_saving'), # 적금 데이터 가져오기
    path('deposit_list/', views.deposit_list, name = 'deposit_list'), 
    path('saving_list/', views.saving_list, name = 'saving_list'), 
    path('deposit_list/<int:pk>/', views.deposit_detail, name = 'deposit_detail'), 
    path('saving_list/<int:pk>/', views.saving_detail, name = 'saving_detail'),
]