# Cameron J. Calv HNRS 304
# On the search for connectedness between movie actors/actresses

from imdb_utils import findMovies
from imdb_utils import aggregateInfo
from network_plot_utils import plotNetworkGraph

if __name__ == '__main__':
    [mcu_links, mcu_names] = findMovies('Marvel Cinematic Universe')
    # Returns dictionaries convenient for finding cast names, movie names, and unique links for each
    [mcu_link_to_movie, mcu_link_to_cast, mcu_performer_to_name, mcu_performer_to_movies] = aggregateInfo(mcu_links, mcu_names)
    plotNetworkGraph(mcu_link_to_movie, mcu_link_to_cast, mcu_performer_to_name, mcu_performer_to_movies)


    # [hsm_links, hsm_names] = findMovies('High School Musical')
    # [hsm_link_to_movie, hsm_link_to_cast, hsm_performer_to_name, hsm_performer_to_movies] = aggregateInfo(hsm_links, hsm_names)
    # plotNetworkGraph(hsm_link_to_movie, hsm_link_to_cast, hsm_performer_to_name, hsm_performer_to_movies)


    print("Finished")








