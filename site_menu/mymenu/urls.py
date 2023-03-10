from django.urls import path
from .views import CategoryMenuListView, get_my_menu

urlpatterns = [
    path('', CategoryMenuListView.as_view(), name='category-menu-list'),
    path('<str:slug>/', get_my_menu, name='podcategory-menu'),
]