import requests
import streamlit as st
import datetime
from textblob import TextBlob

# News API Key (use your own key here)
api_key = 'ae264a6d304344109cc583d9df65fc75'

# Set up the Streamlit page
st.title("News Update Hub")
st.write("Welcome to the News Update Hub! Get the latest news updates here.")

# Select the categories
categories = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']
category = st.selectbox("Select News Category", categories)

# Function to fetch news from News API
def get_news(category):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}&category={category}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return data['articles']
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return []

# Fetch and display news
if category:
    articles = get_news(category)
    if articles:
        for article in articles:
            st.subheader(article['title'])
            st.write(article['description'])
            st.write(f"Read more: {article['url']}")
            st.write(f"Published at: {article['publishedAt']}")
            
            # Perform sentiment analysis on the article title
            blob = TextBlob(article['title'])
            sentiment = blob.sentiment.polarity
            if sentiment > 0:
                st.write("Sentiment: Positive")
            elif sentiment < 0:
                st.write("Sentiment: Negative")
            else:
                st.write("Sentiment: Neutral")
    else:
        st.write("No news available for this category.")
else:
    st.write("Please select a category to get the news.")

# Display the current date and time
st.write(f"Current Date and Time: {datetime.datetime.now()}")

