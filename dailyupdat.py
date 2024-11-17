import requests
import streamlit as st
from bs4 import BeautifulSoup
from textblob import TextBlob

# Page configuration
st.set_page_config(page_title="Daily Update Hub", layout="wide")

# Title of the app
st.title("📰 Daily Update Hub")

# Sidebar for user input
st.sidebar.header("Filter News")
country = st.sidebar.selectbox("Select Country", ["us", "in", "gb", "ca", "au"])
category = st.sidebar.selectbox(
    "Select Category",
    ["business", "entertainment", "health", "science", "sports", "technology"]
)
st.sidebar.text("Powered by NewsAPI.org")

# News API request function
def fetch_news(country, category):
    api_key = "ae264a6d304344109cc583d9df65fc75"  # Your existing API Key
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        news_data = response.json()
        return news_data["articles"]
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return []

# Display news articles
def display_news(articles):
    if articles:
        for article in articles:
            st.markdown(f"### {article.get('title', 'No Title')}")
            st.image(article.get("urlToImage", "https://via.placeholder.com/150"), width=300)
            st.write(article.get("description", "No Description Available"))
            st.markdown(f"[Read more]({article.get('url')})")
            st.markdown("---")
    else:
        st.warning("No news articles found.")

# Fetch and display news
articles = fetch_news(country, category)
display_news(articles)
