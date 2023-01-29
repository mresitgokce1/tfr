from django.urls import path
from api.locations.views import LocationsView

urlpatterns = [
    path('locations', LocationsView.as_view())
]