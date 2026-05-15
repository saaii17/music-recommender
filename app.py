import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import base64

# Set page config
st.set_page_config(
    page_title="🎵 Spotify Music Pro",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Spotify-like dark theme
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #fff;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e, #16213e);
    }
    
    [data-testid="stMainBlockContainer"] {
        background: transparent;
    }
    
    /* Card Styling */
    .song-card {
        background: linear-gradient(135deg, rgba(30, 215, 96, 0.1), rgba(191, 14, 14, 0.1));
        border: 1px solid rgba(30, 215, 96, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        backdrop-filter: blur(10px);
    }
    
    .player-card {
        background: linear-gradient(135deg, rgba(30, 215, 96, 0.15), rgba(191, 14, 14, 0.15));
        border: 2px solid #1DB954;
        border-radius: 16px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 8px 32px rgba(29, 185, 84, 0.2);
    }
    
    .recommend-card {
        background: rgba(20, 20, 20, 0.8);
        border: 1px solid rgba(30, 215, 96, 0.2);
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    }
    
    .info-box {
        background: rgba(45, 45, 45, 0.9);
        border-left: 4px solid #1DB954;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #1DB954, #1ed760);
        color: white;
        border: none;
        border-radius: 24px;
        font-weight: bold;
        padding: 10px 30px;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(29, 185, 84, 0.3);
    }
    
    .stButton > button:hover {
        box-shadow: 0 6px 25px rgba(29, 185, 84, 0.6);
        transform: translateY(-2px);
    }
    
    /* Text Input */
    .stTextInput > div > div > input {
        background: rgba(40, 40, 40, 0.8);
        color: white;
        border: 1px solid rgba(30, 215, 96, 0.3);
        border-radius: 8px;
    }
    
    /* Select Box */
    .stSelectbox > div > div > select {
        background: rgba(40, 40, 40, 0.8);
        color: white;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #1ed760;
        font-weight: 700;
    }
    
    /* Tabs */
    [data-testid="stTabs"] [role="tablist"] button {
        background: rgba(30, 30, 30, 0.6);
        color: #b3b3b3;
        border: none;
        border-radius: 8px;
    }
    
    [data-testid="stTabs"] [role="tablist"] button[aria-selected="true"] {
        background: #1DB954;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('hindi_songs.csv')
        return df
    except:
        st.error("❌ Data file not found")
        return None

# Create similarity matrix
@st.cache_data
def create_similarity_matrix(df):
    vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 2))
    genre_vectors = vectorizer.fit_transform(df['genre'].astype(str))
    similarity_matrix = cosine_similarity(genre_vectors)
    return similarity_matrix

# Recommend 10 similar songs
def recommend_songs(song_name, df, similarity_matrix, num_recommendations=10):
    try:
        song_idx = df[df['song_name'].str.lower() == song_name.lower()].index[0]
    except IndexError:
        return None
    
    similarity_scores = similarity_matrix[song_idx]
    similar_indices = np.argsort(similarity_scores)[::-1][1:num_recommendations+1]
    return df.iloc[similar_indices]

# Get song info
def get_song_info(song_name, df):
    song = df[df['song_name'].str.lower() == song_name.lower()]
    if song.empty:
        return None
    return song.iloc[0]

# Create waveform visualization
def create_waveform():
    x = np.linspace(0, 4*np.pi, 200)
    y = np.sin(x) * np.exp(-x/20)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        line=dict(color='#1DB954', width=3),
        fill='tozeroy',
        fillcolor='rgba(29, 185, 84, 0.2)',
        hoverinfo='skip'
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        hovermode=False,
        height=150,
        margin=dict(l=0, r=0, t=0, b=0)
    )
    return fig

# Main app
def main():
    # Header
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("# 🎵")
    with col2:
        st.markdown("# Spotify Music Pro - Hindi Edition")
    
    st.markdown("### Your Personal Music Streaming Platform")
    st.divider()
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    similarity_matrix = create_similarity_matrix(df)
    
    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎵 Player & Search",
        "🎧 Recommendations",
        "📊 Discover",
        "⭐ Top Charts",
        "🎓 About"
    ])
    
    # TAB 1: PLAYER & SEARCH
    with tab1:
        st.markdown("### 🎼 Music Player")
        st.markdown("---")
        
        # Search Section
        col1, col2 = st.columns([3, 1])
        with col1:
            search_query = st.text_input(
                "Search for a song",
                placeholder="Enter song name (e.g., 'Aashiqui 2', 'Chaiyya Chaiyya')"
            )
        with col2:
            search_btn = st.button("🔍 Search", use_container_width=True)
        
        if search_btn and search_query:
            song_info = get_song_info(search_query, df)
            
            if song_info is not None:
                # Now Playing Display
                st.markdown('<div class="player-card">', unsafe_allow_html=True)
                
                col1, col2 = st.columns([2, 3])
                
                with col1:
                    # Album Art Placeholder with gradient
                    st.markdown("""
                    <div style="
                        width: 200px; 
                        height: 200px; 
                        background: linear-gradient(135deg, #1DB954, #1ed760);
                        border-radius: 12px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 80px;
                        margin: 20px auto;
                    ">♪</div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"### ♫ Now Playing")
                    st.markdown(f"**🎵 Song:** {song_info['song_name']}")
                    st.markdown(f"**🎤 Artist:** {song_info['artist']}")
                    st.markdown(f"**💿 Album:** {song_info['album']}")
                    st.markdown(f"**🎬 Movie:** {song_info['movie']}")
                    st.markdown(f"**🎼 Genre:** {song_info['genre']}")
                    st.markdown(f"**⏱️ Duration:** {int(song_info['duration_sec'])} seconds")
                    st.markdown(f"**📅 Year:** {int(song_info['release_year'])}")
                    st.markdown(f"**⭐ Rating:** {song_info['rating']}/5.0")
                    st.markdown(f"**🔥 Popularity:** {song_info['popularity_score']}/100")
                    st.markdown(f"**📢 Streams:** {int(song_info['streams']):,}")
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Player Controls
                st.markdown("---")
                col1, col2, col3, col4, col5 = st.columns(5)
                with col1:
                    st.button("⏮️ Previous", use_container_width=True, disabled=True)
                with col2:
                    st.button("⏸️ Pause", use_container_width=True)
                with col3:
                    st.button("▶️ Play", use_container_width=True)
                with col4:
                    st.button("⏭️ Next", use_container_width=True, disabled=True)
                with col5:
                    st.button("🔊 Volume", use_container_width=True)
                
                # Waveform
                st.markdown("---")
                st.markdown("### 📈 Waveform")
                waveform_fig = create_waveform()
                st.plotly_chart(waveform_fig, use_container_width=True)
                
                # Progress Bar
                progress_time = st.slider(
                    "Progress",
                    0, int(song_info['duration_sec']),
                    int(song_info['duration_sec'] // 2),
                    label_visibility="collapsed"
                )
                st.caption(f"{progress_time}s / {int(song_info['duration_sec'])}s")
                
                # Song Info Details
                st.markdown("---")
                st.markdown("### ℹ️ Song Details")
                
                info_col1, info_col2, info_col3 = st.columns(3)
                with info_col1:
                    st.markdown(f"""
                    <div class="info-box">
                        <strong>🎵 Mood</strong><br>
                        {song_info['mood']}
                    </div>
                    """, unsafe_allow_html=True)
                
                with info_col2:
                    st.markdown(f"""
                    <div class="info-box">
                        <strong>🌍 Language</strong><br>
                        {song_info['language']}
                    </div>
                    """, unsafe_allow_html=True)
                
                with info_col3:
                    st.markdown(f"""
                    <div class="info-box">
                        <strong>📊 Audio Quality</strong><br>
                        320 kbps
                    </div>
                    """, unsafe_allow_html=True)
                
            else:
                st.error(f"❌ Song '{search_query}' not found. Try another search!")
                st.info("💡 Try searching for: Aashiqui 2, Chaiyya Chaiyya, Raatan Lambiyan")
        
        else:
            st.info("🎵 Enter a song name and click Search to start playing!")
            
            # Show featured songs
            st.markdown("### 🎯 Featured Songs")
            featured = df.nlargest(6, 'popularity_score')[['song_name', 'artist', 'album', 'movie', 'streams', 'rating']]
            
            cols = st.columns(3)
            for idx, (i, song) in enumerate(featured.iterrows()):
                with cols[idx % 3]:
                    st.markdown(f"""
                    <div class="song-card">
                        <strong>🎵 {song['song_name']}</strong><br>
                        <small>by {song['artist']}</small><br>
                        <small>📀 {song['album']}</small><br>
                        <small>🎬 {song['movie']}</small><br>
                        <small>⭐ {song['rating']}/5 | 📢 {int(song['streams']):,} streams</small>
                    </div>
                    """, unsafe_allow_html=True)
    
    # TAB 2: RECOMMENDATIONS (10 SIMILAR SONGS)
    with tab2:
        st.markdown("### 🎧 Get 10 Similar Songs")
        
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            rec_search = st.text_input(
                "Search for a song to get recommendations",
                placeholder="Enter song name...",
                key="rec_search"
            )
        with col2:
            rec_btn = st.button("🔍 Get Similar Songs", use_container_width=True)
        
        if rec_btn and rec_search:
            recommendations = recommend_songs(rec_search, df, similarity_matrix, 10)
            
            if recommendations is not None:
                st.success(f"✅ Found 10 similar songs to '{rec_search}'!")
                st.markdown("---")
                
                # Display recommendations in a nice format
                for idx, (i, song) in enumerate(recommendations.iterrows(), 1):
                    col1, col2 = st.columns([1, 10])
                    with col1:
                        st.markdown(f"### {idx}")
                    with col2:
                        st.markdown(f"""
                        <div class="recommend-card">
                            <strong>🎵 {song['song_name']}</strong><br>
                            <small>🎤 Artist: {song['artist']} | 💿 Album: {song['album']} | 🎬 Movie: {song['movie']}</small><br>
                            <small>⭐ Rating: {song['rating']}/5 | 🔥 Popularity: {song['popularity_score']}/100 | 📢 Streams: {int(song['streams']):,}</small>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.error(f"❌ Song '{rec_search}' not found!")
                st.info("Try these popular songs: Aashiqui 2, Chaiyya Chaiyya, Raatan Lambiyan, Sooraj Dooba Hain")
        
        else:
            st.info("🎵 Search for a song to get 10 personalized recommendations based on genre similarity!")
    
    # TAB 3: DISCOVER
    with tab3:
        st.markdown("### 📊 Explore Music")
        
        tab_discover1, tab_discover2, tab_discover3 = st.tabs(["📈 Analytics", "🎼 By Genre", "🎭 By Mood"])
        
        with tab_discover1:
            # Top Artists
            top_artists = df.groupby('artist').agg({
                'streams': 'sum',
                'rating': 'mean'
            }).nlargest(10, 'streams')
            
            fig_artists = px.bar(
                top_artists.reset_index(),
                x='artist',
                y='streams',
                title="🎤 Top 10 Artists by Streams",
                labels={'streams': 'Total Streams', 'artist': 'Artist'},
                color='rating',
                color_continuous_scale='Greens'
            )
            fig_artists.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                hovermode='x unified'
            )
            st.plotly_chart(fig_artists, use_container_width=True)
            
            # Genre Distribution
            genre_dist = df['genre'].value_counts()
            fig_genre = px.pie(
                values=genre_dist.values,
                names=genre_dist.index,
                title="🎼 Music Genre Distribution",
                color_discrete_sequence=px.colors.sequential.Greens
            )
            fig_genre.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white')
            )
            st.plotly_chart(fig_genre, use_container_width=True)
        
        with tab_discover2:
            selected_genre = st.selectbox("Select Genre", df['genre'].unique())
            genre_songs = df[df['genre'] == selected_genre].nlargest(10, 'rating')
            
            st.markdown(f"### 🎵 Top Songs in {selected_genre}")
            for idx, (i, song) in enumerate(genre_songs.iterrows(), 1):
                st.markdown(f"""
                <div class="song-card">
                    <strong>{idx}. {song['song_name']}</strong><br>
                    <small>🎤 {song['artist']} | 💿 {song['album']} | 🎬 {song['movie']}</small><br>
                    <small>⭐ {song['rating']}/5 | 📢 {int(song['streams']):,} streams</small>
                </div>
                """, unsafe_allow_html=True)
        
        with tab_discover3:
            selected_mood = st.selectbox("Select Mood", df['mood'].unique())
            mood_songs = df[df['mood'] == selected_mood].nlargest(10, 'rating')
            
            st.markdown(f"### 🎭 {selected_mood} Playlist")
            for idx, (i, song) in enumerate(mood_songs.iterrows(), 1):
                st.markdown(f"""
                <div class="song-card">
                    <strong>{idx}. {song['song_name']}</strong><br>
                    <small>🎤 {song['artist']} | 💿 {song['album']} | 🎬 {song['movie']}</small><br>
                    <small>⭐ {song['rating']}/5 | 📢 {int(song['streams']):,} streams</small>
                </div>
                """, unsafe_allow_html=True)
    
    # TAB 4: TOP CHARTS
    with tab4:
        st.markdown("### ⭐ Charts & Rankings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🏆 Top 10 Highest Rated")
            top_rated = df.nlargest(10, 'rating')[['song_name', 'artist', 'album', 'movie', 'rating', 'streams']]
            for idx, (i, song) in enumerate(top_rated.iterrows(), 1):
                st.markdown(f"""
                <div class="song-card">
                    <strong>{idx}. ⭐ {song['rating']}/5 - {song['song_name']}</strong><br>
                    <small>🎤 {song['artist']} | 🎬 {song['movie']}</small>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### 🔥 Top 10 Most Popular")
            top_popular = df.nlargest(10, 'popularity_score')[['song_name', 'artist', 'album', 'movie', 'popularity_score', 'streams']]
            for idx, (i, song) in enumerate(top_popular.iterrows(), 1):
                st.markdown(f"""
                <div class="song-card">
                    <strong>{idx}. 🔥 {song['popularity_score']}/100 - {song['song_name']}</strong><br>
                    <small>🎤 {song['artist']} | 🎬 {song['movie']}</small>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("#### 📢 Top 15 Most Streamed")
        top_streamed = df.nlargest(15, 'streams')[['song_name', 'artist', 'streams', 'rating']]
        
        fig_streams = px.bar(
            top_streamed,
            x='song_name',
            y='streams',
            title="Most Streamed Songs",
            labels={'streams': 'Total Streams', 'song_name': 'Song'},
            color='rating',
            color_continuous_scale='Greens',
            height=500
        )
        fig_streams.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            xaxis_tickangle=-45,
            hovermode='x unified'
        )
        st.plotly_chart(fig_streams, use_container_width=True)
    
    # TAB 5: ABOUT
    with tab5:
        st.markdown("### ℹ️ About Spotify Music Pro")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="info-box">
                <h4>📊 Platform Statistics</h4>
                <strong>Total Songs:</strong> {len(df)}<br>
                <strong>Artists:</strong> {df['artist'].nunique()}<br>
                <strong>Albums:</strong> {df['album'].nunique()}<br>
                <strong>Genres:</strong> {df['genre'].nunique()}<br>
                <strong>Movies:</strong> {df['movie'].nunique()}<br>
                <strong>Languages:</strong> {df['language'].nunique()}<br>
                <strong>Moods:</strong> {df['mood'].nunique()}
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="info-box">
                <h4>🎵 Music Library</h4>
                <strong>All Hindi Songs:</strong> Premium Collection<br>
                <strong>Avg Rating:</strong> {df['rating'].mean():.1f}/5.0<br>
                <strong>Avg Popularity:</strong> {df['popularity_score'].mean():.1f}/100<br>
                <strong>Year Range:</strong> {int(df['release_year'].min())} - {int(df['release_year'].max())}<br>
                <strong>Total Streams:</strong> {int(df['streams'].sum()):,}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 🎓 How It Works")
        
        st.markdown("""
        **1. 🔍 Search & Play**
        - Search for any Hindi song by name
        - View complete song information (artist, album, movie, rating, streams)
        - Professional music player interface
        
        **2. 🎧 Get 10 Similar Songs**
        - Search for a song
        - Get 10 recommendations based on genre similarity
        - Discover music you'll love
        
        **3. 📊 Explore & Discover**
        - Browse songs by genre (Pop, Rock, Bollywood, etc.)
        - Filter by mood (Romantic, Sad, Happy, Energetic, etc.)
        - View analytics and trends
        
        **4. ⭐ Top Charts**
        - Highest rated songs
        - Most popular songs
        - Most streamed songs with real data
        """)
        
        st.markdown("---")
        st.markdown("### 💡 Features")
        
        features_col1, features_col2, features_col3 = st.columns(3)
        
        with features_col1:
            st.markdown("""
            ✅ **Music Search & Play**
            ✅ **10 Song Recommendations**
            ✅ **Full Track Details**
            ✅ **Artist Information**
            """)
        
        with features_col2:
            st.markdown("""
            ✅ **Album Details**
            ✅ **Movie Reference**
            ✅ **Genre Filtering**
            ✅ **Mood Selection**
            """)
        
        with features_col3:
            st.markdown("""
            ✅ **Ratings & Reviews**
            ✅ **Stream Counts**
            ✅ **Top Charts**
            ✅ **Analytics Dashboard**
            """)
        
        st.markdown("---")
        st.markdown("### 🎤 Popular Artists")
        
        artists_list = df.groupby('artist')['streams'].sum().nlargest(12).index.tolist()
        for i in range(0, len(artists_list), 4):
            cols = st.columns(4)
            for j, col in enumerate(cols):
                if i+j < len(artists_list):
                    with col:
                        st.markdown(f"**{artists_list[i+j]}**")
        
        st.markdown("---")
        st.markdown("### 🎬 Popular Movies")
        
        movies_list = df.groupby('movie')['streams'].sum().nlargest(8).index.tolist()
        for i, movie in enumerate(movies_list, 1):
            st.write(f"{i}. 🎬 {movie}")
        
        st.markdown("---")
        st.markdown("### 🌟 Quick Tips")
        
        st.markdown("""
        - **Search Tip:** Use exact song names for best results
        - **Recommendation:** Get 10 similar songs based on genre
        - **Discover:** Explore by genre or mood with filtering
        - **Charts:** Check trending and top-rated songs
        - **Details:** See full song information including streams, rating, popularity
        """)
        
        st.markdown("---")
        st.caption("🎵 Spotify Music Pro - Your Personal Music Streaming Platform | Hindi Edition | 200+ Premium Songs | Powered by Streamlit")

if __name__ == "__main__":
    main()
