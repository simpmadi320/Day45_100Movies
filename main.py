from bs4 import BeautifulSoup
import requests

# https://news.ycombinator.com/
# https://news.ycombinator.com/newest

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

soup_list = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in soup_list]


"""
movie_titles.reverse()
for movie in movie_titles:
    print(movie)
"""

movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
