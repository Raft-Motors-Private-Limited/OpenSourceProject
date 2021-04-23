from django.urls import path
from . import views
urlpatterns = [
    path('',views.todo, name="main"),
    path('update_task/<str:pk>/',views.updateTask, name="update_task"),
    path('delete/<int:pk>/',views.deleteitem, name="delete_task"),
    
]
