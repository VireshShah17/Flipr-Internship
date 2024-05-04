from django.urls import path
from . import views

app_name = 'panel'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_a_customer/', views.add_a_customer, name='add_a_cusotmer'),
]
