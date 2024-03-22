import pandas as pd
from src.movies_dataset_class import MoviesDataSet


# Setting up pandas data frame display options
pd.set_option("colheader_justify", "right")
pd.set_option("display.precision", 3)
pd.set_option("display.unicode.east_asian_width", True)


# 1. Load the dataset from a CSV file.
movies_dataset_object = MoviesDataSet()
print(
    "--- Creating an object of the class MoviesDataSet that loads the movies dataset CSV files when instantiated."
    f"\n\n--- 1. Load the dataset from a CSV file."
    f"\n------ movies_df ------\n{movies_dataset_object.movies_df.dtypes}"
    f"\n------ ratings_df ------\n{movies_dataset_object.ratings_df.dtypes}"
    f"\n------ genres_df ------\n{movies_dataset_object.genres_df.dtypes}"
)

# 2. Print the number of the unique movies in the dataset.
unique_movies_count_df = movies_dataset_object.get_unique_movies()
print(
    f"\n\n--- 2. Print the number of the unique movies in the dataset."
    f"\n------ Unique movies count: {unique_movies_count_df['movies_count'][0]}"
)

# 3. Print the average rating of all the movies.
average_movies_ratings_df = movies_dataset_object.get_average_movie_rating()
print(
    f"\n\n--- 3. Print the average rating of all the movies."
    f"\n------ Data frame with average ratings for movies:\n{average_movies_ratings_df}"
)

# 4. Print the top 5 highest rated movies.
top_5_highest_rated_movies = movies_dataset_object.get_top_5_highest_rated_movies()
print(
    f"\n\n--- 4. Print the top 5 highest rated movies."
    f"\n------ Data frame with top 5 highest rated movies:\n{top_5_highest_rated_movies}"
)

# 5. Print the number of movies released each year.
num_of_movies_released_by_year = movies_dataset_object.get_movies_released_each_year()
print(
    f"\n\n--- 5. Print the number of movies released each year."
    f"\n------ Data frame with number of movies released by year:\n{num_of_movies_released_by_year}"
)

# 6. Print the number of movies in each genre.
num_of_movies_by_genre = movies_dataset_object.get_movies_count_by_genre()
print(
    f"\n\n--- 6. Print the number of movies in each genre."
    f"\n------ Data frame with number of movies grouped by genre:\n{num_of_movies_by_genre}"
)

# 7. Save the dataset to a JSON file.
movies_dataset_object.save_to_json_movies_dataset()
print(
    f"\n\n--- 7. Save the dataset to a JSON file."
    f"\n------ Saving the dataset to JSON files:"
    f"\n------------ Movies metadata saved to: {movies_dataset_object.config.movies_metadata_json}"
    f"\n------------ Movies ratings data saved to: {movies_dataset_object.config.ratings_json}"
    f"\n------------ Movies genres data saved to: {movies_dataset_object.config.genres_json}"
    f"\n------------ Unique movies count data saved to: {movies_dataset_object.config.unique_movies_json}"
    f"\n------------ Average movies ratings data saved to: {movies_dataset_object.config.average_movies_rating_json}"
    f"\n------------ Top 5 highest rated movies data saved to: {movies_dataset_object.config.top_5_rated_movies_json}"
    f"\n------------ Number of of movies released by year data saved to: {movies_dataset_object.config.movies_released_by_year_json}"
    f"\n------------ Number of movies by genre data saved to: {movies_dataset_object.config.movies_by_genre_json}"
)
