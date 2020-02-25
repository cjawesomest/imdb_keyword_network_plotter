# Cameron J. Calv

# A collection of functions whose purpose it is to scrape the IMDB website for information
# on various movies and performers

from lxml import etree
from io import StringIO
import requests  # Used to make HTTP requests

def getCast(movieURL):
    baseURL = 'https://www.imdb.com'
    htmlList = getHTMLAsList(baseURL+movieURL)
    # Find the featured cast on the front page
    performerNames = []
    performerLinks = []
    within_cast_list = 0
    found_photo = 0
    for row in htmlList:
        if within_cast_list and found_photo:
            if 'href=' in row:
                split_line = row.split("\"");
                link = split_line[1]
                name = split_line[7]
                if '&#' in name and ';' in name:
                    name = name.replace(name[name.find('&#'): name.find(';') + 1],
                                   chr(int(name[name.find('&#') + len('&#'): name.find(';')])))
                if not link in performerLinks:
                    performerNames.append(name)
                    performerLinks.append(link)
                # print(name+" @ "+link)
                # print(row.split("\""))
                found_photo = 0
        elif within_cast_list:
            if 'primary_photo' in row:
                found_photo = 1
        else:
            if 'cast_list' in row:
                within_cast_list = 1

    # Find the entire credited cast list (In case I need it later)
    # fullCastListPage = getHTMLAsList(baseURL+movieURL+'fullcredits')

    return performerLinks, performerNames

def getHTMLAsList(nextURL):
    print("Requesting page: "+nextURL+"...")
    siteRequest = requests.get(nextURL)
    webpage = siteRequest.text
    htmlParser = etree.HTMLParser()
    pageTree = etree.parse(StringIO(webpage), htmlParser)
    htmlBytes = etree.tostring(pageTree.getroot(), pretty_print=True, method="html")
    htmlString = htmlBytes.decode("utf-8")
    htmlList = htmlString.split('\n')
    return htmlList


def findMovies(searchTerm):
    print("Initiating search for all movies \""+searchTerm+"\"...")
    baseURL = 'https://www.imdb.com/search/keyword/'
    movieListLinks = []
    keyword = '?keywords='
    for word in searchTerm.split():
        keyword = keyword + word.lower() + '-'
    keyword = keyword[0:-1]
    search_another_page = 1
    # Using the keyword provided, find all of the pages that contain movies under this keyword
    while search_another_page:
        search_another_page = 0
        nextURL = baseURL + keyword

        htmlList = getHTMLAsList(nextURL)

        next_page_delim = 'lister-page-next'
        prev_page_delim = 'lister-page-prev'

        found_link = 0
        for row in htmlList:
            if next_page_delim in row or prev_page_delim in row:
                for piece in row.split('\"'):
                    if found_link:
                        if not piece in movieListLinks:
                            movieListLinks.append(piece)
                            # print(piece)
                            keyword = piece
                            search_another_page = 1
                        found_link = 0
                    if "href=" in piece:
                        found_link = 1
    only_one_page = 0
    if not movieListLinks:
        movieListLinks.append(nextURL)
        only_one_page = 1
    # Now that we have the pages, go through each one and get the movie name and links to the movie
    # web pages.
    count_movies = 0
    movieLinks = []
    movieNames = []
    for moviePage in movieListLinks:
        if only_one_page:
            htmlList = getHTMLAsList(moviePage)
        else:
            htmlList = getHTMLAsList(baseURL + moviePage)
        found_movie = 0
        idx = 0
        for line in htmlList:
            # print(line)
            if 'lister-item-header' in line:
                found_movie = 1
            if found_movie and 'href=' in line:
                split_line = line.split('\"')
                movie_link = split_line[1]
                movie_name = split_line[2].split('<')[0][1:]
                # print(split_line[1])
                # print(split_line[2].split('<')[0][1:])
                if '&amp;' in movie_name:
                    movie_name = movie_name.replace('&amp;', '&')
                if not movie_link in movieLinks and not movie_name in movieNames:
                    movieLinks.append(movie_link)
                    movieNames.append(movie_name)
                    count_movies += 1
                found_movie = 0
            idx += 1
    return movieLinks, movieNames

def getCastAppearances(performer_to_name, link_to_cast_dict, link_to_movie_dict):
    performer_to_movies = dict()
    for performer in performer_to_name.keys():
        # dictionary key: dict(performer_link) = [list of movies]
        print(performer_to_name[performer]+" has appeared in...")
        performer_to_movies[performer] = []
        for movie in link_to_cast_dict.keys():
            for cast_member in link_to_cast_dict[movie]:
                if cast_member == performer:
                    print("\t-"+link_to_movie_dict[movie])
                    performer_to_movies[performer].append(link_to_movie_dict[movie])
    return performer_to_movies

def aggregateInfo(links, names):
    movieLinkToMovieNameDict = dict()
    movieLinkToMovieCastDict = dict()
    castLinkToCastNameDict = dict()
    cast_num = 0
    for idx in range(len(links)):
        if links[idx] in movieLinkToMovieNameDict.keys():
            print("Found a duplicate flick : " + names[idx])
            print("Omitting from total list")
        else:
            movieLinkToMovieNameDict[links[idx]] = names[idx]
        [castLinks, castNames] = getCast(links[idx])
        movieLinkToMovieCastDict[links[idx]] = castLinks
        per_idx = 0
        for performer_link in castLinks:
            if performer_link in castLinkToCastNameDict.keys():
                print("Found a duplicate performer : " + castLinkToCastNameDict[performer_link])
            else:
                cast_num += 1
                castLinkToCastNameDict[performer_link] = castNames[per_idx]
            per_idx += 1
    castLinkToMovieNames = getCastAppearances(castLinkToCastNameDict, movieLinkToMovieCastDict, movieLinkToMovieNameDict)
    return movieLinkToMovieNameDict, movieLinkToMovieCastDict, castLinkToCastNameDict, castLinkToMovieNames
