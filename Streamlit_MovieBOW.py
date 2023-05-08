import streamlit as st
import pandas as pd
import pickle
movies_data=pickle.load(open("movies_data.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
def recommend(movie):
    movie_index=movies_data[movies_data['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list_index=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recom_movies=[]
    for i in movies_list_index:
        recom_movies.append(movies_data.iloc[i[0]].title)
    return(recom_movies)

def main():
    st.title("Movie Recommender system")
    movies_list=movies_data['title']
    selected=st.selectbox('Which movie have you seen',movies_list)
    
    if st.button("Recommend"):
        recommendations=recommend(selected)
        for i in recommendations:
            st.write(i)

if __name__=='__main__':
    main()
