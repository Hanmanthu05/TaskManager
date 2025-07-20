
from django.urls import path
from . import views


urlpatterns = [
   path('',views.index,name='Home'),
   path('add/',views.add_task,name='addTask'),
   path('List-Tasks/',views.task_list,name='listTask'),
   path('Completed-Tasks/',views.completed,name='completedTask'),
   path('delete/<int:task_id>/',views.delete_task,name='deleteTask'),
   path('edit/<int:task_id>/',views.update_task,name='updateTask'),
   path('Pending-Tasks/',views.pending,name='pendingTask'),
   path('register/',views.register,name='register'),
   path('profile/',views.profile,name='profile'),
] 
