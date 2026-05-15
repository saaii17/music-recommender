# 🎵 Spotify Music Pro - Hindi Edition

A professional music streaming platform built with Streamlit, featuring 200+ popular Hindi songs with an intuitive music player interface, AI-powered recommendations, and advanced analytics.

## ✨ Features

### 🎵 Music Player & Search
- **Professional Music Player Interface** - Spotify-like dark theme with modern UI
- **Full Song Details** - View artist, album, movie, genre, rating, popularity, streams
- **Real-time Search** - Find any Hindi song instantly
- **Waveform Visualization** - Animated music waveform display
- **Player Controls** - Play, pause, volume, progress tracking interface

### 🎧 AI-Powered Recommendations (10 Similar Songs)
- **Get 10 Similar Songs** - Personalized recommendations based on genre similarity
- **Cosine Similarity Algorithm** - Uses machine learning to find similar songs
- **Instant Recommendations** - Fast computation of related tracks
- **Complete Song Details** - Each recommendation shows all song information

### 📊 Analytics Dashboard
- **Top Artists** - View most-streamed artists by total streams
- **Genre Distribution** - Pie chart showing music genres
- **Genre Filtering** - Browse songs by specific genre
- **Mood Selection** - Filter songs by mood (Romantic, Sad, Happy, Energetic, etc.)

### ⭐ Top Charts
- **Highest Rated Songs** - Top 10 songs by rating (3.5-5.0 scale)
- **Most Popular Songs** - Top 10 by popularity score (50-100 scale)
- **Most Streamed Songs** - Top 15 with stream counts and visual charts

### 🎭 Discover Features
- **Genre Explorer** - Browse top songs in each genre
- **Mood Playlists** - Curated playlists by emotional mood
- **Analytics Charts** - Interactive Plotly visualizations

### 🎓 About Section
- **Platform Statistics** - Total songs, artists, genres, moods
- **Library Information** - Average ratings, popularity, year ranges
- **How-to Guide** - Feature explanations
- **Popular Artists & Movies** - Quick reference lists
- **Usage Tips** - Pro tips for best experience

## 📊 Dataset

### Collection Size
- **Total Songs:** 200+ popular Hindi songs
- **Artists:** 50+ legendary and modern artists
- **Albums:** 100+ iconic albums
- **Movies:** 80+ Bollywood and regional films
- **Genres:** 8+ genres
- **Moods:** 7 moods
- **Languages:** Hindi
- **Year Range:** 1949-2024

### Song Data Fields
```
- song_name: Full song title
- artist: Artist/singer name
- album: Album name
- movie: Movie/source name
- genre: Music genre classification
- duration_sec: Song length in seconds (180-360)
- release_year: Release year (1949-2024)
- rating: Quality rating (3.5-5.0 scale)
- popularity_score: Popularity metric (50-100 scale)
- mood: Emotional classification
- language: Song language (Hindi)
- streams: Number of streams (1M-500M)
- audio_url: Audio file URL
```

### Sample Popular Songs
- Aashiqui 2 - Arijit Singh (4.9★)
- Chaiyya Chaiyya - A.R. Rahman (4.8★)
- Raatan Lambiyan - Jubin Nautiyal (4.9★)
- Sooraj Dooba Hain - Arijit Singh (4.8★)
- Gerua - Arijit Singh (4.8★)
- Kabira - Arijit Singh (4.9★)
- Tum Saath Ho - A.R. Rahman (4.8★)
- Galliyan - Emiway Bantai (4.9★)
- Chaleya - Arijit Singh (4.8★)
- And 190+ more classics!

## 🚀 Quick Start

### Installation

1. **Download Repository**
```bash
cd music-recommender
```

2. **Create Virtual Environment**
```bash
python -m venv venv
```

3. **Activate Virtual Environment**
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run app.py
```

The app automatically opens at `http://localhost:8501`

## 💻 System Requirements

- **Python:** 3.8 or higher
- **OS:** Windows, macOS, or Linux
- **RAM:** 512 MB minimum
- **Disk Space:** 100+ MB
- **Browser:** Modern web browser
- **Internet:** For first-time setup

## 🎯 Usage Guide

### 1. 🎵 Player & Search Music
1. Go to **"🎵 Player & Search"** tab
2. Enter a song name (e.g., "Aashiqui 2")
3. Click **"🔍 Search"**
4. View the professional music player
5. See complete song details:
   - Song name, artist, album, movie
   - Genre, duration, release year
   - Rating (3.5-5.0), Popularity (0-100), Streams

### 2. 🎧 Get 10 Similar Songs
1. Go to **"🎧 Recommendations"** tab
2. Enter a song name
3. Click **"🔍 Get Similar Songs"**
4. View 10 personalized recommendations
5. Each shows: song, artist, album, movie, rating, popularity

### 3. 📊 Explore Analytics
1. Go to **"📊 Discover"** tab
2. **Analytics:** View top artists, genre distribution
3. **By Genre:** Select genre and browse top songs
4. **By Mood:** Select mood and view playlist

### 4. ⭐ Browse Top Charts
1. Go to **"⭐ Top Charts"** tab
2. View:
   - Top 10 highest-rated songs
   - Top 10 most popular songs
   - Top 15 most-streamed songs

### 5. 🎓 Learn About Platform
1. Go to **"🎓 About"** tab
2. View statistics and features
3. See popular artists and movies
4. Get usage tips

## 🎨 User Interface

### Theme: Spotify Dark Mode
- **Background:** Dark gradient (navy to purple)
- **Primary Color:** Spotify Green (#1DB954)
- **Accent Color:** Emerald Green (#1ed760)
- **Cards:** Translucent with glassmorphism
- **Interactive Elements:** Smooth animations and transitions

### Navigation Tabs
- 🎵 Player & Search - Main music player
- 🎧 Recommendations - 10 similar songs
- 📊 Discover - Analytics and filtering
- ⭐ Top Charts - Trending and rated
- 🎓 About - Platform info

## 🤖 Recommendation Algorithm

### How It Works
1. **Feature Extraction:** Genres converted to character n-grams
2. **Vectorization:** CountVectorizer creates vectors
3. **Similarity:** Cosine similarity measures song closeness
4. **Ranking:** Songs sorted by similarity (descending)
5. **Results:** Top 10 returned

### Example
```
Search: "Aashiqui 2" (Romantic, Bollywood)
↓
Finds similar genre songs
↓
Returns:
1. Sooraj Dooba Hain (Romantic, Bollywood)
2. Gerua (Romantic, Bollywood)
3. Tum Saath Ho (Romantic, Bollywood)
... and 7 more
```

## 📈 Analytics Features

### Metrics
- **Rating:** 3.5-5.0 scale
- **Popularity:** 0-100 scale
- **Streams:** 1M-500M range

### Charts & Visualizations
- Artist streams bar chart
- Genre distribution pie chart
- Rating vs popularity scatter plot
- Most streamed songs chart
- Mood distribution analysis

## 🔧 Technical Stack

| Component | Version |
|-----------|---------|
| **Streamlit** | 1.28.0+ |
| **Python** | 3.8+ |
| **Pandas** | 2.0.0+ |
| **Scikit-learn** | 1.3.0+ |
| **Plotly** | 5.0.0+ |
| **NumPy** | 1.24.0+ |

## 📁 Project Structure

```
music-recommender/
├── app.py                # Main Streamlit app
├── hindi_songs.csv       # 200+ song database
├── requirements.txt      # Dependencies
├── README.md             # Documentation
└── setup.bat/.sh         # Setup scripts
```

## 🎬 Popular Artists

- Arijit Singh (30+ songs)
- Shreya Ghoshal
- Lata Mangeshkar
- A.R. Rahman
- Atif Aslam
- And 40+ more!

## 🎭 Mood Categories

- 😊 **Happy** - Uplifting songs
- 💕 **Romantic** - Love songs
- 😢 **Sad** - Emotional tracks
- ⚡ **Energetic** - High-energy
- 😌 **Chill** - Relaxing
- 😔 **Melancholic** - Deep tracks
- 🎉 **Upbeat** - Fun songs

## 🎼 Genre Categories

- Bollywood
- Pop
- Rock
- Romantic
- Classical
- Devotional
- Hip-Hop
- Punjabi

## 💡 Pro Tips

1. **Search Exactly** - Use full song names
2. **Explore Genres** - Each has unique songs
3. **Check Moods** - Match your current vibe
4. **View Charts** - Discover trending songs
5. **Compare Artists** - See streams and ratings

## 🔍 Troubleshooting

### "Song not found"
- Check spelling
- Browse Top Songs for exact names

### Slow loading
- Refresh page
- Clear browser cache

### Charts not showing
- Reinstall Plotly: `pip install --upgrade plotly`

### Missing modules
- Install all: `pip install -r requirements.txt`

## 📊 Features Overview

| Feature | Spotify Music Pro |
|---------|------------------|
| Songs | 200+ |
| Recommendations | 10 songs |
| Hindi Focus | ✅ Yes |
| Movie Info | ✅ Complete |
| Analytics | ✅ Advanced |
| Dark Theme | ✅ Spotify-style |
| Free | ✅ 100% |
| Open Source | ✅ Yes |

## 🎉 Quick Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py

# Check Python version
python --version

# Check dependencies
pip list | grep -E "streamlit|pandas|plotly"
```

## 📞 Support

- **Issues:** Report bugs or feature requests
- **Suggestions:** Contribute ideas
- **Database:** Add more songs

## 📜 License

Open-source and free to use.

## 🙏 Credits

- **Artists:** All featured musicians
- **Framework:** Streamlit
- **ML:** Scikit-learn
- **Visualization:** Plotly

## 🚀 Get Started Now

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open `http://localhost:8501` in your browser!

---

🎵 **Spotify Music Pro - Your Personal Music Streaming Platform**
*200+ Premium Hindi Songs | AI Recommendations | Professional Interface*
*Search • Recommend • Discover • Analyze • Enjoy*
