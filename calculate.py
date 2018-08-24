"""Module to calculate."""

from pyproj import Proj
import json
from shapely.geometry import shape
from shapely.geometry import LineString
from shapely.geometry import Point


class Area():
    """Class to calculate area."""

    @staticmethod
    def area(pointsOfArea):
        """Method to calculate area."""
        # Get geojson from request:
        geo = json.loads(pointsOfArea["geojson"])

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


class Distance():
    """Class to calculate distance between given points."""

    @staticmethod
    def distance(pointsOfArea):
        """Method to calculate distance between given points."""
        # Get geojson from request:
        geo = json.loads(pointsOfArea["geojson"])

        # Get lng and lat from geojson coordinates:
        lng, lat = zip(*geo["coordinates"][0])

        # Project area of interest (By pyproj):
        p = Proj(proj='utm', ellps='WGS84')
        x, y = p(lng, lat)

        # Calculate length(by shapely):
        cop = {"type": "Polygon", "coordinates": [zip(x, y)]}

        points = LineString(cop["coordinates"][0])
        distance = points.length

        # Preperate result in dict:
        result = {"distance": distance}

        return result


class Circumference():
    """Class to calculate circumference of the area."""

    @staticmethod
    def circumference(pointsOfArea):
        """Method to calculate circumference of the area."""
        # Get geojson from request:
        geo = json.loads(pointsOfArea["geojson"])

        # Get lng and lat from geojson coordinates:
        lng, lat = zip(*geo["coordinates"][0])

        # Project area of interest (By pyproj):
        p = Proj(proj='utm', ellps='WGS84')
        x, y = p(lng, lat)

        # Calculate circumference(by shapely):
        cop = {"type": "Polygon", "coordinates": [zip(x, y)]}
        circumference = shape(cop).length

        # Preperate result in dict:
        result = {"circumference": circumference}

        return result


class Contains():
    """Class to calculate contains."""

    @staticmethod
    def contains(pointsOfArea, verifiedPoint):
        """Method for checking if the point is in a given area."""
        """Takes pointsOfArea and verifiedPoint as parameters."""
        """Location is format geojson."""
        """verifiedPoint is point for example: (19.937032, 50.061587)"""
        # Get geojson from request:
        geo = json.loads(pointsOfArea["geojson"])

        # verifiedPoint = (19.937032, 50.061587)

        # Checking if the point is in a given area(by shapely):
        points = shape(geo).contains(Point(verifiedPoint))

        result = {"contains": points}

        return result
