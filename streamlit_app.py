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

col = st.columns((1.5,3.5,2), gap='medium')

with col[0]:
    st.markdown('#### Top Rated')

    movie_stats = df.groupby('movie_id').agg(
    average_rating=('rating', 'mean'),
    rating_count=('rating', 'count')
    ).reset_index()

    # 5 best-rated movies with at least 50 ratings
    top_5_50 = (
        movie_stats[movie_stats['rating_count'] >= 50]
        .sort_values(by='average_rating', ascending=False)
        .head(5)
    )

    # 5 best-rated movies with at least 150 ratings
    top_5_150 = (
        movie_stats[movie_stats['rating_count'] >= 150]
        .sort_values(by='average_rating', ascending=False)
        .head(5)
    )

    st.subheader("Top 5 Movies with at least 50 Ratings")
    st.dataframe(top_5_50)

    st.subheader("Top 5 Movies with at least 150 Ratings")
    st.dataframe(top_5_150)

with col[1]:
    st.markdown('#### Mean Movie Ratings By Genre')
    #mean rating by genre
    df_satisfaction = df.groupby('genres')['rating'].mean().reset_index()
    
    
    fig1, ax1 = plt.subplots()

    # Create the barplot
    sns.barplot(data=df_satisfaction, x="rating", y="genres", ax=ax1, color='r')

    # Optional: add title or adjust layout

    # Display in Streamlit
    st.pyplot(fig1)


    st.markdown('#### Viewer Satisfaction Across Release Years')
    df_decade = df.groupby('decade')['rating'].mean().reset_index()

    # Create the figure and axes
    fig2, ax2 = plt.subplots()

    # Create the lineplot
    sns.lineplot(x="decade", y="rating", data=df_decade, ax=ax2, color='r')

    # Rotate x-axis labels
    plt.xticks(rotation=25)

    # Show in Streamlit
    st.pyplot(fig2)

with col[2]:
    st.markdown('#### Genre Breakdown')

    st.dataframe(df_genre, hide_index="True")
