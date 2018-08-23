from pyproj import Proj
import json
from shapely.geometry import shape
from shapely.geometry import LineString


class distance:
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

    # Calculate length(by shapely):
    cop = {"type": "Polygon", "coordinates": [zip(x, y)]}

    points = LineString(cop["coordinates"][0])
    distance = points.length

    result = {"distance": distance}

    print(result)
