import streamlit as st
import requests

# FastAPI endpoint URL
API_URL = "http://127.0.0.1:8000/search_food"

st.title("FatSecret Food Search API Tester 🍏")

query = st.text_input("Enter a food name:", "")

if st.button("Search"):
    if query:
        with st.spinner("Searching..."):
            response = requests.get(API_URL, params={"query": query})
            st.write("Raw Response:", response.json())  # Print raw JSON for debugging

        if response.status_code == 200:
            data = response.json()
            if "foods" in data and "food" in data["foods"]:
                st.success("Results Found!")
                for food in data["foods"]["food"]:
                    st.subheader(food["food_name"])
                    st.write(f"**Type:** {food.get('food_type', 'N/A')}")
                    st.write(f"🔗 [View Details]({food.get('food_url', '#')})")
                    st.write("---")
            else:
                st.warning("No results found.")
        else:
            st.error(f"API error: {response.status_code}")
    else:
        st.warning("Please enter a food item.")
