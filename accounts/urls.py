from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    
    path('index/', views.index, name="index"),
    path('marriage/', views.marriage, name="marriage"),

    path('profile/', views.profile, name="profile"),
    
    path('personal/', views.personal, name="personal"),
    path('childdata/', views.childdata, name="childdata"),

    path('navigation/', views.navigation, name="navigation"),

    path('delete/', views.delete, name="delete"),

    path('main/', views.main, name="main"),
    

    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]