# install streamlit: pip install streamlit
# run: streamlit run app.py

import streamlit as st
import pickle
import time



st.title('Twitter Sentiment Analysis')

model = pickle.load(open('twitter_sentiment.pkl', 'rb'))


tweet = st.text_input('Enter your tweet')
