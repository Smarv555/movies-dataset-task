# [movies-dataset-task](https://github.com/Smarv555/movies-dataset-task)

This Python program analyzes a dataset containing information about various movies, including their title, release year,
director, genre, and ratings. It is capable to load the dataset and perform several operations utilized by the provided
MoviesDataSet class.

## Folder Structure

```
├───movies-dataset-task
    ├───config
    │   ├───config-main.json
    │   └───config-test.json	
    ├───data
    │   ├───movies_dataset
    │   │   ├───csv
    │   │   │ 	├───genres.csv
    │   │   │ 	├───movies_metadata.csv
    │   │   │ 	└───ratings_small.csv
    │   │   └───json
    │   │    	├───average_movies_rating.json
    │   │   	├───genres.json
    │   │    	├───movies_by_genre.json
    │   │   	├───movies_metadata.json
    │   │    	├───movies_released_by_year.json
    │   │   	├───ratings.json
    │   │    	├───top_5_rated_movies.json
    │   │    	└───unique_movies.json
    │   └───test_datasets
    │       ├───csv
    │       │ 	├───genres.csv
    │       │ 	├───movies_metadata.csv
    │       │ 	└───ratings_small.csv
    │       └───json
    │        	├───average_movies_rating.json
    │      	├───genres.json
    │       	├───movies_by_genre.json
    │      	├───movies_metadata.json
    │       	├───movies_released_by_year.json
    │      	├───ratings.json
    │       	├───top_5_rated_movies.json
    │       	└───unique_movies.json
    ├───src
    │   ├───__init__.py
    │   ├───main.py
    │   ├───movies_dataset_class.py
    │   └───utils.py
    ├───tests
    │   └───test_movies_dataset_class.py
    ├───gitignore
    ├───LICENSE
    ├───pyproject.toml
    ├───README.md
    └───requirements.txt


```

## Features

The main program is utilizing the MoviesDataSet class in order to perform the following tasks:

- Load the dataset from a CSV file.
- Print the number of unique movies in the dataset.
- Print the average rating of all the movies.
- Print the top 5 highest-rated movies.
- Print the number of movies released each year.
- Print the number of movies in each genre.
- Save the dataset to a JSON file.

## Installation

1. Clone this repository to your local machine:

```shell
git clone <repository_url>
```

2. Set up a virtual environment:

```shell
python3 -m venv .venv
```

3. Activate the virtual environment:

```shell
# Linux or Mac
source .venv/bin/activate
```

```shell
# Windows
.venv/Scripts/activate.bat
```

4. Install the required dependencies:

```shell
pip install -r requirements.txt
```

5. Set the Python path environment variable for the project

```shell
# Linux or Mac
export PYTHONPATH=$(pwd):$(pwd)/src
```

```shell
# Windows
set PYTHONPATH=%cd%;%cd%/src
```

## Configuration

There are config-main.json and config-test.json files in the config directory that specify the paths to the dataset
files and other configurations used in the main file and unit tests.

- config-main.json

```json
{
  "csv": {
    "movies_metadata_csv": "../data/movies_dataset/csv/movies_metadata.csv",
    "ratings_csv": "../data/movies_dataset/csv/ratings_small.csv",
    "genres_csv": "../data/movies_dataset/csv/genres.csv"
  },
  "json": {
    "movies_metadata_json": "../data/movies_dataset/json/movies_metadata.json",
    "ratings_json": "../data/movies_dataset/json/ratings.json",
    "genres_json": "../data/movies_dataset/json/genres.json",
    "unique_movies_json": "../data/movies_dataset/json/unique_movies.json",
    "average_movies_rating_json": "../data/movies_dataset/json/average_movies_rating.json",
    "top_5_rated_movies_json": "../data/movies_dataset/json/top_5_rated_movies.json",
    "movies_released_by_year_json": "../data/movies_dataset/json/movies_released_by_year.json",
    "movies_by_genre_json": "../data/movies_dataset/json/movies_by_genre.json"
  }
}
```

## Usage

1. Ensure you have the dataset files in CSV format located in the movies-dataset-task/data/movies_dataset/csv

2. Ensure you are in the src project directory:

```shell
cd src
```

3. Run the main program:

```shell
python main.py
```

## Running Unit Tests

1. Ensure you have the test dataset files in CSV format located in the movies-dataset-task/data/test_datasets/csv

2. Ensure you are in the projects directory

3. Run pytest

```shell
pytest -v tests
```

## Authors

- Stanislav Tsanev - s.tsanev95@abv.bg