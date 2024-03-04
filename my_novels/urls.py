from django.urls import path
from . import views

app_name = 'my_novels'
urlpatterns = [
    path('hello', views.hello_world, name='hello'),
    path('', views.list, name='list'),
    path('novel/<int:pk>/', views.DetailView.as_view(), name='detail')
]