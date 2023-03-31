from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.list_rooms, name="rooms"),
    path('new', views.new, name="new")
]
