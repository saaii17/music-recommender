# IMPORTS
import streamlit as st
import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import plotly.express as px
import plotly.graph_objects as go

# PAGE CONFIGURATION
st.set_page_config(
    page_title="🎵 Music Recommender System Pro",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
        :root {
            --primary-color: #FF6B6B;
            --secondary-color: #4ECDC4;
            --background-color: #f8f9fa;
        }
        .main {
            background-color: #f8f9fa;
        }
        .stMetric {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .song-card {
            background-color: white;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #FF6B6B;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 10px 0;
        }
        .recommendation-header {
            color: #FF6B6B;
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
        }
        .info-box {
            background-color: #e8f4f8;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #4ECDC4;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# FUNCTION 1: load_data()
@st.cache_data
def load_data():
    """Load music data from CSV file"""
    try:
        csv_path = os.path.join(SCRIPT_DIR, 'music.csv')
        df = pd.read_csv(csv_path)
        # Handle missing values
        df['song_name'] = df['song_name'].fillna('Unknown Song')
        df['artist'] = df['artist'].fillna('Unknown Artist')
        df['genre'] = df['genre'].fillna('Unknown')
        return df
    except FileNotFoundError:
        st.error("❌ Error: music.csv file not found!")
        return None
    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
        return None

# FUNCTION 2: create_similarity_matrix(df)
def create_similarity_matrix(df):
    """Create cosine similarity matrix based on genres"""
    try:
        # Create CountVectorizer from genre column
        vectorizer = CountVectorizer()
        genre_vectors = vectorizer.fit_transform(df['genre'])
        
        # Compute cosine similarity
        similarity_matrix = cosine_similarity(genre_vectors)
        return similarity_matrix
    except Exception as e:
        st.error(f"❌ Error creating similarity matrix: {str(e)}")
        return None

# FUNCTION 3: recommend_songs(song_name, df, similarity_matrix, num_recommendations=5)
def recommend_songs(song_name, df, similarity_matrix, num_recommendations=5):
    """Recommend songs similar to the input song"""
    try:
        # Case-insensitive search
        song_lower = song_name.lower()
        matching_songs = df[df['song_name'].str.lower() == song_lower]
        
        # Validate if song exists
        if matching_songs.empty:
            return None
        
        # Get index of the song
        song_index = matching_songs.index[0]
        
        # Extract similarity scores
        similarity_scores = similarity_matrix[song_index]
        
        # Sort by similarity (descending) and get indices
        similar_indices = np.argsort(similarity_scores)[::-1]
        
        # Exclude the input song itself and get top N
        recommendations = []
        for idx in similar_indices:
            if idx != song_index and len(recommendations) < num_recommendations:
                recommendations.append(df.iloc[idx]['song_name'])
        
        return recommendations
    except Exception as e:
        st.error(f"❌ Error generating recommendations: {str(e)}")
        return None

# FUNCTION 4: get_song_info(song_name, df)
def get_song_info(song_name, df):
    """Get detailed information about a song"""
    try:
        song_data = df[df['song_name'].str.lower() == song_name.lower()]
        if song_data.empty:
            return None
        return song_data.iloc[0]
    except:
        return None

# FUNCTION 5: Filter songs by mood
def filter_by_mood(df, mood):
    """Filter songs by mood"""
    return df[df['mood'] == mood]

# FUNCTION 6: Filter songs by genre
def filter_by_genre(df, genre):
    """Filter songs by genre"""
    return df[df['genre'] == genre]

# MAIN UI SECTION
st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h1 style='color: #FF6B6B; font-size: 48px; margin: 0;'>🎵 Music Recommender System</h1>
        <p style='color: #666; font-size: 18px;'>Discover songs you'll love based on your favorites</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Load data
df = load_data()

if df is not None:
    # Create similarity matrix
    similarity_matrix = create_similarity_matrix(df)
    
    if similarity_matrix is not None:
        # TABS for different sections
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔍 Search & Recommend", "📊 Analytics", "🎯 Filters", "⭐ Top Songs", "ℹ️ About"])
        
        # TAB 1: Search & Recommend
        with tab1:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                song_input = st.text_input(
                    "🎵 Enter a song name:",
                    placeholder="e.g., Blinding Lights, Levitating, Heat Waves",
                    label_visibility="collapsed"
                )
            with col2:
                num_recommendations = st.slider("📈 # of recommendations", 3, 20, 10)
            with col3:
                search_button = st.button("🔍 Find", use_container_width=True, key="search_btn")
            
            if search_button or song_input:
                if song_input.strip():
                    song_info = get_song_info(song_input, df)
                    
                    if song_info is not None:
                        # Display selected song info
                        st.markdown(f"<div class='info-box'>", unsafe_allow_html=True)
                        col1, col2, col3, col4, col5 = st.columns(5)
                        with col1:
                            st.metric("Song", song_info['song_name'][:15] + "...")
                        with col2:
                            st.metric("Artist", song_info['artist'][:15] + "...")
                        with col3:
                            st.metric("⭐ Rating", f"{song_info['rating']}")
                        with col4:
                            st.metric("👍 Popularity", f"{int(song_info['popularity_score'])}")
                        with col5:
                            st.metric("🎭 Mood", song_info['mood'])
                        st.markdown("</div>", unsafe_allow_html=True)
                        
                        st.markdown("---")
                        
                        # Get recommendations
                        recommendations = recommend_songs(song_input, df, similarity_matrix, num_recommendations)
                        
                        if recommendations:
                            st.success(f"✅ Found {len(recommendations)} recommendations!")
                            st.markdown(f"<h3 class='recommendation-header'>🎧 Recommended Songs</h3>", unsafe_allow_html=True)
                            
                            # Display recommendations in columns
                            for i in range(0, len(recommendations), 3):
                                cols = st.columns(3)
                                for j, col in enumerate(cols):
                                    if i + j < len(recommendations):
                                        song = recommendations[i + j]
                                        song_data = get_song_info(song, df)
                                        with col:
                                            with st.container():
                                                st.markdown(f"<div class='song-card'>", unsafe_allow_html=True)
                                                st.markdown(f"**{i + j + 1}. {song}**")
                                                st.caption(f"👤 {song_data['artist']}")
                                                st.caption(f"🎭 {song_data['mood']} | ⭐ {song_data['rating']}")
                                                st.markdown(f"</div>", unsafe_allow_html=True)
                        else:
                            st.error(f"❌ No recommendations found!")
                    else:
                        st.error(f"❌ Song '{song_input}' not found!")
                        st.info("💡 Try searching for one of these popular songs:")
                        sample_songs = df.nlargest(5, 'popularity_score')['song_name'].tolist()
                        for song in sample_songs:
                            st.write(f"• {song}")
                else:
                    st.warning("⚠️ Please enter a song name!")
        
        # TAB 2: Analytics
        with tab2:
            st.subheader("📊 Database Analytics")
            
            # Metrics row
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("🎵 Total Songs", len(df))
            with col2:
                st.metric("🎤 Total Artists", df['artist'].nunique())
            with col3:
                st.metric("🎭 Total Genres", df['genre'].nunique())
            with col4:
                st.metric("📅 Year Range", f"{df['release_year'].min()} - {df['release_year'].max()}")
            
            st.markdown("---")
            
            # Charts
            col1, col2 = st.columns(2)
            
            with col1:
                # Top genres
                top_genres = df['genre'].value_counts().head(10)
                fig_genres = px.bar(
                    x=top_genres.values, 
                    y=top_genres.index,
                    orientation='h',
                    title="Top 10 Genres",
                    labels={'x': 'Count', 'y': 'Genre'},
                    color=top_genres.values,
                    color_continuous_scale="Viridis"
                )
                st.plotly_chart(fig_genres, use_container_width=True)
            
            with col2:
                # Mood distribution
                mood_dist = df['mood'].value_counts()
                fig_mood = px.pie(
                    values=mood_dist.values,
                    names=mood_dist.index,
                    title="Song Mood Distribution",
                    color_discrete_sequence=px.colors.qualitative.Set3
                )
                st.plotly_chart(fig_mood, use_container_width=True)
            
            # Rating vs Popularity scatter
            fig_scatter = px.scatter(
                df,
                x='rating',
                y='popularity_score',
                color='mood',
                size='streams',
                hover_data=['song_name', 'artist'],
                title="Rating vs Popularity (size = streams)",
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
            
            # Top artists
            top_artists = df['artist'].value_counts().head(15)
            fig_artists = px.bar(
                x=top_artists.index,
                y=top_artists.values,
                title="Top 15 Artists",
                labels={'x': 'Artist', 'y': 'Songs'},
                color=top_artists.values,
                color_continuous_scale="Plasma"
            )
            st.plotly_chart(fig_artists, use_container_width=True)
        
        # TAB 3: Filters
        with tab3:
            st.subheader("🎯 Filter Songs")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Filter by mood
                selected_mood = st.selectbox("🎭 Select Mood", ["All"] + sorted(df['mood'].unique().tolist()))
                if selected_mood != "All":
                    mood_songs = filter_by_mood(df, selected_mood)
                    st.success(f"Found {len(mood_songs)} songs with '{selected_mood}' mood")
                    st.dataframe(mood_songs[['song_name', 'artist', 'genre', 'rating']].head(20), use_container_width=True)
            
            with col2:
                # Filter by genre
                selected_genre = st.selectbox("🎵 Select Genre", ["All"] + sorted(df['genre'].unique().tolist()))
                if selected_genre != "All":
                    genre_songs = filter_by_genre(df, selected_genre)
                    st.success(f"Found {len(genre_songs)} songs in '{selected_genre}' genre")
                    st.dataframe(genre_songs[['song_name', 'artist', 'mood', 'rating']].head(20), use_container_width=True)
            
            # Combined filter
            st.markdown("---")
            st.subheader("Advanced Filters")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                min_rating = st.slider("⭐ Minimum Rating", 3.5, 5.0, 3.5)
            with col2:
                min_popularity = st.slider("👍 Minimum Popularity", 50, 100, 50)
            with col3:
                year_range = st.slider("📅 Year Range", 1950, 2024, (1980, 2024))
            
            # Apply combined filters
            filtered_df = df[
                (df['rating'] >= min_rating) &
                (df['popularity_score'] >= min_popularity) &
                (df['release_year'] >= year_range[0]) &
                (df['release_year'] <= year_range[1])
            ]
            
            st.info(f"📊 Showing {len(filtered_df)} songs matching your criteria")
            st.dataframe(
                filtered_df[['song_name', 'artist', 'genre', 'rating', 'popularity_score', 'release_year']],
                use_container_width=True
            )
        
        # TAB 4: Top Songs
        with tab4:
            st.subheader("⭐ Top Songs")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Top Rated Songs**")
                top_rated = df.nlargest(10, 'rating')[['song_name', 'artist', 'rating', 'mood']]
                for idx, (_, row) in enumerate(top_rated.iterrows(), 1):
                    st.write(f"{idx}. **{row['song_name']}** - {row['artist']} ⭐ {row['rating']}")
            
            with col2:
                st.markdown("**Most Popular Songs**")
                most_popular = df.nlargest(10, 'popularity_score')[['song_name', 'artist', 'popularity_score', 'streams']]
                for idx, (_, row) in enumerate(most_popular.iterrows(), 1):
                    st.write(f"{idx}. **{row['song_name']}** - {row['artist']} 👍 {int(row['popularity_score'])}")
            
            st.markdown("---")
            
            # Most streamed
            st.markdown("**Most Streamed Songs**")
            most_streamed = df.nlargest(15, 'streams')[['song_name', 'artist', 'streams', 'genre']]
            fig_streams = px.bar(
                most_streamed,
                x='streams',
                y='song_name',
                orientation='h',
                title="Top 15 Most Streamed Songs",
                color='streams',
                color_continuous_scale="Reds"
            )
            st.plotly_chart(fig_streams, use_container_width=True)
        
        # TAB 5: About
        with tab5:
            st.markdown("""
            ### 🎵 About This Application
            
            Welcome to the **Music Recommender System Pro**! This advanced application helps you discover new music based on your preferences.
            
            #### Features:
            
            - **🔍 Smart Search**: Find songs and get personalized recommendations
            - **📊 Analytics Dashboard**: Explore music statistics and trends
            - **🎯 Advanced Filters**: Filter songs by mood, genre, rating, and more
            - **⭐ Top Songs**: Discover the highest-rated and most popular songs
            - **💾 Large Database**: 500+ songs from various genres and eras
            
            #### Dataset Information:
            
            Our database contains:
            """)
            
            # Display dataset stats
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("🎵 Songs", len(df))
            with col2:
                st.metric("👤 Artists", df['artist'].nunique())
            with col3:
                st.metric("🎭 Genres", df['genre'].nunique())
            
            st.markdown("""
            #### How to Use:
            
            1. **Search & Recommend**: Enter your favorite song name and get similar recommendations
            2. **Explore Analytics**: View charts and statistics about the music database
            3. **Use Filters**: Find songs matching specific moods, genres, or ratings
            4. **Browse Top Songs**: Check out the highest-rated and most popular tracks
            
            #### Recommendation Algorithm:
            
            Our system uses advanced machine learning (Cosine Similarity) to analyze song genres and find similar tracks based on their characteristics.
            
            ---
            
            **Enjoy discovering new music! 🎧**
            """)
        
        # SIDEBAR
        with st.sidebar:
            st.markdown("### 📊 Quick Stats")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Songs", len(df))
            with col2:
                st.metric("Artists", df['artist'].nunique())
            
            st.markdown("---")
            st.markdown("### 🎵 Sample Songs")
            sample_songs = df.nlargest(8, 'popularity_score')['song_name'].tolist()
            for i, song in enumerate(sample_songs, 1):
                st.write(f"{i}. {song}")
            
            st.markdown("---")
            st.markdown("### 💡 Tips")
            st.info("""
            - Use exact song names for best results
            - Check the 'Sample Songs' for popular tracks
            - Explore the Analytics tab for insights
            - Try different moods and genres to discover new music
            """)
            
            st.markdown("---")
            st.markdown("### 🔗 Version")
            st.caption("Music Recommender Pro v2.0")
            st.caption("Powered by Streamlit & Machine Learning")
