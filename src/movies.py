import pandas as pd
from pandasql import sqldf
from utils import logger, read_csv, save_to_json


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
        Get the number of unique movies in movies dataframe from the class attribute
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
        Get the average rating of all movies
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
        Get the top 5 highest rated movies
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
        Get the number of movies released each year
        :return: Pandas data frame with number of movies grouped by released year
        """
        method_name = self.get_movies_released_each_year.__name__
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
        Get the number of movies for each genre
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
            ORDER BY movies_count DESC;
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

    def save_to_json_movies_dataset(self,
                                    movies_json: str,
                                    ratings_json: str,
                                    genres_json: str,
                                    unique_movies_json: str,
                                    average_movies_rating_json: str,
                                    top_5_rated_movies_json: str,
                                    movies_released_by_year_json: str,
                                    movies_by_genre_json: str
                                    ) -> None:
        """
        Saving all MoviesDataSet data frames to JSON files
        :param movies_file_json: movies metadata JSON file path
        :param ratings_file_json: movie ratings JSON file path
        :param genres_file_json: movie genres JSON file path
        :param unique_movies_json: unique movies JSON file path
        :param average_movies_rating_json: average movie ratings JSON file path
        :param top_5_rated_movies_json: top 5 rated movies JSON file path
        :param movies_released_by_year_json: movies released by year JSON file path
        :param movies_by_genre_json: movies count by genre JSON file path
        """
        method_name = self.save_to_json_movies_dataset.__name__
        try:
            logger.info(
                f"Calling {self.__class__.__name__} method {method_name}."
            )
            save_to_json(df=self.movies_df, file_path=movies_json)
            save_to_json(df=self.ratings_df, file_path=ratings_json)
            save_to_json(df=self.genres_df, file_path=genres_json)
            save_to_json(df=self.get_unique_movies(), file_path=unique_movies_json)
            save_to_json(df=self.get_average_movie_rating(), file_path=average_movies_rating_json)
            save_to_json(df=self.get_top_5_highest_rated_movies(), file_path=top_5_rated_movies_json)
            save_to_json(df=self.get_movies_released_each_year(), file_path=movies_released_by_year_json)
            save_to_json(df=self.get_movies_count_by_genre(), file_path=movies_by_genre_json)
        except Exception as error:
            error_msg = f"Error occurred in {method_name} method: {error}"
            logger.error(error_msg)
            raise error_msg

        logger.info(f"The {method_name} method finished successfully.")


if __name__ == "__main__":
    movies_metadata_csv = "../movies_dataset/csv/movies_metadata.csv"
    ratings_csv = "../movies_dataset/csv/ratings_small.csv"
    genres_csv = "../movies_dataset/csv/genres.csv"

    movies_metadata_json = "../movies_dataset/json/movies_metadata.json"
    ratings_json = "../movies_dataset/json/ratings.json"
    genres_json = "../movies_dataset/json/genres.json"
    unique_movies_json = "../movies_dataset/json/unique_movies.json"
    average_movies_rating_json = "../movies_dataset/json/average_movies_rating.json"
    top_5_rated_movies_json = "../movies_dataset/json/top_5_rated_movies.json"
    movies_released_by_year_json = "../movies_dataset/json/movies_released_by_year.json"
    movies_by_genre_json = "../movies_dataset/json/movies_by_genre.json"

    print("Instantiating MoviesDataSet")
    my_movie_object = MoviesDataSet(
        movies_file_path=movies_metadata_csv,
        ratings_file_path=ratings_csv,
        genres_file_path=genres_csv
    )
    print("Starting save_to_json_movies_dataset")
    my_movie_object.save_to_json_movies_dataset(
        movies_json=movies_metadata_json,
        ratings_json=ratings_json,
        genres_json=genres_json,
        unique_movies_json=unique_movies_json,
        average_movies_rating_json=average_movies_rating_json,
        top_5_rated_movies_json=top_5_rated_movies_json,
        movies_released_by_year_json=movies_released_by_year_json,
        movies_by_genre_json=movies_by_genre_json
    )
    print("save_to_json_movies_dataset finished")





