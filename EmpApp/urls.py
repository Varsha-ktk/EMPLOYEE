from django.urls import path

from EmpApp import views

urlpatterns=[
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('table_view',views.table_view,name='table_view'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')
]