#!/bin/bash

echo "============================================"
echo "Music Recommender System - Setup"
echo "============================================"
echo ""

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "============================================"
echo "Setup complete!"
echo "To run the application, execute:"
echo "   streamlit run app.py"
echo "============================================"
