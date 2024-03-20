import ast
import pandas as pd
from movies import MoviesDataSet

movies_metadata_file = "../movies_dataset/movies_metadata.csv"
ratings_file = "../movies_dataset/ratings_small.csv"
genres_file = "../movies_dataset/genres.csv"

movies = MoviesDataSet(movies_file_path=movies_metadata_file, ratings_file_path=ratings_file)
movies_df = movies.movies_df
movie_genres_df = pd.DataFrame(
    {
        "id": [],
        "genre_name": []
    }
)

for ind in movies_df.index:
    if movies_df["genres"][ind]:
        # Converting string to a list
        genres_list = ast.literal_eval(movies_df["genres"][ind])
        for genre in genres_list:
            new_row = {
                "id": movies_df["id"][ind],
                "genre_name": genre.get("name")
            }
            movie_genres_df = movie_genres_df.append(new_row, ignore_index=True)

movie_genres_df.to_csv(path_or_buf=genres_file, sep=",", header=True, index=False)
