from django.urls import path,include
from . import views

app_name='tour'
urlpatterns = [
    path('', views.tour, name='tour'), 
    path('ajax_data/', views.ajax_data, name='ajax_data'),
]