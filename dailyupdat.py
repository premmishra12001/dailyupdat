import streamlit as st
import requests

# Title of the app
st.title('https://i.imgur.com/lwlAREm.jpeg')

# Displaying the logo (Make sure the URL is correct or use a local path)
logo_url = "https://your-logo-url.com/logo.png"  # Replace with your logo URL or path
st.image(logo_url, width=200)  # Display logo

# A simple text input to get a category from the user
category = st.text_input("Enter News Category (e.g. business, sports, entertainment):", "business")

# Your News API key
api_key = 'ae264a6d304344109cc583d9df65fc75'  # Use your actual News API key here

# API URL to fetch news based on category
url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={api_key}'

# Requesting news from the API
response = requests.get(url)

# If the request is successful
if response.status_code == 200:
    data = response.json()
    articles = data['articles']

    # Displaying the news articles
    if articles:
        for article in articles:
            st.subheader(article['title'])
            st.write(article['description'])
            st.write(f"Read more: [Link]({article['url']})")
    else:
        st.write('No articles found for this category.')
else:
    st.write(f"Error: {response.status_code}")


