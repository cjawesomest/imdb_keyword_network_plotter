# IMDB Performer Network Plotter

Scrapes the Internet Movie DataBase (IMDB) for media content created under a particular searchterm. After scraping for performers from each movie, show, flick, etc, a plot is generated connecting each performer to each other if they share a common production. 

## Initial Results 2020
Plots showcases snapshots of the IMDB taken for a variety of keywords as of March 11th, 2020.
* Plots showcase a network of performers, with connections made between them if they are both present in a single production.
* Each performer (node) is colored based on how many productions that they have appeared in.
* Clustering coefficients show the degree to which all of the nodes of the graph are interconnected. A single node's clustering coefficient is calculated by dividing the number of edges from that node by the total number of nodes.
The full report write-up for this project may be found [here](https://github.com/cjawesomest/imdb_keyword_network_plotter/blob/master/doc/Exploring%20IMDB%20Cinema%20Franchises%20with%20Networks%20Calv.pdf).

| High School Musical | Kingdom Hearts | Legend of Zelda |
|     :---:      |     :---:      |     :---:      |
| ![IMDB HSM](img/High%20School%20Musical%20Plot.png?raw=true "High School Musical Plot") | ![IMDB KH](img/Kingdom%20Hearts%20Plot.png?raw=true "Kingdom Hearts Plot") | ![IMDB LoZ](img/Legend%20of%20Zelda%20Plot.png?raw=true "Legend of Zelda Plot") |
| Lord of the Rings | Mad Max | Marvel Cinematic Universe|
| ![IMDB LotR](img/Lord%20of%20the%20Rings%20Plot.png?raw=true "Lord of the Rings Plot") | ![IMDB MM](img/Mad%20Max%20Plot.png?raw=true "Mad Max Plot") | ![IMDB MCU](img/Marvel%20Cinematic%20Universe%20Plot.png?raw=true "Marvel Cinematic Universe Plot") |
| Mission Impossible | Nintendo | Planet of the Apes |
| ![IMDB MI](img/Mission%20Impossible.png?raw=true "Mission Impossible Plot") | ![IMDB Nintendo](img/Nintendo%20Plot.png?raw=true "Nintendo Plot") | ![IMDB PotA](img/Planet%20of%20the%20Apes%20Plot.png?raw=true "Planet of the Apes Plot") |
| Pokemon | Rocky | Sega |
| ![IMDB Pokemon](img/Pokemon%20Plot.png?raw=true "Pokemon Plot") | ![IMDB Rocky](img/Rocky%20Plot.png?raw=true "Rocky Plot") | ![IMDB Sega](img/Sega%20Plot.png?raw=true "Sega Plot") |
| Star Trek | Stargate | Terminator |
| ![IMDB ST](img/Star%20Trek%20Plot.png?raw=true "Star Trek Plot") | ![IMDB SG](img/Stargate%20Plot.png?raw=true "Stargate Plot") | ![IMDB Terminator](img/Terminator%20Plot.png?raw=true "Terminator Plot") |
| The Muppets | X-Men |   |
| ![IMDB Muppets](img/The%20Muppets%20Plot.png?raw=true "The Muppets Plot") | ![IMDB XM](img/X-Men%20Plot.png?raw=true "X-Men Plot") |  |

## To-Do (Perhaps)
- [ ] Expand upon this awesome project
