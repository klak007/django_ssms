from django.urls import path
from . import views

urlpatterns = [
    # Path converters:
    # int: number
    # str: string
    # path: whole urls /
    # slug: hyphen-and_underscore_stuff
    # uuid: universal unique identifier

    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('bikes/', views.all_bikes, name="bikes-list"),
    path('add_bike/', views.add_bike, name="add-bike"),
    path('list_salon/', views.list_salons, name="list-salon"),
    path('show_salon/<int:id_salonu>/', views.show_salon, name="show-salon"),
    path('search_bike/', views.search_bike, name="search-bike"),
    path('update_salon/<int:id_salonu>/', views.update_salon, name="update-salon"),
    path('add_salon/', views.add_salon, name="add-salon"),
    path('add_order', views.add_order, name="add-order"),
    path('delete_salon/<int:id_salonu>/', views.delete_salon, name="delete-salon"),
]
