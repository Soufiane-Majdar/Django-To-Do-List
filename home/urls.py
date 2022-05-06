from django.urls import  path
from . import views

urlpatterns = [
    path('',views.home,name='all'),
    path('active',views.Active,name='active'),
    path('completed',views.Completed,name='completed'),


    path('add',views.add,name='add'),
    path('donne/<int:idt>',views.donne,name='donne'),
    path('delete/<int:idt>',views.delete,name='delete'),



]