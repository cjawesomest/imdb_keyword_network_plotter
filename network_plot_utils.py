# Cameron J. Calv

import networkx as nx
import matplotlib.pyplot as plt
from math import cos, sin, pi, hypot

def plotNetworkGraph(d_movie_to_name, d_movie_to_cast, d_performer_to_name, d_performer_to_movies):
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
    fig = plt.figure()
    nx.draw_networkx_nodes(network_graph, node_positions, cmap=plt.get_cmap('jet'),
                           node_size=50, alpha=1.0)
    nx.draw_networkx_edges(network_graph, node_positions) #, edge_color=edge_values, arrows=False)
    plt.show()
    print('hello')

