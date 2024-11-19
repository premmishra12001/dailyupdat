import streamlit as st
import datetime
import urllib.parse

# Add Google site verification meta tag
st.markdown("""
<meta name="google-site-verification" content="xqn9xjvybwhYcx2jw67nQjtSEffnvenNDkYiHGGGfiY" />
""", unsafe_allow_html=True)

# Logo Display
st.image("https://i.imgur.com/XkL05SS.jpeg", width=200)

# Title and Introduction
st.title("Welcome To Daily Update Hub")
st.write("""
Yahan aapko health updates, cooking updates, daily lifestyle updates, 
national aur international news jaise kai topics milenge.
""")

# Manual Articles
articles = [
    {
        "title": "TOP NEWS INDIA",
        "description": "भारत ने किया हाइपरसोनिक मिसाइल का सफल परीक्षण, जानिए क्या है ख़ासियत?.",
        "url": "https://www.bbc.com/hindi/articles/c5yrq7eq7g9o",
        "source": "BBC NEWS",
        "image": "https://i.imgur.com/5VEbncP.png",
        "category": "SPACE",
        "date": datetime.datetime(2024, 11, 20, 10, 30)  # Date and Time of article
    },
    {
        "title": "टॉप स्टोरी",
        "description": "कनाडा अपने जंगलों में लगने वाली आग को कैसे रोक सकता है?.",
        "url": "https://www.bbc.com/hindi/articles/c62ld2w443yo",
        "source": "BBC NEWS",
        "image": "https://i.imgur.com/Ob9hpZZ.png",
        "category": "Technology",
        "date": datetime.datetime(2024, 11, 19, 15, 45)
    },
    {
        "title": "TOP STORY",
        "description": "ट्रंप प्रशासन में मंत्री बनने जा रहे लोग भारत-पाकिस्तान और चीन के बारे में क्या सोचते हैं?.",
        "url": "https://www.bbc.com/hindi/articles/cg57g4766nvo",
        "source": "BBC NEWS",
        "image": "https://i.imgur.com/JNA37Jc.png",
        "category": "POLITICS",
        "date": datetime.datetime(2024, 11, 18, 9, 0)
    }
]

# Initialize a dictionary to store likes count for each article
likes_count = {article['title']: 0 for article in articles}

# 1. Search Functionality
search_query = st.text_input("Search Articles")

# Filter articles based on search query
filtered_articles = [article for article in articles if search_query.lower() in article['title'].lower() or search_query.lower() in article['description'].lower()]

# 2. Category Filter
categories = ["All", "Space", "Technology", "Politics"]
category_filter = st.selectbox("Select Category", categories)

# Filter articles based on selected category
if category_filter != "All":
    filtered_articles = [article for article in filtered_articles if article['category'] == category_filter]

# 3. Date Filter
start_date = st.date_input("Start Date", datetime.date(2024, 11, 1))
end_date = st.date_input("End Date", datetime.date(2024, 11, 30))

# Filter articles based on date range
filtered_articles = [article for article in filtered_articles if start_date <= article['date'].date() <= end_date]

# 4. Pagination (Show 2 articles per page)
page_size = 2
page_number = st.number_input("Page number", min_value=1, max_value=len(filtered_articles) // page_size + 1, step=1)

# Calculate which articles to display
start_idx = (page_number - 1) * page_size
end_idx = start_idx + page_size
articles_to_display = filtered_articles[start_idx:end_idx]

# 5. Dark Mode / Light Mode toggle
theme = st.radio("Select Theme", ("Light", "Dark"))
if theme == "Dark":
    st.markdown("""
    <style>
    body {
        background-color: #2e2e2e;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    body {
        background-color: white;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# 6. Subscribe for Daily Updates
email = st.text_input("Enter your email to subscribe for daily updates:")

if email:
    st.write(f"Thank you for subscribing with {email}!")
    # Store the email for actual subscription (not implemented here)

# Display filtered articles with all features
for article in articles_to_display:
    # 7. Like Button functionality
    if st.button(f"Like {article['title']}"):
        likes_count[article['title']] += 1
        st.write(f"You liked: {article['title']}")

    st.subheader(article["title"])
    st.write(article["description"])
    st.write(f"**Category**: {article['category']}")
    st.write(f"**Published on**: {article['date'].strftime('%B %d, %Y at %I:%M %p')}")
    st.write(f"**Source**: {article['source']}")
    if article.get("image"):
        st.image(article["image"], caption=article["title"], use_container_width=True)
    st.write(f"[Read more]({article['url']})")

    # 8. Comment Section
    comment = st.text_area(f"Leave a comment on {article['title']}")
    if comment:
        st.write(f"**Your comment**: {comment}")
    
    # 9. Social Share Links
    encoded_url = urllib.parse.quote(article['url'])
    st.markdown(f"""
    <div style="display: flex; gap: 10px;">
        <a href="https://www.facebook.com/sharer/sharer.php?u={encoded_url}" target="_blank">Share on Facebook</a>
        <a href="https://twitter.com/intent/tweet?url={encoded_url}" target="_blank">Share on Twitter</a>
        <a href="https://api.whatsapp.com/send?text={encoded_url}" target="_blank">Share on WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)
    
    # 10. Article Rating (Star Rating)
    stars = st.slider(f"Rate this article: {article['title']}", 1, 5, 3)
    st.write(f"You rated this article {stars} stars.")
    
    st.write("---")

# 11. Popular Articles (Based on Likes)
st.subheader("Popular Articles")
popular_articles = sorted(articles, key=lambda x: likes_count[x['title']], reverse=True)

for article in popular_articles[:3]:  # Display top 3 most liked articles
    st.subheader(article["title"])
    st.write(article["description"])
    st.write(f"**Category**: {article['category']}")
    st.write(f"**Published on**: {article['date'].strftime('%B %d, %Y at %I:%M %p')}")
    st.write(f"**Source**: {article['source']}")
    if article.get("image"):
        st.image(article["image"], caption=article["title"], use_container_width=True)
    st.write(f"[Read more]({article['url']})")
    st.write("---")

# If no articles match the filters, display a message
if not filtered_articles:
    st.write("No articles found matching your search criteria.")
