from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemsView.as_view({'get':'list'})),
    path('menu-items/<int:pk>', views.MenuItemsViewSet.as_view({'get': 'retrieve'})),
]