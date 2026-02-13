from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    # About page
    path('about/', views.about, name='about'),

    # Show category
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),

    # Add page to category
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),

    # Add category
    path('add_category/', views.add_category, name='add_category'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Restricted page
    path('restricted/', views.restricted, name='restricted'),
]