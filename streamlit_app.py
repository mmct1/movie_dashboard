import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import altair as alt
import squarify

st.set_page_config(
    page_title="ReelData",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="expanded")

df = pd.read_csv('./data/movie_ratings.csv')

with st.sidebar:
    st.title('🍿 ReelData 🍿')
    
    year_list = list(df.rating_year.unique())[::-1]
    
    selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
    df_selected_year = df[df.rating_year == selected_year]
    df_selected_year_sorted = df_selected_year.sort_values(by="rating", ascending=False)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

#genre breakdown
def make_treemap(input_df, input_col, input_color_thm):
    normed = squarify.normalize_sizes(df['value'], 100, 100)
    rects = squarify.squarify(normed, 0, 0, 100, 100)

    # Add rectangle info to the dataframe
    for i, r in enumerate(rects):
        df.loc[i, 'x'] = r['x']
        df.loc[i, 'y'] = r['y']
        df.loc[i, 'dx'] = r['dx']
        df.loc[i, 'dy'] = r['dy']

    # Create Altair treemap
    treemap = alt.Chart(df).mark_rect().encode(
        x=alt.X('x:Q', scale=alt.Scale(domain=[0, 100])),
        y=alt.Y('y:Q', scale=alt.Scale(domain=[0, 100])),
        x2='x2:Q',
        y2='y2:Q',
        color='category:N',
        tooltip=['category', 'value']
    ).properties(
        width=600,
        height=400,
        title="Altair Treemap"
    )

    # Add calculated x2, y2 (bottom right corner)
    df['x2'] = df['x'] + df['dx']
    df['y2'] = df['y'] + df['dy']

    st.title("Altair Treemap in Streamlit")
    st.altair_chart(treemap, use_container_width=True)

col = st.columns((3.5, 4.5), gap='medium')

with col[0]:
    st.markdown('#### Genre Breakdown')

    treemap = make_treemap(df, 'genres',  selected_color_theme)
    st.altair_chart(treemap, use_container_width=True)