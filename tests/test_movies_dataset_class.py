import pandas as pd
from pandas.testing import assert_frame_equal
from src.movies_dataset_class import MoviesDataSet

test_movies_dataset_object = MoviesDataSet(test=True)


def test_get_unique_movies():
    """
    Testing the get_unique_movies method from MoviesDataSet class
    """
    expected_data = {"movies_count": 7}

    expected_df = pd.DataFrame(data=expected_data, index=[0])
    actual_df = test_movies_dataset_object.get_unique_movies()

    assert_frame_equal(expected_df, actual_df)


def test_get_average_movie_rating():
    """
    Testing the get_average_movie_rating method from MoviesDataSet class
    """
    expected_data = {
        "id": [1, 2, 3, 4, 5, 6, 7],
        "title": ["title1", "title2", "title3", "title4", "title5", "title6", "title7"],
        "average_rating": [4.0, 2.0, 3.0, 1.0, 5.0, 5.0, 3.0]
    }

    expected_df = pd.DataFrame(data=expected_data)
    actual_df = test_movies_dataset_object.get_average_movie_rating()

    assert_frame_equal(expected_df, actual_df)


def test_get_top_5_highest_rated_movies():
    """
    Testing the get_top_5_highest_rated_movies method from MoviesDataSet class
    """
    expected_data = {
        "id": [5, 6, 1, 3, 7],
        "title": ["title5", "title6", "title1", "title3", "title7"],
        "average_rating": [5.0, 5.0, 4.0, 3.0, 3.0]
    }

    expected_df = pd.DataFrame(data=expected_data)
    actual_df = test_movies_dataset_object.get_top_5_highest_rated_movies()

    assert_frame_equal(expected_df, actual_df)


def test_get_movies_released_each_year():
    """
    Testing the get_movies_released_each_year method from MoviesDataSet class
    """
    expected_data = {
        "year": ["1995", "2000", "2010"],
        "movies_released": [3, 1, 1],
    }

    expected_df = pd.DataFrame(data=expected_data)
    actual_df = test_movies_dataset_object.get_movies_released_each_year()

    assert_frame_equal(expected_df, actual_df)


def test_get_movies_count_by_genre():
    """
    Testing the get_movies_count_by_genre method from MoviesDataSet class
    """
    expected_data = {
        "genre": ["genre1", None, "genre2", "genre3", "genre5"],
        "movies_count": [3, 2, 2, 1, 1],
    }

    expected_df = pd.DataFrame(data=expected_data)
    actual_df = test_movies_dataset_object.get_movies_count_by_genre()

    assert_frame_equal(expected_df, actual_df)



