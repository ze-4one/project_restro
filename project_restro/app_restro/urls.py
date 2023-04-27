from django.urls import path
from . import views
urlpatterns = [
    path('menu/', views.menu_index, name='menu-list'),
    path('menu/add/', views.menu_add, name='menu-add'),
    path('menu/edit/', views.menu_edit, name='menu-edit'),
    path('menu/show/', views.menu_show, name='menu-show'),

    # category
    path('category/create/',views.category_create, name='category-create')

]