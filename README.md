# 🎵 Music Recommender System

An intelligent web application that suggests songs based on user preferences using machine learning and genre-based similarity analysis.

## 📋 Features

✅ **Smart Recommendations** - Uses cosine similarity algorithm to find similar songs
✅ **Genre Analysis** - Analyzes music genres for accurate recommendations
✅ **Fast Performance** - Streamlit caching for instant results
✅ **Clean UI** - User-friendly interface with intuitive design
✅ **Error Handling** - Comprehensive error messages and validation
✅ **Cloud Ready** - Easy deployment to Streamlit Cloud

## 📊 Project Structure

```
music-recommender/
├── app.py                   # Main Streamlit application
├── generate_document.py     # Documentation generator
├── music.csv                # Music dataset (CSV format)
├── requirements.txt         # Python dependencies
├── setup.bat               # Windows setup script
├── setup.sh                # Mac/Linux setup script
└── README.md               # This file
```

## 🛠️ Technologies

- **Streamlit** (≥1.28.0) - Web UI framework
- **Pandas** (≥2.0.0) - Data manipulation
- **Scikit-learn** (≥1.3.0) - Machine learning
- **NumPy** (≥1.24.0) - Numerical operations
- **Python-docx** - Document generation

## 📥 Installation

### Windows
```bash
# Run the setup script
setup.bat
```

### Mac/Linux
```bash
# Make script executable
chmod +x setup.sh

# Run the setup script
./setup.sh
```

### Manual Setup
```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 💻 How It Works

1. **User Input**: Enter a song name you like
2. **Search**: System searches for the song in the database
3. **Analysis**: Calculates similarity scores based on genres
4. **Recommendation**: Returns top 5 most similar songs
5. **Display**: Shows recommendations with song name and artist

### Example Usage
- Enter: "Blinding Lights"
- Get: Songs similar to The Weeknd's electronic/pop style
- Results: Top 5 recommendations like "Levitating", "Heat Waves", etc.

## 🧪 Test Songs

Try these songs to test the system:
- "Blinding Lights" - Synthwave Pop Electronic
- "Bohemian Rhapsody" - Rock Theatrical
- "Heat Waves" - Indie Pop Psychedelic
- "Come Together" - Rock Psychedelic
- "Hotel California" - Classic Rock

## 📊 Database Info

The `music.csv` file contains:
- **song_name** - Name of the song
- **artist** - Artist/Band name
- **genre** - Music genre(s) separated by spaces

Default dataset: 20 songs (easily expandable)

## 🌐 Deployment to Streamlit Cloud

1. Create a GitHub repository
2. Push code to GitHub
3. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
4. Click "New app"
5. Select repository, branch, and main file (app.py)
6. Deploy!

## 🧠 Algorithm Explanation

### CountVectorizer
Converts genre text into numerical vectors where each genre word becomes a feature.

### Cosine Similarity
Measures the angle between genre vectors to find similar songs.
- Values 0-1 (0 = no similarity, 1 = identical)
- Formula: cos(θ) = (A·B) / (|A| × |B|)

### Recommendation Pipeline
1. Find the input song's index
2. Get its genre vector
3. Compare with all other songs' vectors
4. Sort by similarity score
5. Return top 5 (excluding input song)

## 📝 Generate Documentation

Generate a Word document with project documentation:

```bash
python generate_document.py
```

Creates: `Music_Recommender_Documentation.docx`

## 🔧 Customization

### Add More Songs
Edit `music.csv` and add new rows with song name, artist, and genres.

### Change Recommendation Count
In `app.py`, modify the `num_recommendations` parameter in the `recommend_songs()` function call.

### Customize UI
Modify colors and styling in `app.py` using Streamlit components.

## 📊 Performance Metrics

- **Recommendation Speed**: ~10-100ms per request
- **Load Time**: Instant with caching
- **Database Size**: 20-100+ songs (expandable)
- **Accuracy**: Based on genre similarity

## 🐛 Troubleshooting

### "music.csv not found"
- Ensure `music.csv` is in the same directory as `app.py`
- Check file name spelling

### "Song not found"
- Check exact song name spelling
- Try a different song from the sample list
- See sidebar for available songs

### Installation Issues
- Ensure Python 3.8+ is installed
- Delete `venv` folder and reinstall
- Try `pip install --upgrade pip`

## 💡 Future Enhancements

- Add song ratings and popularity scores
- User preference profiles
- Multi-feature similarity (artist, date, popularity)
- Playlist auto-generation
- Export recommendations
- Dark mode theme
- Advanced ML with embeddings

## 📄 License

This project is free to use and modify.

## 👨‍💻 Author

Created as a comprehensive music recommendation system using machine learning.

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📞 Support

For issues or questions, check the troubleshooting section or review the code comments.

---

**Built with ❤️ using Python, Streamlit, and Machine Learning**
