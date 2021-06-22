from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage,name='home2'),
    path('home/', views.home,name='home'),
    
    path('create_complaint/<int:pk>/',views.createComplaint,name='create_complaint'),
    path('update_complaint/<str:pk>/',views.updateComplaint,name='update_complaint'),
    path('delete_complaint/<str:pk>/',views.deleteComplaint,name='delete_complaint'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/',views.logoutUser,name='logout'),
    

    path('student/<str:pk_test>/', views.students,name='student'),
    path('complaint/<str:pk_test>/',views.complaintinfo,name='complaint'),
  
]