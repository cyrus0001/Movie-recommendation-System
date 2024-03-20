import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=672d94cfa918ff6b57256c2588fb420e&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
indices = pd.Series(movies.index, index = movies['title'])


def get_recommendations_similarity(movie):
    try:
        movie_index = indices[movie]
    except KeyError:
        st.error("Error: Movie not found in the database.")
        st.stop()

    sim_scores = list(enumerate(similarity[movie_index]))

    # Extract similarity scores from sim_scores
    sim_scores = [score for _, score in sim_scores]

    # Sort the similarity scores and get the indices of top recommendations
    movie_indices = sorted(range(len(sim_scores)), key=lambda i: sim_scores[i], reverse=True)[1:11]

    recommend_movies = []
    recommended_movie_posters = []
    for i in movie_indices:
        movie_id = movies.iloc[i].movie_id
        recommend_movies.append(movies.iloc[i].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommend_movies, recommended_movie_posters


selected_movie_name = st.selectbox(
     "Type or select a movie from the dropdown",
    movies['title'].values)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = get_recommendations_similarity(selected_movie_name)
    num_rows = 2
    num_columns = 5

    for i in range(num_rows):
        with st.container():
            cols = st.columns(num_columns)
            for j in range(num_columns):
                index = i * num_columns + j
                cols[j].text(recommended_movie_names[index])
                cols[j].image(recommended_movie_posters[index])
