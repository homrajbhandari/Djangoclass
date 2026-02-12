from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.student_login, name='login'),
    path("dashboard/",views.student_dashboard, name='dashboard'),
    path("logout/",views.student_logout, name='logout'),
]
