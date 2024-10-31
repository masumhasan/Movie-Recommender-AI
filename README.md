# Movie-Recommender-AI
masumhasan: Update the readme file based on my code 

Workspace: Sure, here is an updated version of your 

README.md

 file based on the provided code excerpts from 

recommender.ipynb

:

```markdown
# Movie-Recommender-AI

Machine Learning Project of end-to-end movie recommender system building.

## Overview

This project builds a movie recommender system using data from the TMDB 5000 dataset. The dataset includes information about movies, such as genres, cast, crew, and keywords.

## Data

The project uses two CSV files:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

## Preprocessing

The preprocessing steps include:
1. Merging the movies and credits datasets on the `title` column.
2. Dropping missing data.
3. Converting string representations of lists (e.g., genres, cast, crew) into actual lists using helper functions like `converttoL` and `convertcast`.
4. Extracting specific roles (e.g., Director) from the crew data using the `fDirector` function.
5. Splitting the overview text into words.

## Helper Functions

- `converttoL(obj)`: Converts a string representation of a list into an actual list.
- `convertcast(obj)`: Extracts the names of up to 4 cast members from a string representation of a list.
- `fDirector(obj)`: Extracts the name of the director from the crew data.

## Example Usage

```python
import pandas as pd
import ast

# Load data
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# Merge datasets
movies = movies.merge(credits, on='title')

# Drop missing data
movies.dropna(inplace=True)

# Convert genres, keywords, cast, and crew to lists
movies['genres'] = movies['genres'].apply(converttoL)
movies['keywords'] = movies['keywords'].apply(converttoL)
movies['cast'] = movies['cast'].apply(convertcast)
movies['crew'] = movies['crew'].apply(fDirector)

# Split overview into words
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Display the first movie
print(movies.head(1))
```

## Requirements

- Python 3.10.8
- pandas
- numpy

## Running the Project

To run the project, execute the cells in the `recommender.ipynb` Jupyter notebook.

## License

This project is licensed under the MIT License.
```