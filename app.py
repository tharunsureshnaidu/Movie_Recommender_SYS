import streamlit as st
import pickle
import pandas as pd
movies_list=pickle.load(open("movies.pkl","rb"))


movies=pd.DataFrame(movies_list)

st.title("Movie Recommender System")

similarity=pickle.load(open("similarity.pkl","rb"))

def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key= lambda x:x[1])[1:6]
    for i in movie_list:
        st.write(movies.iloc[i[0]].title)
    
    

selected_movie=st.selectbox("search",movies["title"].values)
if (st.button("Recommend")):
    recommend(selected_movie)
    
