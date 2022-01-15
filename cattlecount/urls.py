from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("home", views.home),
    path("about/", views.about),
    path("addcattle", views.handleaddcattle, name='handleaddcattle'),
    path("deletecattle", views.handledeletecattle, name='handledeletecattle'),
    path("addemployee", views.handleaddemployee, name='handleaddemployee'),
    path("deleteemployee", views.handledeleteemployee, name='handledeleteemployee'),
    path("addshed", views.handleaddshed, name='handleaddshed'),
    path("deleteshed", views.handledeleteshed, name='handledeleteshed'),
    path("vemp/",views.viewemployee),
    path("vcat/",views.viewcattle),
    path("vshed/",views.viewshed),
]