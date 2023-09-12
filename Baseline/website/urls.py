from django.urls import path 
from . import views

urlpatterns = [
    # path('current_date/', views.current_date1, name='current_date'),
    # path('current_date/', views.sum, name = 'sum'),
    path('current_date/', views.form_view, name='form_view'),
]