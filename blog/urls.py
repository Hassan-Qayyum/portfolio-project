from django.urls import path
from blog import views

urlpatterns = [

    path('', views.allblogs, name="allblogs"),
    path('<int:id>', views.detailblog, name="detailblog"),
]
