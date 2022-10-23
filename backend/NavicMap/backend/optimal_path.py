from .algorithms.aStarSearch import *
from .models import *
from .algorithms.geo_coordinate_algorithms import pathDistance, coordinateInsidePolygon

inf = 10**20
# x = latitude y = longitude
class Coordinate:
    def __init__(self, x, y):
        self.__address = self.calcAddress(x, y)

    def calcAddress(self, x, y):  # information = country, state, city, area, x, y
        address = {"x": x, "y": y}

        countries = Country.objects()
        states = []
        cities = []
        areas = []

        for country in countries:
            coordinates = []
            for node in country.coordinates:
                coordinates.append((node.latitude, node.longitude))
            if coordinateInsidePolygon(coordinates, (x, y)):
                address["country"] = (country.name, country.id)
                states = country.states
                break

        for iterator in states:
            state = State.objects(id=iterator).first()
            coordinates = []
            for node in state.coordinates:
                coordinates.append((node.latitude, node.longitude))
            if coordinateInsidePolygon(coordinates, (x, y)):
                address["state"] = (state.name, state.id)
                cities = state.cities
                break

        for iterator in cities:
            city = City.objects(id=iterator).first()
            coordinates = []
            for node in city.coordinates:
                coordinates.append((node.latitude, node.longitude))
            if coordinateInsidePolygon(coordinates, (x, y)):
                address["city"] = (city.name, city.id)
                areas = city.areas
                break

        for iterator in areas:
            area = Area.objects(id=iterator).first()
            coordinates = []
            for node in area.coordinates:
                coordinates.append((node.latitude, node.longitude))
            if coordinateInsidePolygon(coordinates, (x, y)):
                address["area"] = (area.name, area.id)
                break

        return address

    @property
    def Address(self):
        return self.__address

    @property
    def coordinate(self):
        return (self.__address["x"], self.__address["y"])


class Path:
    def __init__(self, startX, startY, endX, endY):
        self.start = Coordinate(startX, startY)
        self.end = Coordinate(endX, endY)

    def isSame(self, qry):
        return str(int(self.start.Address[qry] == self.end.Address[qry]))

    def getGraph(self, obj):
        graph = {}
        for lst in obj:
            par = (lst.parent_node.latitude, lst.parent_node.longitude)
            graph[par] = []
            for child in lst.children:
                c = (child.latitude, child.longitude)
                graph[par].append(c)
        return graph

    def nearestRoad(self, graph, node):
        near_point = (inf, (0, 0))
        for parent in graph:
            distance = pathDistance(node, parent)
            if distance < near_point[0]:
                near_point = (distance, parent)
        return near_point[1]

    def totalPathDistance(self, lst):
        distance = 0
        for node in range(1, len(lst)):
            distance += pathDistance(lst[node - 1], lst[node])
        return distance

    def sameArea(self):
        area = Area.objects(id=self.start.Address["area"][1]).first()
        gr = self.getGraph(area.graph)

        near_start = self.nearestRoad(gr, self.start.coordinate)
        near_end = self.nearestRoad(gr, self.end.coordinate)

        path = AstarSearch(graph=gr).searchPath(start=near_start, end=near_end)

        path.insert(0, self.start.coordinate)
        path.append(self.end.coordinate)
        distance = self.totalPathDistance(path)
        fin = []
        for point in path:
            fin.append([point[1], point[0]])
        return (fin, distance)

    def sameCity(self):
        path = []
        # implement it
        return path

    def sameState(self):
        path = []
        # implement it
        return path

    def sameCountry(self):
        path = []
        # implement it
        return path

    def samePlanet(self):
        path = []
        # implement it
        return path

    def getCombinationCode(self):
        return (
            self.isSame(qry="country")
            + self.isSame(qry="state")
            + self.isSame(qry="city")
            + self.isSame(qry="area")
        )

    def getOptimalPath(self):

        code_combination = self.getCombinationCode()

        match code_combination:
            case "1111":
                return self.sameArea()
            case "1110":
                return self.sameCity()
            case "1100":
                return self.sameState()
            case "1000":
                return self.sameCountry()
            case default:
                return self.samePlanet()
