from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task', views.task, name='task'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('view/<str:pk>', views.view, name="view"),
]
