from django.urls import path

from . import views

urlpatterns = [
    path('waste', views.WasteList.as_view(), name='waste'),
    path('waste_national',views.WasteNational.as_view(),name='waste_national'),
    path('make_demand_trip',views.MakeDemandInTrip.as_view(),name="make_demand_trip")
]