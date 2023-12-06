from django.urls import path
from . import views


app_name = 'tree'


urlpatterns = [
    path('list-menu/<int:id>', views.display_menu, name='display-menu'),
    path('list-menu/', views.list_menu, name='list-menu'),
]
