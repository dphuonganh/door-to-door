from node import Node


class Graph:
    def __init__(self):
        self.node_list = []
        self.path_list = []

    def add_node(self, node):
        self.node_list.append(node)

    def get_all_distance(self, traverse_city):
        """
        This function used to get the distance
        of the selected city to another city
        @return: distance_list with all of city, distance had appended
        """
        distance_list = []
        for i in range(len(traverse_city)):
            city, distance = Node.get_distance(
                                            self.path_list[-1],
                                            traverse_city[i])
            distance_list.append((city, distance))
        return distance_list

    def print_result(self, path, city_distance):
        """
        This function use to print result of program:
        Path from the first city to all of cities
        Total distance after visit all of cities
        """
        for i in range(len(self.path_list)):
            path.append(self.path_list[i].name)
        print(" -> ".join(path))
        print("Total distance: " + str(sum(i for i in city_distance)))

    def find_shortest_path(self):
        """
        This function use Greedy Algorithm to find shortes path of the Graph
        We always find the nearest city with the city selected and go to it
        """
        short_path = []
        city_distance = []
        self.path_list.append(self.node_list[0])
        traverse_city = self.node_list[1:]
        while traverse_city:
            distance_list = self.get_all_distance(traverse_city)
            nearest_city = min(distance_list, key=lambda x: x[1])
            self.path_list.append(nearest_city[0])
            city_distance.append(nearest_city[1])
            traverse_city.remove(nearest_city[0])
        self.print_result(short_path, city_distance)
