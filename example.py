from calculate import Area

location = {
    	   "geojson":"{\"type\": \"Polygon\", \"coordinates\": [[[19.936901, 50.062682], [19.935745, 50.061403], [19.937697, 50.060558], [19.938877, 50.062003]]]}"
        }
# geojson = Area(location)
# result = geojson.area()

result = Area.area(location)

print result

# class Test():
#     def __init__(self, name):
#         self.name = name
