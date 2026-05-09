@echo off
echo ============================================
echo Music Recommender System - Windows Setup
echo ============================================
echo.

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ============================================
echo Setup complete!
echo To run the application, execute:
echo   streamlit run app.py
echo ============================================
pause
