from django.contrib import admin         
from django.urls import path
from . import views as mainView
from admins import views as admins
from django.conf import settings 
from django.conf.urls.static import static   
from django.contrib import admin
from django.urls import path, include
from users import views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # connect users app
    path('', include('users.urls')),

    # Main Views
    path("", mainView.index, name="index"),
    path("AdminLogin/", mainView.AdminLogin, name="AdminLogin"),
    path("UserLogin/", mainView.UserLogin, name="UserLogin"),  # Renders login form  # Handles POST

    path("UserRegister/", mainView.UserRegister, name="UserRegister"),  # Renders register form  # Handles POST

    # Admin Views
    path("AdminHome/", admins.adminHome, name="AdminHome"),
    path("adminlogin/", admins.adminLoginCheck, name="AdminLoginCheck"),
    path("RegisterUsersView/", admins.RegisterUsersView, name="RegisterUsersView"),
    path("ActivaUsers/", admins.activateUser, name="ActivaUsers"),
    path("deactivate_user/", admins.DeactivateUsers, name="deactivate_user"),
    path("delete_user/", admins.deleteUser, name="delete_user"),
    

    # User Views
    path("UserHome/", views.UserHome, name="UserHome"),
    path("", views.base, name='base'),

    path('generate/', views.generate_flowchart, name='generate_flowchart'),
    # path('export_pdf/',usr.export_pdf,name='export_pdf'),
    path("register/", views.UserRegisterActions, name="register"), 
    path("UserLoginCheck/", views.UserLoginCheck, name="UserLoginCheck"),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    

