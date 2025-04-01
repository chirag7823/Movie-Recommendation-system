import streamlit as st
import pickle
import pandas as pd

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies

# Streamlit UI
st.title('Movie Recommender System')

# Load movies and similarity data
movies_dict = pickle.load(open(r'C:\Users\Chirag B A\OneDrive\Desktop\Documents\movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open(r'C:\Users\Chirag B A\OneDrive\Desktop\Documents\similarity.pkl', 'rb'))

# Dropdown for movie selection
selected_movie_name = st.selectbox("Choose a movie", movies['title'].values)

# Recommend button
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)

    st.subheader("Top 5 Recommended Movies:")
    for movie in recommendations:
        st.write(f"🎬 {movie}")
