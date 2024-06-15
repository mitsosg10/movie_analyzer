
import unittest
import pandas as pd
from movie_analyzer import MovieAnalyzer

class TestMovieAnalyzer(unittest.TestCase):

    def setUp(self):
        # Sample data to test the MovieAnalyzer class
        self.csv_files = {
            'metadata': pd.DataFrame({
                'id': [1, 2],
                'vote_count': [10, 20],
                'vote_average': [7.5, 8.0],
                'genres': ['[{"id": 28, "name": "Action"}]', '[{"id": 12, "name": "Adventure"}]'],
                'release_date': ['2000-01-01', '2001-01-01'],
                'popularity': [1.0, 2.0],
                'title': ['Movie 1', 'Movie 2']
            }),
            'credits': pd.DataFrame({
                'id': [1, 2],
                'cast': ['[{"cast_id": 14, "character": "Character 1", "name": "Actor 1"}]',
                         '[{"cast_id": 15, "character": "Character 2", "name": "Actor 2"}]'],
                'crew': ['[{"credit_id": "52fe4233", "department": "Directing", "name": "Director 1"}]',
                         '[{"credit_id": "52fe4234", "department": "Directing", "name": "Director 2"}]']
            }),
            'keywords': pd.DataFrame({
                'id': [1, 2],
                'keywords': ['[{"id": 931, "name": "keyword1"}]', '[{"id": 932, "name": "keyword2"}]']
            }),
            'links': pd.DataFrame({
                'movieId': [1, 2],
                'imdbId': [111, 222],
                'tmdbId': [1001, 1002]
            }),
            'ratings': pd.DataFrame({
                'userId': [1, 2],
                'movieId': [1, 2],
                'rating': [4.0, 5.0],
                'timestamp': [964982703, 964982224]
            })
        }
        self.analyzer = MovieAnalyzer(self.csv_files)

    def test_unique_movies_count(self):
        self.analyzer.unique_movies_count()
        self.assertEqual(self.analyzer.un, 2)

    def test_average_rating(self):
        self.analyzer.average_rating()
        expected_avg_ratings = {1: 4.0, 2: 5.0}
        self.assertEqual(self.analyzer.avgrt, expected_avg_ratings)

    def test_top_rated_movies(self):
        self.analyzer.top_rated_movies()
        self.assertEqual(len(self.analyzer.top5), 2)

    def test_movies_per_year(self):
        self.analyzer.movies_per_year()
        expected_movies_per_year = pd.DataFrame({
            'Year': [2000, 2001],
            'Number of Movies': [1, 1]
        })
        pd.testing.assert_frame_equal(self.analyzer.mpy, expected_movies_per_year)

    def test_movies_per_genre(self):
        self.analyzer.movies_per_genre()
        expected_genre_count = {'Action': 1, 'Adventure': 1}
        self.assertEqual(self.analyzer.gc, expected_genre_count)

    def test_combine_results(self):
        self.analyzer.unique_movies_count()
        self.analyzer.average_rating()
        self.analyzer.movies_per_year()
        self.analyzer.movies_per_genre()
        self.analyzer.top_rated_movies()
        self.analyzer.combine_results()
        self.assertIn('Unique Movies Count', self.analyzer.df)
        self.assertIn('Average Ratings', self.analyzer.df)
        self.assertIn('Top Rated Movies', self.analyzer.df)
        self.assertIn('Movies Per Year', self.analyzer.df)
        self.assertIn('Movies Per Genre', self.analyzer.df)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
