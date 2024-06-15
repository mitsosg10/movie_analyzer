# movie_analyzer
A script to analyze movie data
# Movie Abalyzer

    Movie Abalyzer is a tool for analyzing movie data.

    ## Installation

    Use the package manager [pip](https://pip.pypa.io/en/stable/) to install movie_abalyzer.

    ```bash
    pip install movie_abalyzer
    ```

    ## Usage

    ## Basic example
    
    ```import pandas as pd
#from movie_analyzer import MovieAnalyzer

# Define DataFrames (replace 'path/to/file.csv' with actual file paths)
md = pd.read_csv('path/to/metadata.csv')
crd = pd.read_csv('path/to/credits.csv')
kw = pd.read_csv('path/to/keywords.csv')
links = pd.read_csv('path/to/links.csv')
rt = pd.read_csv('path/to/ratings.csv')

# Create a dictionary of DataFrames
csv_files = {
    'metadata': md,
    'credits': crd,
    'keywords': kw,
    'links': links,
    'ratings': rt
}

# Create an instance of MovieAnalyzer
movie_analyzer = MovieAnalyzer(csv_files)

# Perform operations
movie_analyzer.unique_movies_count()
movie_analyzer.average_rating()
movie_analyzer.movies_per_year()
movie_analyzer.movies_per_genre()
movie_analyzer.top_rated_movies()
movie_analyzer.combine_results()

# Save results to a JSON file
json_file_path = 'results.json'
movie_analyzer.save_series_to_json(json_file_path)

    ```

    ## Contributing
    Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

    ## License
    [MIT](https://choosealicense.com/licenses/mit/)
    ''')
