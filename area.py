"""Module to calculate."""

from pyproj import Proj
import json
from shapely.geometry import shape


class Area():
    """Class to calculate area."""

    @staticmethod
    def area(location):
        """Method to calculate area."""
        # Get geojson from request:
        geo = json.loads(location["geojson"])

        # Get lng and lat from geojson coordinates:
        lng, lat = zip(*geo["coordinates"][0])

        # Project area of interest (By pyproj):
        pa = Proj("+proj=aea ")
        x, y = pa(lng, lat)

        # Calculate area(by shapely):
        cop = {"type": "Polygon", "coordinates": [zip(x, y)]}
        area = shape(cop).area

        # Preperate result in dict:
        result = {"area": area}
        return result
