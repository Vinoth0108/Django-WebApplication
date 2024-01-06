from django.contrib import admin
from django.urls import path, include
from Myapp import views

urlpatterns = [
    
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('goback/', views.goback, name="goback"),
    path('notallowed/', views.notallowed, name="notallowed"),

    
    path('tabular_view/', views.tabular_view, name="tabular_view"),
    path('chart_view/', views.chart_view, name="chart_view"),
    path('graph_view/', views.graph_view, name="graph_view"),


    path('dashboard/', views.dashboard, name="dashboard"),
    path('histogram/', views.histogram, name="histogram"),
    path('treemaps/', views.treemaps, name="treemaps"),


    path('time/', views.time, name="time"),
    path('network/', views.network, name="network"),
    path('boxplot/', views.boxplot, name="boxplot"),


    path('user_credentials/', views.all_users_credentials_json, name='all_users_credentials_json'), 
]