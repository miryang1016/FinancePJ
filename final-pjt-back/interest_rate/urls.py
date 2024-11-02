from django.urls import path
from . import views

app_name = 'interest_rate'
urlpatterns = [
    path('save_rates/', views.save_rates, name = 'save_rates'),
    path('calculate/', views.calculate, name='calculate'),
]