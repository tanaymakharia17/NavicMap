from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, Polygon, Feature
from math import radians, cos, sin, asin, sqrt


def coordinateInsidePolygon(coordinates, point):
    point = Feature(geometry=Point(point))
    polygon = Polygon(
        [
            coordinates
        ]
    )
    return boolean_point_in_polygon(point, polygon)

def pathDistance(x, y):
    
    lat1, lon1 = radians(x[0]), radians(x[1])
    lat2, lon2 = radians(y[0]), radians(y[1])
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # for meter multiply 1000
    return(c * r)
