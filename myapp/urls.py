from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_event/', views.new_event, name='new_event'),
    path('delete_event/<int:todo_id>/', views.delete_event, name='delete_event'),

]
