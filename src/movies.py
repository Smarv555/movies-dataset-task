import numpy as np
import os
import pandas as pd
from pandasql import sqldf


class MoviesDataSet:

    def __init__(self, file_path):
        # Load the movies dataset from a CSV file
        self.movies_df = self.read_csv(file_path)

    def read_csv(self, file_path: str) -> pd.DataFrame:
        """
        Read csv file and return a pandas dataframe
        :param file_path: Input file path
        :return: Pandas dataframe
        """
        try:
            df = pd.read_csv(filepath_or_buffer=file_path, header=0, low_memory=False)
            df = df.convert_dtypes(infer_objects=True)
        except Exception as error:
            raise f"Error occurred in read_csv method: {error}"

        return df

    def get_unique_movies(self) -> pd.DataFrame:
        """
        Get the number of unique movies in movies dataset
        :return: Pandas dataframe with count of unique movies
        """
        try:
            movies_table = self.movies_df
            unique_movies_query = sqldf("SELECT COUNT(DISTINCT id) AS movies_count FROM movies_table")
        except Exception as error:
            raise f"Error occurred in get_unique_movies method: {error}"

        return unique_movies_query

