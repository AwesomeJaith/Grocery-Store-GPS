import json
from rich import print
from rich.console import Console
from rich.table import Table
import networkx as nx
from networkx.algorithms.approximation import *
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import os

class Map:
    # Take a json file and process it
    def __init__(self, store_json):
        self.store_data = store_json
        self.nodes = []
        self.names = []
        self.coordinates = []
        self.edges = []
        self.locations = []
        self.G = nx.Graph()
        self._load_data()
        self._load_graph()

    def display_table(self):
        console = Console()
        table = Table(show_header=True, header_style="bold")
        table.add_column("Node Number")
        table.add_column("Node Name")
        table.add_column("Node Coordinates")

        coordinates_string = []
        for coordinate in self.coordinates:
            coordinates_string.append(f"({coordinate[0]}, {coordinate[1]})")

        for node, name, coordinate in zip(self.nodes, self.names, coordinates_string):
            table.add_row(str(node), name, coordinate)

        console.print(table)

    def display_edges(self):
        console = Console()
        table = Table(show_header=True, header_style="bold")
        table.add_column("Node 1")
        table.add_column("Node 2")
        table.add_column("Edge Weight")

        for edge in self.edges:
            node1 = str(edge[0])
            node2 = str(edge[1])
            weight = str(edge[2]['weight'])
            table.add_row(node1, node2, weight)

        console.print(table)

    def display_graph(self):
        G = self.G
        nx.draw(G, nx.kamada_kawai_layout(G), with_labels=True, labels={node: data['label'] for node, data in G.nodes(data=True)}, node_size=100, font_size=8)
        plt.show()

    def find_product_location(self, product_name):
        # Possibly categorize locations by department in the future. Something to explore.
        return self.locations[0][product_name]

    def find_optimal_path(self, grocery_list):
        required_nodes = self._get_required_nodes(grocery_list)

        tsp = nx.approximation.traveling_salesman_problem
        optimal_path = tsp(self.G, nodes=required_nodes)
        total_weight = sum(self.G[u][v]['weight'] for u, v in zip(optimal_path, optimal_path[1:]))

        return optimal_path

    def draw_path_png(self, path, directory=""):
        store_map = Image.open("store_map.png")
        draw = ImageDraw.Draw(store_map)

        print(path)
        # Draw the optimal path
        polyline_1 = []
        for node_id in path:
            polyline_1.append(self.coordinates[node_id - 1])

        polyline_tuple = [tuple(coord) for coord in polyline_1]

        print(polyline_tuple)
        draw.line(polyline_tuple, fill="blue", width=10)

        # Draw each coordinate in the path
        for coordinate in polyline_tuple:
            dot_color = (255, 0, 0)
            dot_radius = 5
            x, y = coordinate[0], coordinate[1]
            draw.ellipse((x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius),fill=dot_color,outline=dot_color,)

        image_path = os.path.join(directory, "temp_store_map_path.png")
        store_map.save(image_path)
        return image_path

    # change this later to adapt to different entrance/checkout/exit option
    def _get_required_nodes(self, grocery_list):
        required_nodes = [1, 131]
        for item in grocery_list:
            product_node = self.find_product_location(item)
            if product_node is not None:
                if product_node not in required_nodes:
                    required_nodes.append(product_node)
            else:
                return -1
        return required_nodes

    # Extract store data from input json file
    def _load_data(self):
        dir = os.path.dirname(__file__)
        json_file_path = os.path.join(dir, self.store_data)
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        self.nodes = data['nodes']
        self.names = data['names']
        self.coordinates = data['coordinates']
        self.edges = [(item["node_1"], item["node_2"], {"weight": item["weight"]}) for item in data['edges']]
        self.locations = data['product_locations']

    def _load_graph(self):
        for node, name in zip(self.nodes, self.names):
            self.G.add_node(node, label=name)

        self.G.add_edges_from(self.edges)