
from django.urls import path,include
from .import views

urlpatterns = [

    path('',views.index),
    path('about-me.html',views.about),
    path('recent-posts.html',views.recent)

]

