from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_view, name='schedule'),
    path('reserve/<str:date>/<str:time_slot>/', views.reserve_slot, name='reserve_slot'),
]
