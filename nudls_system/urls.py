from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.DragonListCreateAPIView.as_view(),name='add_dragon'),
    path('list/', views.DragonListCreateAPIView.as_view(), name='list_dragons'),
    path('<int:pk>/delete/', views.DragonDestroy.as_view(), name='delete_dragon'),

    path('<int:pk>/updatelocation/', views.DragonLocationUpdateAPIView.as_view(), name='updatelocation'),

    path('<int:pk>/fedupdate/', views.DragonFedUpdateAPIView.as_view(), name='update_fed'),

    path('<int:pk>/updatemaintaine/', views.ZoneUpdateAPIView.as_view(), name='update_maintaine'),

    path('checkzone/', views.check_zone),

]