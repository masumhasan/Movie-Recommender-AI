import streamlit as st
import pandas as pd
import pickle
st.title('UFlix Movie Recommender AI')

mList = pickle.load(open('movies.pkl','rb'))
mList = mList['title'].values

selectedMovie = st.selectbox(
    'How would you like to be contacted?',
    mList)

st.write('You selected:', selectedMovie)

import streamlit as st

if st.button('Recommend'):
    st.write(selectedMovie)
