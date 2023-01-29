import requests
from django.conf import settings


class FoursquareService:
    latitude = ""
    longitude = ""

    def __init__(self, location_data):
        self.latitude = location_data.get("latitude")
        self.longitude = location_data.get("longitude")

    def _get_url(self):
        url = settings.FOURSQUARE_BASE_URL + "/places/search?ll={}%2C{}".format(self.latitude, self.longitude)
        return url

    def _get_header(self):
        headers = {
            "accept": "application/json",
            "Authorization": settings.FOURSQUARE_AUTHORIZATION_TOKEN
        }
        return headers

    def get_location_datas(self):
        response = requests.get(self._get_url(), headers=self._get_header())
        locations = response.json().get("results")

        location_list = []

        for location in locations:
            location_list.append(
                {
                    "fsq_id": location.get("fsq_id"),
                    "latitude": location.get("geocodes").get("main").get("latitude"),
                    "longitude": location.get("geocodes").get("main").get("longitude"),
                    "address": location.get("location").get("address"),
                    "country": location.get("location").get("country"),
                    "region": location.get("location").get("region"),
                    "name": location.get("name"),
                }
            )

        return location_list



