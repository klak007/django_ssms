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
]
