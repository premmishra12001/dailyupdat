import streamlit as st
import datetime

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

# Displaying the manual articles with categories and date/time
for article in articles:
    st.subheader(article["title"])
    st.write(article["description"])
    st.write(f"**Category**: {article['category']}")
    st.write(f"**Published on**: {article['date'].strftime('%B %d, %Y at %I:%M %p')}")
    st.write(f"**Source**: {article['source']}")
    
    if article.get("image"):
        st.image(article["image"], caption=article["title"], use_container_width=True)
    
    st.write(f"[Read more]({article['url']})")
    st.write("---")




