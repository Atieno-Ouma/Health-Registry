
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),

    path('list_facility/',views.list_facility, name="list_facility"),
    path('list_client/', views.list_client, name="list_client"),

    path('add_facility/', views.add_Facility, name="add_facility"),
    path('add_client/', views.add_client, name="add_client"),


    path('delete_facility/<str:pk>/', views.delete_facility, name="delete_facility"),
    path('delete_client/<str:pk>/', views.delete_client, name="delete_client"),
    path('facility_report/<str:pk>/', views.stock_detail, name="stock_detail"),


    path('admin/', admin.site.urls),
    path('update_facility/<str:pk>/',views.update_facility,name="update_facility"),
    path('update_client/<str:pk>/',views.update_client,name="update_client")

]
