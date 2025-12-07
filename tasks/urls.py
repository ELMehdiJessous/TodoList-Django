from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo'),
    path('delete/<int:item_id>/', views.remove, name='delete'), 
]