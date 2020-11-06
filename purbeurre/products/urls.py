from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('results', views.ResultView.as_view(), name='results'),
]
