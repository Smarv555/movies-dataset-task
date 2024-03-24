import os
import ast
import json
import logging
import pandas as pd

# Logger setup
logger = logging.getLogger()
logging.basicConfig(
    filename="movies_dataset_logs.log", format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG
)


def read_csv(file_path: str) -> pd.DataFrame:
    """
    Read csv file and return a pandas data frame
    :param file_path: Input file path
    :return: Pandas data frame
    """
    function_name = read_csv.__name__
    try:
        logger.info(
            f"Calling function {function_name} on file {file_path}."
        )
        df = pd.read_csv(filepath_or_buffer=file_path, header=0, low_memory=False)
    except Exception as error:
        error_msg = f"Error occurred in {function_name} function: {error}"
        logger.error(error_msg)
        raise error_msg

    logger.info(
        f"The {function_name} function finished successfully. Data frame created from CSV file: {file_path}"
    )
    return df


def save_to_json(df: pd.DataFrame, file_path: str) -> None:
    """
    Saving Pandas data frame to a JSON file
    :param df: Pandas data frame to be saved
    :param file_path: JSON file path where the data frame will be saved
    """
    function_name = save_to_json.__name__
    try:
        logger.info(
            f"Calling function {function_name} on file {file_path}."
        )
        df.to_json(path_or_buf=file_path, indent=4, orient="table", index=False)
    except Exception as error:
        error_msg = f"Error occurred in {function_name} function: {error}"
        logger.error(error_msg)
        raise error_msg

    logger.info(
        f"The {function_name} function finished successfully. Data frame saved to JSON file: {file_path}"
    )


def save_to_csv(df: pd.DataFrame, file_path: str) -> None:
    """
    Saving Pandas data frame to a CSV file
    :param df: Pandas data frame to be saved
    :param file_path: CSV file path where the data frame will be saved
    """
    function_name = save_to_json.__name__
    try:
        logger.info(
            f"Calling function {function_name} on file {file_path}."
        )
        df.to_csv(path_or_buf=file_path, sep=",", header=True, index=False)
    except Exception as error:
        error_msg = f"Error occurred in {function_name} function: {error}"
        logger.error(error_msg)
        raise error_msg

    logger.info(
        f"The {function_name} function finished successfully. Data frame saved to CSV file: {file_path}"
    )


def generate_genres_df(test: bool = False) -> None:
    """
    Generates a new genre data frame grouped by movie id and saves it to a CSV file
    :param test: Boolean value, False by default. If true the test_dataset location will be used instead of movies_dataset
    """
    env = "test" if test else "main"
    config_parser = ConfigParser(env=env)
    movies_df = read_csv(config_parser.movies_metadata_csv)
    # Creating empty df for the new genres table
    movie_genres_df = pd.DataFrame(
        {
            "id": [],
            "genre_name": []
        }
    )

    # Looping through the movies metadata rows
    for i in movies_df.index:
        if movies_df["genres"][i]:
            # Converting string to a list
            genres_list = ast.literal_eval(movies_df["genres"][i])
            # Looping through the genres dictionaries in the list
            for genre in genres_list:
                new_row = {
                    "id": movies_df["id"][i],
                    "genre_name": genre.get("name")
                }
                # Adding the new row with movie id and genre name to the genres df
                movie_genres_df = movie_genres_df.append(new_row, ignore_index=True)

    # Saving the new genres df as CSV
    save_to_csv(df=movie_genres_df, file_path=config_parser.genres_csv)


def generate_test_df() -> None:
    """
    Generating test datasets for the unit tests
    """
    config_parser = ConfigParser(env="test")
    movies_metadata_test_csv = config_parser.movies_metadata_csv
    ratings_test_csv = config_parser.ratings_csv

    movies_test_data = {
        "id": [1, 2, 3, 4, 5, 6, 7, 1, 2],
        "original_title": ["title1", "title2", "title3", "title4", "title5", "title6", "title7", "title1", "title2"],
        "genres": [
            "[{'name': 'genre1'}]",
            "[{'name': 'genre2'}]",
            "[{'name': 'genre1'}, {'name': 'genre2'}]",
            "[{'name': 'genre1'}, {'name': 'genre3'}]",
            "[{'name': 'genre5'}]",
            "[]",
            "[]",
            "[]",
            "[]"
        ],
        "release_date": [
            "1995-01-01",
            "1995-02-01",
            "1995-03-01",
            "2000-04-01",
            "2010-05-01",
            "1995-06",
            "",
            "",
            ""
        ]
    }

    ratings_test_data = {
        "movieId": [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7],
        "rating": [2.0, 5.0, 5.0, 2.0, 3.0, 1.0, 1.0, 4.0, 4.0, 1.0, 1.0, 1.0, 5.0, 5.0, 5.0, 5.0, 3.0]
    }

    movies_test_df = pd.DataFrame(data=movies_test_data)
    save_to_csv(movies_test_df, file_path=movies_metadata_test_csv)

    ratings_test_df = pd.DataFrame(data=ratings_test_data)
    save_to_csv(ratings_test_df, file_path=ratings_test_csv)


class ConfigParser:
    """
    A class for movies dataset configuration parser
    ...

    Attributes
    ----------
    config_json : dict
        config dictionary with movies dataset file paths
    movies_metadata_csv : str
        movies metadata csv file path
    ratings_csv : str
        movie ratings csv file path
    genres_csv : str
        movie genres csv file path
    movies_metadata_json : str
        movies metadata json file path
    ratings_json : str
        movie ratings json file path
    genres_json : str
        movie genres json file path
    unique_movies_json : str
        unique movies json file path
    average_movies_rating_json : str
        average movie ratings json file path
    top_5_rated_movies_json : str
        top 5 highest rated movies json file path
    movies_released_by_year_json : str
        count of movies released by year json file path
    movies_by_genre_json : str
        count of movies by genre json file path

    Methods
    -------
    read_config_file():
        Read the config.json file
    """

    def __init__(self, env):
        # Read config file
        self.config_json = self.read_config_file(env)
        # Set config parser attributes
        self.movies_metadata_csv = os.path.abspath(self.config_json["csv"]["movies_metadata_csv"])
        self.ratings_csv = os.path.abspath(self.config_json["csv"]["ratings_csv"])
        self.genres_csv = os.path.abspath(self.config_json["csv"]["genres_csv"])
        self.movies_metadata_json = os.path.abspath(self.config_json["json"]["movies_metadata_json"])
        self.ratings_json = os.path.abspath(self.config_json["json"]["ratings_json"])
        self.genres_json = os.path.abspath(self.config_json["json"]["genres_json"])
        self.unique_movies_json = os.path.abspath(self.config_json["json"]["unique_movies_json"])
        self.average_movies_rating_json = os.path.abspath(self.config_json["json"]["average_movies_rating_json"])
        self.top_5_rated_movies_json = os.path.abspath(self.config_json["json"]["top_5_rated_movies_json"])
        self.movies_released_by_year_json = os.path.abspath(self.config_json["json"]["movies_released_by_year_json"])
        self.movies_by_genre_json = os.path.abspath(self.config_json["json"]["movies_by_genre_json"])

    def read_config_file(self, env) -> dict:
        """
        Read the config.json file
        :param env: A string indicating which config file to be used. It could be either 'main' or 'test'.
        :return: JSON file with configuration
        """
        try:
            config_file_path = os.path.join(
                os.path.dirname(__file__),
                "..",
                "config",
                f"config-{env}.json"
            )
            with open(config_file_path, "r", encoding="utf-8") as config_file:
                config_json = json.load(config_file)
        except Exception as error:
            error_msg = f"Error occurred in {self.read_config_file.__name__} method: {error}"
            logger.error(error_msg)
            raise error_msg

        return config_json
