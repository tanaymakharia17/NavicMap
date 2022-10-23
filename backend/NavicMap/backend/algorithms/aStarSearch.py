from .heap import Heap
from .geo_coordinate_algorithms import pathDistance

inf = 10**20

class AstarSearch:

    def __init__(self, graph):
        self.graph = graph
    
    def heuristicsValue(self, x, y): #imporove hurestic for better performance
        return pathDistance(x, y)

    def searchPath(self, start, end):

        priority_queue = Heap("min")
        par = {}
        distance = {start: 0.0}
        fx = 0.0 + self.heuristicsValue(start, end) # fx = hx + start_to_node_distance
        priority_queue.push((fx, start))
        while not priority_queue.isEmpty():
            v = priority_queue.pop()[1]
            if v == end:
                break
            for node in self.graph.get(v, []):
                gx = distance.get(v, 0) + pathDistance(v, node)
                if gx < distance.get(node, inf):
                    par[node] = v
                    distance[node] = gx
                    fx = distance[node] + self.heuristicsValue(node, end)
                    priority_queue.push((fx, node))

        node = end
        ans = []
        while node != start:
            ans.append(node)
            node = par[node]
        ans.append(start)
        ans.reverse()

        return ans