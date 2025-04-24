import streamlit as st 
import pandas as pd
import pickle
import requests

movie_list = pickle.load(open("movies_dict.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movies = pd.DataFrame(movie_list)

def fetch_poster(movie_name):
    response=requests.get('https://www.omdbapi.com/?apikey=448e0559&t={}'.format(movie_name))
    data=response.json()
    return " " + data['Poster']

def recommend(movie):
    # Get the index of the movie in the movie list
    index = movies[movies['title'] == movie].index[0]
    # index = list(movies.values()).index(movie)
    
    # Get the distances (similarities) for the selected movie
    distances = similarity[index]
    
    # Sort the movies based on their similarity (in descending order)
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    
    # Prepare the recommended movie list (excluding the first element since it's the input movie itself)
    recommend_movies = []
    recommend_movies_poster=[]
    for i in movies_list: 
        # movie_id = i[0] 
        name=movies.iloc[i[0]].title
        # Start from index 1 to exclude the input movie itself
        recommend_movies.append(movies.iloc[i[0]].title)  # i[0] gives the movie index
        # recommend_movies_poster.append(fetch_poster(movie_id))
        recommend_movies_poster.append(fetch_poster(name))
    
    return recommend_movies,recommend_movies_poster

st.title(":orange[Movie Recommender]")

selected = st.selectbox(":orange[Select a movie from the given list:]", movies["title"].values)

if st.button("Recommend"):
    try:
        names,posters = recommend(selected)
        cols1 = st.columns(3)  # First row of 3 columns
        cols2 = st.columns(3)
        cols3 = st.columns(3)  # Second row of 3 columns
    
        # Display the first three items in the first row
        for i, col in enumerate(cols1):
            with col:
                st.text(names[i])
                st.image(posters[i])

        # Display the next three items in the second row
        for i, col in enumerate(cols2):
            with col:
                st.text(names[i + 3])  # Start from index 3 for the second row
                st.image(posters[i + 3])

        # Display the next three items in the third row    
        for i, col in enumerate(cols3):
            with col:
                st.text(names[i + 6])  # Start from index 6 for the third row
                st.image(posters[i + 6])
                
        st.write("Thank you 😊")
        
    except Exception:
        
        # Handle the exception and display a custom message without details
        st.error("Oops! Something went wrong. 😢 Please try again later. ")
        
page_element="""
<style>

[data-testid="stAppViewContainer"]{
  background-image: url("https://wallpaperaccess.com/full/5696663.jpg");
  background-size: cover;
  background-position: center;
  animation: move-background 10s infinite linear;
  flex:1;
}

[data-testid="stHeader"]{
  background-color: rgba(0,0,0,0);
}

@keyframes move-background {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 100vw 0;
  }
}

@media (min-width: 1024px) {
    /* Customize behavior for larger screens here */
    body {
        animation: move-background 20s infinite linear;
    }
}

footer {
  position: fixed; /* Keeps the footer fixed at the bottom */
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.8); /* Semi-transparent background */
  color: white;
  text-align: center;
  padding: 10px 0;
  font-size: 14px;
}

</style>

<footer>
Made by: Anubha, Anamika, Archana
</footer>
"""

st.markdown(page_element, unsafe_allow_html=True)

