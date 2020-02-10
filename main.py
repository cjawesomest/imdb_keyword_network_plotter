# Cameron J. Calv HNRS 304
# On the search for connectedness between movie actors/actresses

from imdb_utils import findMovies
from imdb_utils import aggregateInfo

if __name__ == '__main__':
    [mcu_links, mcu_names] = findMovies('Marvel Cinematic Universe')
    # Returns dictionaries convenient for finding cast names, movie names, and unique links for each
    [mcu_link_to_movie, mcu_link_to_cast, mcu_cast_to_name] = aggregateInfo(mcu_links, mcu_names)

    [hsm_links, hsm_names] = findMovies('High School Musical')
    [hsm_link_to_movie, hsm_link_to_cast, hsm_cast_to_name] = aggregateInfo(hsm_links, hsm_names)

    print("Finished")








