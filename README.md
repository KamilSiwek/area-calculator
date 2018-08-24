# area-calculator

# AREA-CALCULATOR

Puckage to:
* calculate area and circumference points of takes location.
* calculate distance betweet points of takes location.
* checking if the point is in a given area

## Technologies

* Python 2.7

## Getting started

To add package to your project(in commandline):

```
pip install calculate
```

## Usage

Add to your project file:

```
from calculate import Calculate
```

### Parameters format:

#### area should be in the geojson format. For example:
```
pointsOfArea = {
    	   "geojson":"{\"type\": \"Polygon\", \"coordinates\": [[[19.936901, 50.062682], [19.935745, 50.061403], [19.937697, 50.060558], [19.938877, 50.062003]]]}"
         }
```
#### Point should be in the tumple format. For example:
```
verifiedPoint = (19.937032, 50.061587)
```

### To calculate area:

```
area = Calculate.area(pointsOfArea)
```

### To calculate circumference:

```
circumference = Calculate.circumference(pointsOfArea)
```

### To calculate distance:

```
distance = Calculate.distance(pointsOfArea)
```

### For checking if the point is in a given area:

```
contains = Calculate.contains(pointsOfArea, verifiedPoint)
```

### Version 0.0.1
