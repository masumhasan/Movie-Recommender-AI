import streamlit as st
import pickle
import pandas as pd
import requests

from pathlib import Path
import streamlit_authenticator as stauth


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=05f24270b79f2c782124c1ec4c01fc55&language=en-US'.format(
            movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def fetch_trailer(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}/videos?api_key=05f24270b79f2c782124c1ec4c01fc55&language=en-US'.format(
            movie_id))
    data = response.json()

    # Get the first trailer key
    if data['results']:
        return "https://www.youtube.com/watch?v=" + data['results'][0]['key']
    else:
        return None


movie_d = pickle.load(open('movie_d.pkl', 'rb'))
m = pd.DataFrame(movie_d)

match = pickle.load(open('match.pkl', 'rb'))


def recommend(movie):
    movie_index = m[m['title'] == movie].index[0]
    distances = match[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:6]
    recommended = []
    recommended_posters = []
    for i in movies_list:
        movie_id = m.iloc[i[0]].movie_id
        recommended.append(m.iloc[i[0]].title)
        # fetch poster from Api
        recommended_posters.append(fetch_poster(movie_id))
    return recommended, recommended_posters


# Set meta title and description
st.set_page_config(
    page_title="Movie Recommender App",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title('Movie Recommender')

selected = st.selectbox(
    'What Do You Want To Watch Today?',
    m['title'].values)

st.image(fetch_poster(m[m['title'] == selected].iloc[0]['movie_id']))
st.text(selected)

# Fetch and display trailer
trailer_url = fetch_trailer(m[m['title'] == selected].iloc[0]['movie_id'])
if trailer_url:
    st.video(trailer_url, start_time=0)
else:
    st.warning("No trailer available for this movie.")

if st.button('Recommended Movies'):
    names, posters = recommend(selected)

    st.text('Recommended Movies')
    col1, col2, col3, col4, col5 = (st.columns(5))

    with col1:
        st.image(posters[1])
        st.text(names[1])

    with col2:
        st.image(posters[2])
        st.text(names[2])

    with col3:
        st.image(posters[3])
        st.text(names[3])

    with col4:
        st.image(posters[4])
        st.text(names[4])

    with col5:
        st.image(posters[5])
        st.text(names[5])



st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)