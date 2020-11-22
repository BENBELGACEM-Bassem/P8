from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'favorites'

urlpatterns = [
    path('list', login_required(views.FavoriteListView.as_view()), name='list'),
    path('save', login_required(views.SaveFavouriteView.as_view()), name='save'),
    path('delete', login_required(views.DeleteFavouriteView.as_view()), name='delete'),
]
