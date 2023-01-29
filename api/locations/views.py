from rest_framework.decorators import api_view, action
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from api.locations.serializers import LocationSerializer
from integrations.foursquare.services import FoursquareService
from rest_framework.exceptions import ValidationError
from locations.models import Location
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class LocationsView(ListCreateAPIView):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        methods=['post'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['latitude', 'longitude'],
            properties={
                'latitude': openapi.Schema(type=openapi.TYPE_NUMBER),
                'longitude': openapi.Schema(type=openapi.TYPE_NUMBER),
            },
        ),
        operation_description='Create an location'
    )
    @action(detail=True, methods=['post'])
    def post(self, request):
        try:
            coordinate_serializer = LocationSerializer(data=request.data)
            coordinate_serializer.is_valid(raise_exception=True)

            foursquare_service = FoursquareService(coordinate_serializer.data)
            location_list = foursquare_service.get_location_datas()

            for location in location_list:
                location_serializer = LocationSerializer(data=location)
                try:
                    location_serializer.is_valid(raise_exception=True)
                    location_serializer.save()
                except ValidationError:
                    location["errors"] = location_serializer.errors
                except Exception as error:
                    location["errors"] = error
        except Exception as error:
            return Response({"errors": error})

        return Response({"count": len(location_list), "results": location_list})

