#!/usr/bin/env python
import math
from sys import argv
from graph import Graph
from node import Node

def read_city_file(G, filename):
    """
    This function use to read input file of user and analysis it
    """
    file = open(filename, "r")
    for line in file:
        line = line.strip()
        name, latitude, longtitude = line.split(", ")
        G.add_node(Node(name, float(latitude), float(longtitude)))


def main():
    """
    Main function: use to implement argument parse and run program
    """
    try:
        G = Graph()
        read_city_file(G, argv[1])
        G.find_shortest_path()
    except Exception:
        print("Invalid file")


if __name__ == "__main__":
    main()
