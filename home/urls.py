from django.urls import  path
from . import views

urlpatterns = [
    path('',views.home,name='all'),
    path('active',views.Active,name='active'),
    path('completed',views.Completed,name='completed'),


    path('add',views.add,name='add'),


]