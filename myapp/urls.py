from django.urls import path
from .views import task_list, task_detail
from .views import SecureHelloView

urlpatterns = [
    path('tasks/', task_list, name='task-list'), 
    path('tasks/<int:pk>/', task_detail, name='task-detail'), 
    path('secure-hello/', SecureHelloView.as_view()),
]

