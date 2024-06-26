"""
URL configuration for SolarSchedule project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from solar_schedule.views import EngineerDashboard, HomePage, Dashboards, ScheduleEngineer, Other, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',HomePage.as_view()),
    path('',HomePage.as_view()),
    path('engineers/',EngineerDashboard.as_view()),
    path('scheduleengineer/', ScheduleEngineer.as_view()),
    path('dashboards/', Dashboards.as_view()),
    path('other/', Other.as_view()),
    # path('auth/', Auth.as_view()),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
