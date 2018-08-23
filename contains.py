from pyproj import Proj
import json
from shapely.geometry import shape
from shapely.geometry import Point


def contains():
    # value = input("Enter value: ")
    message = {
               "geojson":"{\"type\": \"Polygon\", \"coordinates\": [[[19.936901, 50.062682], [19.935745, 50.061403], [19.937697, 50.060558], [19.938877, 50.062003]]]}"
            }

    verifiedPoint = (19.937032, 50.061587)

    # Get geojson from request:
    geo = json.loads(message["geojson"])

    points = shape(geo).contains(Point(verifiedPoint))

    result = {"contains": points}

    return result
