import streamlit as st
import pandas as pd
import pickle
movies_d = pickle.load(open('movies_d.pkl','rb'))
movies = pd.DataFrame(movies_d)
st.title('uFlix Movie Recommender AI')
option = st.selectbox(
    'SElect a Movie you like',
    movies['title'].values)

st.write('You selected:', option)