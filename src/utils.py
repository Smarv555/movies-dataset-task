import ast
import logging
import pandas as pd

# Logger setup
logger = logging.getLogger()
logging.basicConfig(
    filename="movies_dataset_logs.log", format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG
)

movies_metadata_file = "../movies_dataset/csv/movies_metadata.csv"
ratings_file = "../movies_dataset/csv/ratings_small.csv"
genres_file = "../movies_dataset/csv/genres.csv"


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
        df = df.convert_dtypes(infer_objects=True)
    except Exception as error:
        error_msg = f"Error occurred in {function_name} function: {error}"
        logger.error(error_msg)
        raise error_msg

    logger.info(
        f"The {function_name} method finished successfully. Data frame created from CSV file: {file_path}"
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
        df.to_json(path_or_buf=file_path, indent=4)
    except Exception as error:
        error_msg = f"Error occurred in {function_name} function: {error}"
        logger.error(error_msg)
        raise error_msg

    logger.info(
        f"The {function_name} method finished successfully. Data frame saved to JSON file: {file_path}"
    )


def generate_genres_df(file_path: str) -> None:
    """

    :return:
    """
    movies_df = read_csv(movies_metadata_file)
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

    movie_genres_df.to_csv(path_or_buf=file_path, sep=",", header=True, index=False)


class ConfigParser:
    pass
