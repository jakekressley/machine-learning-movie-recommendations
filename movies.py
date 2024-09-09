import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Data collection
movies_data = pd.read_csv('movies.csv')
selected_features = ['genres','keywords','tagline','cast','director','vote_average', 'popularity', 'vote_count']

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

movies_data['vote_average'] = movies_data['vote_average'].astype(str)
movies_data['popularity'] = movies_data['popularity'].astype(str)
movies_data['vote_count'] = movies_data['vote_count'].astype(str)

combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director'] + ' ' + movies_data['vote_average'] + ' ' + movies_data['popularity'] + ' ' + movies_data['vote_count']

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

similarity = cosine_similarity(feature_vectors)

movie_title_list = movies_data['title'].tolist()

favorite_movies = []
favorites_hset = set()
for i in range(5):
    movie_name = input(f'Enter your favorite movie name {i+1}: ')
    close_matches = difflib.get_close_matches(movie_name, movie_title_list)
    if close_matches:
        closest_match = close_matches[0]
        favorite_movies.append(closest_match)
        favorites_hset.add(closest_match)
    else:
        print(f"No close matches found for {movie_name}. Skipping this movie.")

similarity_scores = np.zeros(len(movies_data))

for movie_name in favorite_movies:
    movie_index = movies_data[movies_data.title == movie_name]['index'].values[0]
    movie_similarity = list(enumerate(similarity[movie_index]))
    movie_similarity_scores = [score for _, score in movie_similarity]
    similarity_scores += np.array(movie_similarity_scores)

similarity_scores /= len(favorite_movies)

sorted_scores = sorted(list(enumerate(similarity_scores)), key=lambda x: x[1], reverse=True)
recommended_movie_indices = [score[0] for score in sorted_scores[:10]]
#sorted_scores = sorted(similarity_scores, key = lambda x:x[1], reverse = True)

printed_movies_count = 0

for index, movie in enumerate(sorted_scores):
    if printed_movies_count >= 10:
        break  # Stop if we have already printed 10 movies
    
    index_from_title = movie[0]
    title = movies_data[movies_data.index == index_from_title]['title'].values[0]
    
    # Check if the movie is not in the user's favorites before printing
    if title not in favorites_hset:
        printed_movies_count += 1
        print(printed_movies_count, '.', title)