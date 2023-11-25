
from django.contrib import admin
from django.urls import path
from .views import TechnicainsList,Userslist,TechnicainDetailView
urlpatterns = [
    path('technicians/',TechnicainsList, name='members'),
    path('users/',Userslist,name="users"),
    path('technicians/<int:pk>',TechnicainDetailView,name="TechnicainDetailView")
]
