# Cameron J. Calv

import networkx as nx
import matplotlib.pyplot as plt
from math import cos, sin, pi, hypot

def createNetworkGraph(d_movie_to_name, d_movie_to_cast, d_performer_to_name, d_performer_to_movies):
    num_performers = len(d_performer_to_name.keys())
    network_graph = nx.DiGraph()
    node_positions = {}
    for movie in d_movie_to_cast.keys():
        idx = 0
        for performer in d_movie_to_cast[movie]:
            for co_performer in d_movie_to_cast[movie][idx+1:]:
                network_graph.add_edge(performer, co_performer)
            idx += 1
    idx = 0
    for performer in d_performer_to_name.keys():
        node_positions[performer] = [10000*cos(idx*(2*pi)/(num_performers)), 10000*sin(idx*(2*pi)/(num_performers))]
        idx += 1

    performer_appearances = []
    for node in network_graph.nodes:
        performer_appearances.append(len(d_performer_to_movies[node]))

    return network_graph, performer_appearances

