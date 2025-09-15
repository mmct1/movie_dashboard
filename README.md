# movie_dashboard
CUNY Tech Prep Week 3 Dashboard Exercise 

Questions:
1. What's the breakdown of genres for the movies that were rated?
2. Which genres have the highest viewer satisfaction (highest ratings)?
3. How does mean rating change across movie release years?
4. What are the 5 best-rated movies that have at least 50 ratings? At least 150 ratings?

Extras: 
5. Pick 4 genres. For each genre, how does the rating change as viewer age increases?
    - Suggestion: try to do this for more than 4 genres and see which have the most interesting visualization.
6. Plot number of ratings vs mean rating per genre. Is there a correlation between the volume of ratings and mean rating?
7. We gave you a pre-cleaned genres column, the original dataset is movie_ratings_EC.csv, can you clean it yourself?
    - Hint: Use .explode()

Pointers:
- Movies can belong to multiple genres. Exploding genres is acceptable for preference profiling but not for market share.
- Use minimum sample thresholds (e.g., n ≥ 50 or 100) to avoid small-sample noise.
- Decade and age-group distributions are uneven; include counts or context where relevant.


Deliverables:
Streamlit Dashboard
Create an interactive Streamlit app that:
- Loads and displays the dataset
- Contains visualizations answering each question
- Includes interactive filters (age ranges, occupations, genres, etc.)
- Has clear titles, labels, and explanations for each chart
- Provides insights and conclusions based on the visualizations