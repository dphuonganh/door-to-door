class Node:
        def __init__(self, name, latitude, longtitude):
            self.name = name
            self.latitude = latitude
            self.longtitude = longtitude

        def get_name(self):
            return self.name

        def set_name(self, name):
            self.name = name

        def get_latitude(self):
            return self.latitude

        def set_latitude(self, latitude):
            self.latitude = latitude

        def get_longtitude(self):
            return self.longtitude

        def set_longtitude(self, longtitude):
            self.longtitude = longtitude

        def get_distance(node1, node2):
            """
            This function use to get the distance between two cities
            @return: the city to come and distance to that city
            param node1: first city
            param node2: second city
            """
            return node2, (
                        (node2.latitude - node1.latitude) ** 2 +
                        (node2.longtitude - node1.longtitude) ** 2) ** 0.5
