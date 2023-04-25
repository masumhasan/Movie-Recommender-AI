import streamlit as st
import pandas as pd
import pickle
st.title('UFlix Movie Recommender AI')


option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)