"""Example file to call methods."""

from calculate2 import Calculate

pointsOfArea = {
    	   "geojson":"{\"type\": \"Polygon\", \"coordinates\": [[[19.936901, 50.062682], [19.935745, 50.061403], [19.937697, 50.060558], [19.938877, 50.062003]]]}"
        }

verifiedPoint = (19.937032, 50.061587)

# calculate area:
area = Calculate.area(pointsOfArea)
print("Area: {}".format(area))

# calculate circumference:
circumference = Calculate.circumference(pointsOfArea)
print("Circumference: {}".format(circumference))

# calculate distance:
distance = Calculate.distance(pointsOfArea)
print("Distance: {}".format(distance))

# checking if the point is in a given area:
contains = Calculate.contains(pointsOfArea, verifiedPoint)
print("Contains: {}".format(contains))
