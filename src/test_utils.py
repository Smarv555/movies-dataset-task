import pandas as pd
from pandas.testing import assert_frame_equal
from src.utils import ConfigParser, read_csv, save_to_json

config = ConfigParser(env="test")


def test_read_csv():
    """
    Testing the read_csv function from utils module
    """
    expected_data = {
        "movieId": [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7],
        "rating": [2.0, 5.0, 5.0, 2.0, 3.0, 1.0, 1.0, 4.0, 4.0, 1.0, 1.0, 1.0, 5.0, 5.0, 5.0, 5.0, 3.0]
    }

    expected_df = pd.DataFrame(data=expected_data, dtype="Int64")
    actual_df = read_csv(file_path=config.ratings_csv)

    assert_frame_equal(expected_df, actual_df)


def test_save_to_json():
    """
    Testing the save_to_json function from utils module
    """
    expected_data = {
        "movieId": [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7],
        "rating": [2.0, 5.0, 5.0, 2.0, 3.0, 1.0, 1.0, 4.0, 4.0, 1.0, 1.0, 1.0, 5.0, 5.0, 5.0, 5.0, 3.0]
    }

    expected_df = pd.DataFrame(data=expected_data, dtype="Int64")
    actual_df = read_csv(file_path=config.ratings_csv)

    assert_frame_equal(expected_df, actual_df)