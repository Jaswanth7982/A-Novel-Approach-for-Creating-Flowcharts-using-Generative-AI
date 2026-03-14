# from django.urls import path
# from . import views

# urlpatterns = [
#     path('generate/', views.generate_flowchart, name='generate_flowchart'),
# ]

from django.urls import path
from . import views

urlpatterns = [

    path('', views.base, name='base'),

    # user authentication
    path('UserLoginCheck/', views.UserLoginCheck, name='UserLoginCheck'),
    path('register/', views.UserRegisterActions, name='register'),

    # user dashboard
    path('UserHome/', views.UserHome, name='UserHome'),

    # FLOWCHART PAGE 
    path('generate_docs/', views.generate_docs, name='generate_docs'),
]