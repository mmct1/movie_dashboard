import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import altair as alt
import squarify
import seaborn as sns

st.set_page_config(
    page_title="ReelData",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="expanded")

df = pd.read_csv('./data/movie_data_reshaped.csv')
df_genre=pd.read_csv('./data/genre_data.csv')

with st.sidebar:
    st.title('🍿 ReelData 🍿')
    
    genre_list = list(df.genres.unique())[::-1]
    
    selected_genre = st.selectbox('Select a genre', genre_list, index=len(genre_list)-1)
    df_selected_genre = df[df.genres == selected_genre]
    df_selected_year_genre = df_selected_genre.sort_values(by="rating", ascending=False)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)


col = st.columns((1.5,3.5,2), gap='medium')

with col[0]:
    st.markdown('#### Top Rated')

with col[1]:
    st.markdown('#### Movie Ratings Over Time')
    #mean rating by genre
    df_satisfaction = df.groupby('genres')['rating'].mean().reset_index()
    fig, ax = plt.subplots()

    # Create the lineplot
    sns.lineplot(x="genres", y="rating", data=df_satisfaction, ax=ax)

    # Rotate x-axis labels
    plt.xticks(rotation=25)

    # Show in Streamlit
    st.pyplot(fig)

    st.markdown('#### Viewer Satisfaction by Genre')

with col[2]:
    st.markdown('#### Genre Breakdown')

    st.dataframe(df_genre, hide_index="True")
