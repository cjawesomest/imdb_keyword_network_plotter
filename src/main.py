# Cameron J. Calv HNRS 304
# On the search for connectedness between movie actors/actresses
import networkx as nx
import matplotlib.pyplot as plt
import pickle as obj_out
import os.path
from src.imdb_utils import findMovies
from src.imdb_utils import aggregateInfo
from src.network_plot_utils import createNetworkGraph
from datetime import datetime

if __name__ == '__main__':

    output_flag: bool = True
    two_queries_flag: bool = False
    if not two_queries_flag:
        search_term_2 = ''
    import_flag: bool = True
    search_term_1 = 'Marvel Cinematic Universe'
    search_term_2 = 'High School Musical'
    # search_term_1 = 'Star Wars'
    # search_term_2 = 'Lord of the Rings'

    data_name_1 = search_term_1.strip().lower().replace(" ", "")
    if import_flag:
        try:
            with open(os.path.dirname(__file__)+"/../dat/"+data_name_1+".dat", 'rb') as file:
                [link_to_movie_1, link_to_cast_1, performer_to_name_1, performer_to_movies_1, time_1] = obj_out.load(file)
            data_1_exists = True
        except FileNotFoundError:
            data_1_exists = False
    else:
        data_1_exists = False
    if not data_1_exists:
        time_1 = datetime.now()
        [links_1, names_1] = findMovies(search_term_1)
        [link_to_movie_1, link_to_cast_1, performer_to_name_1, performer_to_movies_1] = aggregateInfo(links_1, names_1)
        if output_flag:
            with open(os.path.dirname(__file__)+"/../dat/" + data_name_1 + ".dat", 'wb+') as file:
                obj_out.dump([link_to_movie_1, link_to_cast_1, performer_to_name_1, performer_to_movies_1, time_1], file)
    [graph_1, colors_1] = createNetworkGraph(link_to_movie_1, link_to_cast_1, performer_to_name_1,
                                             performer_to_movies_1)
    acc_1 = nx.average_clustering(graph_1)  # Clustering Coefficient
    coeffs_1 = nx.clustering(graph_1)
    max_cc_1 = 0
    num_nodes_1 = 0
    for performer_node in coeffs_1.keys():
        num_nodes_1 += 1
        if coeffs_1[performer_node] > max_cc_1:
            max_cc_1 = coeffs_1[performer_node]
    if two_queries_flag:
        data_name_2 = search_term_2.strip().lower().replace(" ", "")
        if import_flag:
            try:
                with open(os.path.dirname(__file__)+"/../dat/" + data_name_2 + ".dat", 'rb') as file:
                    [link_to_movie_2, link_to_cast_2, performer_to_name_2, performer_to_movies_2, time_2] = obj_out.load(file)
                data_2_exists = True
            except FileNotFoundError:
                data_2_exists = False
        else:
            data_2_exists = False
        if not data_2_exists:
            time_2 = datetime.now()
            [links_2, names_2] = findMovies(search_term_2)
            [link_to_movie_2, link_to_cast_2, performer_to_name_2, performer_to_movies_2] = aggregateInfo(
                links_2, names_2)
            if output_flag:
                with open(os.path.dirname(__file__)+"/../dat/" + data_name_2 + ".dat", 'wb+') as file:
                    obj_out.dump([link_to_movie_2, link_to_cast_2, performer_to_name_2, performer_to_movies_2, time_2],
                                 file)
        [graph_2, colors_2] = createNetworkGraph(link_to_movie_2, link_to_cast_2, performer_to_name_2,
                                                 performer_to_movies_2)
        acc_2 = nx.average_clustering(graph_2)  # Clustering Coefficient
        coeffs_2 = nx.clustering(graph_2)
        max_cc_2 = 0
        num_nodes_2 = 0
        for performer_node in coeffs_2.keys():
            num_nodes_2 += 1
            if coeffs_2[performer_node] > max_cc_2:
                max_cc_2 = coeffs_2[performer_node]

    # Plot the data

    colormap = plt.cm.get_cmap('plasma')
    fig = plt.figure()
    if two_queries_flag:
        ax = fig.add_subplot(1, 2, 1)
    else:
        ax = fig.add_subplot(1, 1, 1)
    ax.set_aspect('equal', adjustable='box')
    nx.draw_kamada_kawai(graph_1, node_size=10, with_labels=False, font_weight='bold', arrows=False,
                         cmap=colormap, node_color=colors_1)
    ax.set_title(search_term_1)
    props_1 = '\n'.join(("Avg Cluster Coeff: " + str(round(acc_1,3)),
                           "Max Cluster Coeff: " + str(round(max_cc_1,3)),
                           "Num Nodes: " + str(num_nodes_1)))
    if not two_queries_flag:
        ax.annotate(props_1, xy=(0.05, -0.1), xycoords=("data", "axes fraction"), va='bottom', ha='center',
                  bbox=dict(boxstyle='round4', facecolor='orange', alpha=0.8))
    else:
        ax.annotate(props_1, xy=(0.05, -0.3), xycoords=("data", "axes fraction"), va='bottom', ha='center',
                    bbox=dict(boxstyle='round4', facecolor='orange', alpha=0.8))
    sm = plt.cm.ScalarMappable(cmap=colormap, norm=plt.Normalize(vmin=min(colors_1), vmax=max(colors_1)))
    sm.set_array([])
    cbar = plt.colorbar(sm, shrink=0.75)
    cbar.ax.set_ylabel('# of Appearances')

    if two_queries_flag:
        ax = fig.add_subplot(1, 2, 2)
        nx.draw_kamada_kawai(graph_2, node_size=10, with_labels=False, font_weight='bold',  arrows=False,
                             cmap=colormap, node_color=colors_2)
        ax.set_aspect('equal', adjustable='box')
        ax.set_title(search_term_2)
        props_2 = '\n'.join(("Avg Cluster Coeff: "+str(round(acc_2, 3)),
                               "Max Cluster Coeff: "+str(round(max_cc_2, 3)),
                               "Num Nodes: "+str(num_nodes_2)))
        ax.annotate(props_2, xy=(0.05, -0.3), xycoords=("data", "axes fraction"), va='bottom', ha='center',
                    bbox=dict(boxstyle='round4', facecolor='orange', alpha=0.8))
        # plt.gcf().text(0.05, 0.05, props_2, transform=ax.transAxes, va='bottom', ha='left', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        sm = plt.cm.ScalarMappable(cmap=colormap, norm=plt.Normalize(vmin=min(colors_2), vmax=max(colors_2)))
        sm.set_array([])
        cbar = plt.colorbar(sm, shrink=0.75)
        cbar.ax.set_ylabel('# of Appearances')
    plt.show()

    print("Finished")








