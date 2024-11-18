import requests
import streamlit as st
import datetime

# Logo Display
st.image("https://i.imgur.com/XkL05SS.jpeg")

# Background Styling
st.markdown( 
    """
    <style>
    .stApp {
        background-image: url("https://i.imgur.com/xAM9uUj.jpeg");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Introduction
st.title("Welcome To Daily Update Hub")
st.write("""
Here you will find all kinds of news like health updates, cooking updates, 
daily lifestyle updates, national and international news, and much more.
""")

# API Configuration
API_KEY = 'ae264a6d304344109cc583d9df65fc75'
BASE_URL = "https://newsapi.org/v2/top-headlines"

# Filters
start_date = st.date_input("Start date", datetime.date(2024, 1, 1))
end_date = st.date_input("End date", datetime.date(2024, 12, 31))
categories = ["business", "entertainment", "health", "science", "sports", "technology"]
selected_category = st.selectbox("Select category", categories)
query = st.text_input("Search for news")

# Build API URL based on filters
if query:
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}&from={start_date}&to={end_date}"
else:
    url = f"{BASE_URL}?country=us&apiKey={API_KEY}&category={selected_category}&from={start_date}&to={end_date}"

# Fetch Articles
response = requests.get(url)

if response.status_code == 200:
    articles = response.json().get("articles", [])

    # Pagination
    articles_per_page = 5
    total_pages = (len(articles) // articles_per_page) + 1
    page_number = st.slider("Select page number", 1, total_pages)

    # Calculate the range of articles to show
    start_idx = (page_number - 1) * articles_per_page
    end_idx = start_idx + articles_per_page

    # Display Articles
    for article in articles[start_idx:end_idx]:
        st.subheader(article["title"])
        st.write(article["description"])
        st.write(f"**Source**: {article['source']['name']}")
        if article.get("urlToImage"):
            st.image(article["urlToImage"], caption=article["title"])
        st.write(f"[Read more]({article['url']})")

        # Social Media Share Buttons
        st.markdown(
            f'<a href="https://twitter.com/intent/tweet?text={article["title"]} {article["url"]}" target="_blank">Share on Twitter</a>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<a href="https://www.facebook.com/sharer/sharer.php?u={article["url"]}" target="_blank">Share on Facebook</a>',
            unsafe_allow_html=True
        )
        st.write("---")
else:
    st.error("Failed to fetch news. Please check your API key or try again later.")




