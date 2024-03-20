import ast
import pandas as pd
from pandasql import sqldf


def read_csv(file_path: str) -> pd.DataFrame:
    """
    Read csv file and return a pandas data frame
    :param file_path: Input file path
    :return: Pandas data frame
    """
    try:
        df = pd.read_csv(filepath_or_buffer=file_path, header=0, low_memory=False)
        df = df.convert_dtypes(infer_objects=True)
    except Exception as error:
        raise f"Error occurred in read_csv function: {error}"

    return df


class MoviesDataSet:

    def __init__(self, movies_file_path: str, ratings_file_path: str, genres_file_path: str):
        # Load the movies dataframe from a CSV file
        self.movies_df = read_csv(movies_file_path)
        # Load the ratings dataframe from a CSV file
        self.ratings_df = read_csv(ratings_file_path)
        # Load the genres dataframe from a CSV file
        self.genres_df = read_csv(genres_file_path)

    def get_unique_movies(self) -> pd.DataFrame:
        """
        Get the number of unique movies in movies dataset
        :return: Pandas data frame with count of unique movies
        """
        movies_table = self.movies_df
        query = """
            SELECT COUNT(DISTINCT id) AS movies_count 
            FROM movies_table;
        """
        try:
            df_query_result = sqldf(query)
        except Exception as error:
            raise f"Error occurred in get_unique_movies method: {error}"

        return df_query_result

    def get_avarage_movie_rating(self) -> pd.DataFrame:
        """
        Get the average rating of all movies
        :return: Pandas data frame with average ratings grouped by movie id
        """
        movies_table = self.movies_df
        ratings_table = self.ratings_df
        query = """
            SELECT 
            ratings_table.movieId AS id, 
            movies_table.original_title AS title, 
            AVG(ratings_table.rating) AS average_rating
            FROM ratings_table
            INNER JOIN movies_table ON ratings_table.movieId = movies_table.id
            GROUP BY id;
        """
        try:
            df_query_result = sqldf(query)
        except Exception as error:
            raise f"Error occurred in get_average_movie_rating method: {error}"

        return df_query_result

    def get_top_5_highest_rated_movies(self):
        avg_ratings_table = self.get_avarage_movie_rating()
        query = """
            SELECT 
            id, 
            title, 
            average_rating
            FROM avg_ratings_table
            ORDER BY average_rating DESC
            LIMIT 5;
        """
        try:
            df_query_result = sqldf(query)
        except Exception as error:
            raise f"Error occurred in get_average_movie_rating method: {error}"

        return df_query_result

    def get_movies_released_each_year(self) -> pd.DataFrame:
        """
        Get the number of movies released each year
        :return: Pandas data frame with number of movies grouped by released year
        """
        movies_table = self.movies_df
        query = """
            SELECT
            STRFTIME('%Y', release_date) AS year,
            COUNT(id) AS movies_released
            FROM movies_table
            WHERE release_date REGEXP '^\d{4}-\d{2}-\d{2}$'
            GROUP BY year
            ORDER BY movies_released DESC;
        """
        try:
            df_query_result = sqldf(query)
        except Exception as error:
            raise f"Error occurred in get_movies_released_each_year method: {error}"

        return df_query_result

    def get_movies_count_by_genre(self) -> pd.DataFrame:
        """
        Get the number of movies for each genre
        :return: Pandas data frame with the number of movies grouped by genre
        """
        movies_table = self.movies_df
        genres_table = self.genres_df
        query = """
            SELECT
            genres_table.genre_name AS genre,
            COUNT(DISTINCT movies_table.id) AS movies_count
            FROM movies_table
            LEFT JOIN genres_table ON movies_table.id = genres_table.id
            GROUP BY genre
            ORDER BY movies_count DESC;
        """
        try:
            df_query_result = sqldf(query)
        except Exception as error:
            raise f"Error occurred in get_movies_count_by_genre method: {error}"

        return df_query_result


if __name__ == "__main__":
    movies_metadata_file = "../movies_dataset/movies_metadata.csv"
    ratings_file = "../movies_dataset/ratings_small.csv"
    genres_file = "../movies_dataset/genres.csv"

    my_movie_object = MoviesDataSet(
        movies_file_path=movies_metadata_file,
        ratings_file_path=ratings_file,
        genres_file_path=genres_file
    )
    df = my_movie_object.movies_df
    # print(df.dtypes)
    print(my_movie_object.get_top_5_highest_rated_movies())
    # print(df["release_date"].sort_values(ascending=True))
    # print(my_movie_object.movies_df["release_date"])
    # print(my_movie_object.get_movies_released_each_year())


