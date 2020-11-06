from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('legal', views.LegalNoticeView.as_view(), name='legal_notice'),
]
