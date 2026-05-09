# IMPORTS
import streamlit as st
import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Music Recommender System",
    page_icon="🎵",
    layout="centered"
)

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

# MAIN UI SECTION
st.title("🎵 Music Recommender System")
st.markdown("Find songs similar to your favorite music!")

# Load data
df = load_data()

if df is not None:
    # Create similarity matrix
    similarity_matrix = create_similarity_matrix(df)
    
    if similarity_matrix is not None:
        # INPUT SECTION
        col1, col2 = st.columns([3, 1])
        with col1:
            song_input = st.text_input("Enter a song name:", placeholder="e.g., Blinding Lights")
        with col2:
            search_button = st.button("🔍 Recommend", use_container_width=True)
        
        # RECOMMENDATION SECTION
        if search_button:
            # Validate empty input
            if not song_input.strip():
                st.warning("⚠️ Please enter a song name!")
            else:
                # Call recommend_songs
                recommendations = recommend_songs(song_input, df, similarity_matrix)
                
                if recommendations:
                    st.success(f"✅ Found {len(recommendations)} recommendations!")
                    st.markdown("### 🎧 Recommended Songs:")
                    for i, song in enumerate(recommendations, 1):
                        song_data = df[df['song_name'].str.lower() == song.lower()].iloc[0]
                        st.markdown(f"**{i}. {song}** - {song_data['artist']}")
                else:
                    st.error(f"❌ Song '{song_input}' not found in database!")
                    st.info("💡 Try one of these songs:")
                    sample_songs = df['song_name'].sample(min(5, len(df))).tolist()
                    for song in sample_songs:
                        st.markdown(f"- {song}")
        
        # SIDEBAR
        st.sidebar.header("📊 Database Info")
        st.sidebar.metric("Total Songs", len(df))
        st.sidebar.metric("Total Artists", df['artist'].nunique())
        st.sidebar.metric("Total Genres", len(df['genre'].str.split().explode().unique()))
        
        st.sidebar.markdown("### 🎵 Sample Songs:")
        for i, song in enumerate(df['song_name'].sample(min(5, len(df))).tolist(), 1):
            st.sidebar.markdown(f"{i}. {song}")
