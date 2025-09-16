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

df = pd.read_csv('./data/movie_ratings.csv')
df_genre=pd.read_csv('./data/genre_data.csv')

with st.sidebar:
    st.title('🍿 ReelData 🍿')
    
    year_list = list(df.rating_year.unique())[::-1]
    
    selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
    df_selected_year = df[df.rating_year == selected_year]
    df_selected_year_sorted = df_selected_year.sort_values(by="rating", ascending=False)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

#genre breakdown
def make_barplot():
    # Streamlit Title
    st.title("Seaborn Bar Plot in Streamlit")

    # Create the plot
    fig, ax = plt.subplots()
    sns.barplot(data=df_genre, x='count', y='genre', ax=ax, palette='muted')

    # Customize axes
    ax.set_title("Genre Count")
    ax.set_xlabel("Count")
    ax.set_ylabel("Genre")

    # Show in Streamlit
    st.pyplot(fig)
col = st.columns((3.5,4.5), gap='medium')

with col[0]:
    st.markdown('#### Genre Breakdown')

    make_barplot()