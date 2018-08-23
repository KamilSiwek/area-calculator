from pyproj import Proj
import json
from shapely.geometry import shape


def circumference():
    # value = input("Enter value: ")
    message = {
               "geojson":"{\"type\": \"Polygon\", \"coordinates\": [[[19.936901, 50.062682], [19.935745, 50.061403], [19.937697, 50.060558], [19.938877, 50.062003]]]}"
            }

    # Get geojson from request:
    geo = json.loads(message["geojson"])

    # Get lng and lat from geojson coordinates:
    lng, lat = zip(*geo["coordinates"][0])

    # Project area of interest (By pyproj):
    p = Proj(proj='utm', ellps='WGS84')
    x, y = p(lng, lat)

    # Calculate circumference(by shapely):
    cop = {"type": "Polygon", "coordinates": [zip(x, y)]}
    circumference = shape(cop).length
    result = {"circumference": circumference}

    return result
