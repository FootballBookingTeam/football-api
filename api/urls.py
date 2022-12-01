from django.urls import path
from . import views

urlpatterns = [
    path('users/<str:id>', views.get_user, name="user"),
    path('users', views.get_users, name="users"),
    path('user/login', views.view_login, name="login"),
    path('turfs', views.get_turfs, name="turfs"),
    path('turfs/<str:id>', views.get_turf, name="turf"),
    path('turfs/<str:turf_id>/images', views.get_turf_images, name="images"),
    path('schedules', views.api_schedules, name="schedules"),
    path('schedules/<str:id>', views.api_schedule, name="schedule")
]
