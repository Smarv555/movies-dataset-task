import pandas as pd
from pandasql import sqldf
from src.utils import (
    logger,
    read_csv,
    save_to_json,
    ConfigParser
)


class MoviesDataSet:
    """
    A class for movies dataset loading and operations
    ...

    Attributes
    ----------
    config : dict
        config dictionary with movies dataset file paths
    movies_df : pr.DataFrame
        Pandas data frame with movies metadata
    ratings_df : pr.DataFrame
        Pandas data frame with movie ratings
    genres_df : pr.DataFrame
        Pandas data frame with movie genres

    Methods
    -------
    get_unique_movies():
        Gets the number of unique movies in movies dataframe from the class attribute
    get_average_movie_rating():
        Gets the average rating of all movies
    get_top_5_highest_rated_movies():
        Gets the top 5 highest rated movies
    get_movies_released_each_year():
        Gets the number of movies released each year
    get_movies_count_by_genre():
        Gets the number of movies for each genre
    save_to_json_movies_dataset():
        Saves all MoviesDataSet data frames to JSON files
    """

    def __init__(self,
                 movies_file_path: str = None,
                 ratings_file_path: str = None,
                 genres_file_path: str = None,
                 test: bool = None
                 ):
        # Set config attribute for the file paths configuration
        env = "test" if test else "main"
        self.config = ConfigParser(env=env)

        # Load the movies dataframe from a CSV file
        self.movies_df = read_csv(movies_file_path if movies_file_path else self.config.movies_metadata_csv)
        # Load the ratings dataframe from a CSV file
        self.ratings_df = read_csv(ratings_file_path if ratings_file_path else self.config.ratings_csv)
        # Load the genres dataframe from a CSV file
        self.genres_df = read_csv(genres_file_path if genres_file_path else self.config.genres_csv)

    def get_unique_movies(self) -> pd.DataFrame:
        """
        Gets the number of unique movies in movies dataframe from the class attribute
        :return: Pandas data frame with count of unique movies
        """
        method_name = self.get_unique_movies.__name__
        movies_table = self.movies_df
        query = """
            SELECT COUNT(DISTINCT id) AS movies_count 
            FROM movies_table;
        """
        try:
            logger.info(
                f"Calling {self.__class__.__name__} method {method_name} with query: {query}"
            )
            df_query_result = sqldf(query)
        except Exception as error:
            error_msg = f"Error occurred in {method_name} method: {error}"
            logger.error(error_msg)
            raise error_msg

        logger.info(f"The {method_name} method finished successfully.")
        return df_query_result

    def get_average_movie_rating(self) -> pd.DataFrame:
        """
        Gets the average rating of all movies
        :return: Pandas data frame with average ratings grouped by movie id
        """
        method_name = self.get_average_movie_rating.__name__
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
            logger.info(
                f"Calling {self.__class__.__name__} method {method_name} with query: {query}"
            )
            df_query_result = sqldf(query)
        except Exception as error:
            error_msg = f"Error occurred in {method_name} method: {error}"
            logger.error(error_msg)
            raise error_msg

        logger.info(f"The {method_name} method finished successfully.")
        return df_query_result

    def get_top_5_highest_rated_movies(self) -> pd.DataFrame:
        """
        Gets the top 5 highest rated movies
        :return: Pandas data frame with the 5 movies with highest average rating
        """
        method_name = self.get_top_5_highest_rated_movies.__name__
        avg_ratings_table = self.get_average_movie_rating()
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
            logger.info(
                f"Calling {self.__class__.__name__} method {method_name} with query: {query}"
            )
            df_query_result = sqldf(query)
        except Exception as error:
            error_msg = f"Error occurred in {method_name} method: {error}"
            logger.error(error_msg)
            raise error_msg

        logger.info(f"The {method_name} method finished successfully.")
        return df_query_result

    def get_movies_released_each_year(self) -> pd.DataFrame:
        """
        Gets the number of movies released each year
        :return: Pandas data frame with number of movies grouped by released year
        """
        method_name = self.get_movies_released_each_year.__name__
        movies_table = self.movies_df
        query = r"""
            SELECT
            STRFTIME('%Y', release_date) AS year,
            COUNT(DISTINCT id) AS movies_released
            FROM movies_table
            WHERE release_date REGEXP '^\d{4}-\d{2}-\d{2}$'
            GROUP BY year
            ORDER BY movies_released DESC, year;
        """
        try:
            logger.info(
                f"Calling {self.__class__.__name__} method {method_name} with query: {query}"
            )
            df_query_result = sqldf(query)
        except Exception as error:
            error_msg = f"Error occurred in {method_name} method: {error}"
            logger.error(error_msg)
            raise error_msg

        logger.info(f"The {method_name} method finished successfully.")
        return df_query_result

    def get_movies_count_by_genre(self) -> pd.DataFrame:
        """
        Gets the number of movies for each genre
        :return: Pandas data frame with the number of movies grouped by genre
        """
        method_name = self.get_movies_count_by_genre.__name__
        movies_table = self.movies_df
        genres_table = self.genres_df
        query = """
            SELECT
            genres_table.genre_name AS genre,
            COUNT(DISTINCT movies_table.id) AS movies_count
            FROM movies_table
            LEFT JOIN genres_table ON movies_table.id = genres_table.id
            GROUP BY genre
            ORDER BY movies_count DESC, genre;
        """
        try:
            logger.info(
                f"Calling {self.__class__.__name__} method {method_name} with query: {query}"
            )
            df_query_result = sqldf(query)
        except Exception as error:
            error_msg = f"Error occurred in {method_name} method: {error}"
            logger.error(error_msg)
            raise error_msg

        logger.info(f"The {method_name} method finished successfully.")
        return df_query_result

    def save_to_json_movies_dataset(self) -> None:
        """
        Saves all MoviesDataSet data frames to JSON files
        """
        method_name = self.save_to_json_movies_dataset.__name__
        try:
            logger.info(
                f"Calling {self.__class__.__name__} method {method_name}."
            )
            save_to_json(df=self.movies_df, file_path=self.config.movies_metadata_json)
            save_to_json(df=self.ratings_df, file_path=self.config.ratings_json)
            save_to_json(df=self.genres_df, file_path=self.config.genres_json)
            save_to_json(df=self.get_unique_movies(), file_path=self.config.unique_movies_json)
            save_to_json(df=self.get_average_movie_rating(), file_path=self.config.average_movies_rating_json)
            save_to_json(df=self.get_top_5_highest_rated_movies(), file_path=self.config.top_5_rated_movies_json)
            save_to_json(df=self.get_movies_released_each_year(), file_path=self.config.movies_released_by_year_json)
            save_to_json(df=self.get_movies_count_by_genre(), file_path=self.config.movies_by_genre_json)
        except Exception as error:
            error_msg = f"Error occurred in {method_name} method: {error}"
            logger.error(error_msg)
            raise error_msg

        logger.info(f"The {method_name} method finished successfully.")
