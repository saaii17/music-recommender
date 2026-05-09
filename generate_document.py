"""
Generate Word document with project documentation
"""
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml

def add_heading_with_color(doc, text, level, color_rgb):
    """Add colored heading to document"""
    heading = doc.add_heading(text, level=level)
    for run in heading.runs:
        run.font.color.rgb = RGBColor(*color_rgb)
    heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return heading

def add_colored_paragraph(doc, text, color_rgb=None, bold=False):
    """Add formatted paragraph"""
    paragraph = doc.add_paragraph(text)
    for run in paragraph.runs:
        if color_rgb:
            run.font.color.rgb = RGBColor(*color_rgb)
        if bold:
            run.font.bold = True
    return paragraph

def shade_paragraph(paragraph, color_hex):
    """Add background color to paragraph"""
    shading_elm = parse_xml(r'<w:shd {} xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'.format('w:fill="{}"'.format(color_hex)))
    paragraph._element.get_or_add_pPr().append(shading_elm)

def generate_documentation():
    """Generate complete project documentation"""
    doc = Document()
    
    # Title
    add_heading_with_color(doc, "🎵 Music Recommender System", level=0, color_rgb=(0, 102, 204))
    
    # Introduction
    add_heading_with_color(doc, "Project Introduction", level=1, color_rgb=(0, 102, 204))
    doc.add_paragraph(
        "The Music Recommender System is an intelligent web application that suggests songs based on user preferences. "
        "This system uses advanced machine learning algorithms to analyze music genres and provide personalized recommendations."
    )
    
    # System Architecture
    add_heading_with_color(doc, "System Architecture", level=1, color_rgb=(0, 102, 204))
    doc.add_paragraph("The system follows a modern architecture:")
    doc.add_paragraph("Frontend: Streamlit web interface", style='List Bullet')
    doc.add_paragraph("Backend: Python with scikit-learn ML engine", style='List Bullet')
    doc.add_paragraph("Data Storage: CSV-based music database", style='List Bullet')
    doc.add_paragraph("Algorithm: Cosine Similarity on genre vectors", style='List Bullet')
    
    # Technologies
    add_heading_with_color(doc, "Technologies Used", level=1, color_rgb=(0, 102, 204))
    doc.add_paragraph("Python 3.8+", style='List Bullet')
    doc.add_paragraph("Streamlit - Web framework", style='List Bullet')
    doc.add_paragraph("Pandas - Data manipulation", style='List Bullet')
    doc.add_paragraph("Scikit-learn - Machine Learning", style='List Bullet')
    doc.add_paragraph("NumPy - Numerical computing", style='List Bullet')
    
    # Installation
    add_heading_with_color(doc, "Installation Instructions", level=1, color_rgb=(0, 102, 204))
    doc.add_paragraph("Windows Setup:")
    doc.add_paragraph("Run setup.bat script to automatically set up environment", style='List Bullet')
    doc.add_paragraph("Mac/Linux Setup:")
    doc.add_paragraph("Run setup.sh script to automatically set up environment", style='List Bullet')
    doc.add_paragraph("Manual Installation:")
    doc.add_paragraph("python -m venv venv", style='List Bullet')
    doc.add_paragraph("pip install -r requirements.txt", style='List Bullet')
    
    # Deployment
    add_heading_with_color(doc, "Deployment Guide", level=1, color_rgb=(0, 102, 204))
    doc.add_paragraph("Deploy to Streamlit Cloud in 3 simple steps:")
    doc.add_paragraph("1. Push code to GitHub", style='List Number')
    doc.add_paragraph("2. Visit streamlit.io/cloud", style='List Number')
    doc.add_paragraph("3. Click 'New app' and select your repository", style='List Number')
    
    # Testing
    add_heading_with_color(doc, "Testing Scenarios", level=1, color_rgb=(0, 102, 204))
    doc.add_paragraph("Test the system with these example songs:")
    doc.add_paragraph('"Blinding Lights" - Should return Synthwave/Pop songs', style='List Bullet')
    doc.add_paragraph('"Bohemian Rhapsody" - Should return Rock/Theatrical songs', style='List Bullet')
    doc.add_paragraph('"Heat Waves" - Should return Indie Pop/Psychedelic songs', style='List Bullet')
    doc.add_paragraph('"Come Together" - Should return Rock songs', style='List Bullet')
    
    # Features
    add_heading_with_color(doc, "Key Features", level=1, color_rgb=(0, 102, 204))
    doc.add_paragraph("Smart Recommendations using Cosine Similarity", style='List Bullet')
    doc.add_paragraph("Genre-based Analysis", style='List Bullet')
    doc.add_paragraph("Fast Performance with Caching", style='List Bullet')
    doc.add_paragraph("Clean and Intuitive User Interface", style='List Bullet')
    doc.add_paragraph("Comprehensive Error Handling", style='List Bullet')
    doc.add_paragraph("Production-Ready Deployment Ready", style='List Bullet')
    
    # Save document
    doc.save('Music_Recommender_Documentation.docx')
    print("✅ Documentation generated: Music_Recommender_Documentation.docx")

if __name__ == "__main__":
    generate_documentation()
