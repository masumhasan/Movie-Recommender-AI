import requests
import csv

# API key for TMDB
api_key = "05f24270b79f2c782124c1ec4c01fc55"

# base URL for API requests
base_url = "https://api.themoviedb.org/3"

# function to get movie credits


def get_credits(movie_id):
    credits_url = f"{base_url}/movie/{movie_id}/credits?api_key={api_key}"
    response = requests.get(credits_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# function to get movie details


def get_movie(movie_id):
    movie_url = f"{base_url}/movie/{movie_id}?api_key={api_key}"
    response = requests.get(movie_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


# number of movies to scrape
num_movies = 100000

# list to store movie data
movies_data = []

# loop through movie IDs and scrape data
for movie_id in range(1, num_movies+1):
    credits_data = get_credits(movie_id)
    movie_data = get_movie(movie_id)
    # check if both movie and credits data are available
    if credits_data is not None and movie_data is not None:
        # extract relevant movie and credits data
        movie = {
            "budget": movie_data["budget"],
            "genres": "|".join([genre["name"] for genre in movie_data["genres"]]),
            "homepage": movie_data["homepage"],
            "id": movie_data["id"],
            "keywords": "|".join([keyword["name"] for keyword in movie_data.get("keywords", [])]),
            "original_language": movie_data["original_language"],
            "original_title": movie_data["original_title"],
            "overview": movie_data["overview"],
            "popularity": movie_data["popularity"],
            "production_companies": "|".join([company["name"] for company in movie_data["production_companies"]]),
            "production_countries": "|".join([country["name"] for country in movie_data["production_countries"]]),
            "release_date": movie_data["release_date"],
            "revenue": movie_data["revenue"],
            "runtime": movie_data["runtime"],
            "spoken_languages": "|".join([language["name"] for language in movie_data["spoken_languages"]]),
            "status": movie_data["status"],
            "tagline": movie_data["tagline"],
            "title": movie_data["title"],
            "vote_average": movie_data["vote_average"],
            "vote_count": movie_data["vote_count"],
            "cast": "|".join([cast_member["name"] for cast_member in credits_data["cast"]]),
            "crew": "|".join([crew_member["name"] for crew_member in credits_data["crew"]])
        }
        # append movie data to list
        movies_data.append(movie)
    # print progress message
    if movie_id % 1000 == 0:
        print(f"{movie_id} movies scraped")

# create movies.csv file
with open("movies.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=credits_data[0].keys())
    writer.writeheader()
    writer.writerows(movies_data)

# create credits.csv file
credits_data = [{"movie_id": movie["id"], "title": movie["title"], "cast": "|".join([cast_member["name"] for cast_member in movie["credits"]["cast"]]), "crew": "|".join([
    crew_member["name"] for crew_member in movie["credits"]["crew"]])} for movie in movies_data]

with open("credits.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=credits_data[0].keys())
    writer.writeheader()
    writer.writerows(credits_data)

print("Scraping complete")
