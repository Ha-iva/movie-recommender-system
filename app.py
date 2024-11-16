import streamlit as st 
import pandas as pd
import pickle
import requests


movie_list = pickle.load(open("movies_dict.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# movies = movie_list['title'].values()
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

st.title("Movie Recommender")
selected = st.selectbox("Select a movie", movies["title"].values)

if st.button("Recommend"):
    names,posters = recommend(selected)
    
    # col=st.columns(5)
    
    # for i in range(5):
    #     with col[i]:
    #         st.write(names[i])
    #         st.image(posters[i])
    
    # with col1:
    #     st.write(names[0])
    #     st.image(posters[0])
    # with col2:
    #     st.write(names[1])
    #     st.image(posters[1])
    # with col3:
    #     st.write(names[2])
    #     st.image(posters[2])
        
    # print("\n")
    
    # with col4:
    #     st.write(names[3])
    #     st.image(posters[3])
    # with col5:
    #     st.write(names[4])
    #     st.image(posters[4])


    
    cols1 = st.columns(3)  # First row of 3 columns
    cols2 = st.columns(3)
    cols3 = st.columns(3)# Second row of 3 columns

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
            
    for i, col in enumerate(cols3):
        with col:
            st.text(names[i + 6])  # Start from index 3 for the second row
            st.image(posters[i + 6])







# [theme]
# backgroundColor="#000000"
# textColor="#D3D3D3"
# st.markdown(
#     """<style>
#     /* Change the background color of the entire app */
#     .stApp {
#         background-color: #ffffff;  /* Light gray background */
#         color: #ffffff;
#     }
#     </style>"""
# , unsafe_allow_html=True)

# st.markdown("""
#     <h1 style="color: #FF6347;">This is a custom header</h1>
#     <p>This is some custom <b>HTML</b> content.</p>
# """, unsafe_allow_html=True)


# Customizing the title using HTML with CSS
# st.markdown("""
#     <h1 style="color: #4CAF50; text-align: center; font-family: 'Arial', sans-serif;">
#         Custom Styled Title
#     </h1>
# """, unsafe_allow_html=True)

# st.markdown("""
#     <style>
#         .stTitle > h1 {
#             color: #4CAF50;
#             text-align: center;
#         }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("""
#     <style>
#         .stButton > button {
#             background-color: #FF6347;
#             color: white;
#             font-size: 18px;
#             border-radius: 12px;
#             padding: 10px;
#             width: 100%;
#         }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("""
#     <body style="background-color: #000000;">
#     </body>
# """,unsafe_allow_html=True)

# st.markdown("""
#     <style>
#         /* Style for the Streamlit title (h1 element) */
#         .css-18e3th9 {
#             color: #FF6347;  /* Title color */
#             font-size: 40px;  /* Font size */
#             font-family: 'Arial', sans-serif;  /* Font family */
#             text-align: center;  /* Align to center */
#             font-weight: bold;  /* Make it bold */
#         }
        
#         /* Style for the Streamlit button */
#         .stButton > button {
#             background-color: #FF6347;
#             color: white;
#             font-size: 18px;
#             border-radius: 12px;
#             padding: 10px;
#             width: 100%;
#         }
#     </style>
# """, unsafe_allow_html=True)





