# this program picks the random movies from the most popular movies in Imbd charts
import random
import requests
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/moviemeter?pf_rd_m=A2FGELUUNOQJNL&\
       pf_rd_p=cb6cf75a-1a51-49d1-af63-8202cfc3fb01&pf_rd_r=QKD7051N\
       5SWMFFW2V56N&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter\
       &ref_=chtmvm_ql_2"

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")


all_movies = soup.find_all("td", class_="titleColumn")
list_random_movie = []

for movie_info in all_movies:
    movie_name = movie_info.find("a").text
    movie_year = movie_info.find("span", class_="secondaryInfo").text
    # it doesn't look good with parenthesis
    movie_year = movie_year.replace("(", "").replace(")", "")
    list_random_movie.append((movie_name, movie_year))


random_movie = random.choice(list_random_movie)
print(random_movie)
