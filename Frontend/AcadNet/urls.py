from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('loadFile/', views.loadFile, name='loadFile'),
    path('previewXML/', views.previewXML, name='previewXML'),
    path('sendFile/', views.sendFile, name='sendFile'),
    path('cleanSystem/', views.cleanSystem, name='cleanSystem'),
    path('about/', views.about, name='about'),
    path('informationSystem/', views.informationSystem, name='informationSystem'),
    path('logout/', views.logout, name='logout'),
    path('dashboard_tutor/<str:username>/', views.dashboard_tutor, name='dashboard_tutor'),
    path('horariosTutor/<str:username>/', views.horariosTutor, name='horariosTutor'),
    path('uploadSchedule/<str:username>/', views.uploadSchedule, name='uploadSchedule'),
    ]