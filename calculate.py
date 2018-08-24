from pyproj import Proj
import json
from shapely.geometry import shape

class Area():
    def __init__(self, location):
        self.location = location

    def area(location):
        message = self.location

        # Get geojson from request:
        geo = json.loads(message["geojson"])

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
