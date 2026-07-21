from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import os

def create_presentation():
    # Initialize presentation
    prs = Presentation()

    # Helper function to add a standard slide
    def add_slide(prs, title_text, content_bullets, image_path=None):
        slide_layout = prs.slide_layouts[1] # Title and Content layout
        slide = prs.slides.add_slide(slide_layout)
        
        title = slide.shapes.title
        title.text = title_text
        
        # Formatting title
        title.text_frame.paragraphs[0].font.name = "Calibri"
        title.text_frame.paragraphs[0].font.bold = True
        title.text_frame.paragraphs[0].font.size = Pt(40)
        title.text_frame.paragraphs[0].font.color.rgb = RGBColor(30, 58, 138) # Dark blue
        
        # Adding content
        content = slide.placeholders[1]
        tf = content.text_frame
        
        # If there is an image, we should resize the text box to make room on less wide text limits
        if image_path:
            content.width = Inches(5.3)
        
        if content_bullets:
            tf.text = content_bullets[0]
            tf.paragraphs[0].font.size = Pt(24)
            for bullet in content_bullets[1:]:
                p = tf.add_paragraph()
                p.text = bullet
                p.level = 0
                p.font.size = Pt(24)
                # Adding some spacing after paragraphs for better readability
                p.space_after = Pt(14)
                
        # Add Image if provided
        if image_path and os.path.exists(image_path):
            # Positioned on the right side of the slide
            left = Inches(5.5)
            top = Inches(2.0)
            # Setting width so aspect ratio remains proportional
            width = Inches(4.0)
            slide.shapes.add_picture(image_path, left, top, width=width)
                
        return slide

    # Slide 1: Title Slide (Layout 0)
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    
    title.text = "Cardiac Wellness System\n(Heart Risk Predictor)"
    title.text_frame.paragraphs[0].font.bold = True
    title.text_frame.paragraphs[0].font.color.rgb = RGBColor(30, 58, 138)
    
    subtitle.text = "A Comprehensive Machine Learning Health Checkup\n\nDeveloped By: Vinay, Om, and Biswojit"
    subtitle.text_frame.paragraphs[0].font.size = Pt(20)

    # Image Paths generated specifically for the presentation
    img1 = r"C:\Users\vinay\.gemini\antigravity\brain\55a39339-1c12-42ce-b095-1816f92c0504\heart_health_ai_1775624286879.png"
    img2 = r"C:\Users\vinay\.gemini\antigravity\brain\55a39339-1c12-42ce-b095-1816f92c0504\ml_random_forest_1775624306165.png"
    img3 = r"C:\Users\vinay\.gemini\antigravity\brain\55a39339-1c12-42ce-b095-1816f92c0504\ui_dashboard_concept_1775624322507.png"

    # Slide Content Data (Slides 2 to 10)
    slides_data = [
        ("1. Introduction", [
            "Cardiovascular diseases are a leading cause of global mortality.",
            "Early detection using predictive modeling is potentially life-saving.",
            "Purpose: Develop an ML web application to predict heart disease likelihood.",
            "Approach: A streamlined interface providing self-assessment using an underlying trained ML model."
        ], img1),
        ("2. Project Objectives", [
            "Create an intuitive, single-page user interface for quick health checkups.",
            "Utilize key biometric data (Age, Sex, BMI, Blood Temp, etc.) to assess risk.",
            "Implement a Deep Random Forest Classification model for high accuracy.",
            "Provide users with meaningful interactive, animated diagnostic reports."
        ], None),
        ("3. Technologies Used", [
            "Programming Language: Python (Core Logic & ML)",
            "Frontend Framework: Streamlit (Web Interface)",
            "UI/UX Design: Custom HTML/CSS with Glassmorphism & Animated Gradients",
            "Machine Learning: Scikit-Learn (RandomForestClassifier)",
            "Data Processing: Pandas & NumPy"
        ], None),
        ("4. Health Input Features", [
            "The model analyzes 6 critical health indicators:",
            "1. Demographic: Age & Biological Sex",
            "2. Body Metrics: Height and Weight (Real-time BMI calculation)",
            "3. Vital Sign: Resting Blood Pressure (mmHg)",
            "4. Lab Metric: Total Cholesterol (mg/dl)",
            "5. Symptoms: Chest Pain Level (Asymptomatic to Severe Angina)"
        ], None),
        ("5. Machine Learning Methodology", [
            "Algorithm: Random Forest Classifier (100 estimators, max depth 7)",
            "Data Source: Synthetically generated robust dataset of 4,000 cases.",
            "Data Split: 80% Training Data, 20% Testing Data with balanced class weights.",
            "Performance: Achieves high predictive accuracy on the evaluation data."
        ], img2),
        ("6. User Interface & Design Strategy", [
            "Modern \"Glassmorphism\" UI with clean light/dark visually cards.",
            "Dynamic background gradients via custom CSS flow animations.",
            "Single-page architecture for an \"all-in-one-screen\" experience.",
            "Immediate visual feedback as users adjust health input sliders."
        ], img3),
        ("7. Diagnostic Reporting Mechanics", [
            "Dynamic Results Processing:",
            "- Optimal Health: Displays comforting heartbeat animation (Green).",
            "- Elevated Risk: Displays flashing warning animation (Red).",
            "Custom Medical Advisory Plans based on the specific prediction.",
            "Includes a UI Pie Chart visualizing Risk vs. Safe percentages."
        ], None),
        ("8. Key System Advantages", [
            "Real-time Assessment: Instant feedback with near zero-latency.",
            "Privacy-Centric: Localized data processing; no external cloud storage.",
            "Exportable Summaries: Users can download a .txt medical report.",
            "Educational Impact: Promotes awareness of fundamental health trackers."
        ], None),
        ("9. Conclusion", [
            "The Cardiac Wellness System effectively combines aesthetic modern web design with powerful machine learning.",
            "It successfully demonstrates the potential of AI in personal healthcare monitoring systems.",
            "Delivers an intuitive, accessible experience without sacrificing depth."
        ], None),
        ("10. Future Scope & Expansion", [
            "Integration with Wearable Technology (Smartwatches/Fitness trackers) for automated data extraction.",
            "Expand backend connectivity to incorporate Electronic Health Records (EHR).",
            "Incorporate advanced deep learning neural networks utilizing significantly larger, real-world clinical datasets."
        ], None)
    ]

    # Generate slides
    for title_text, bullets, img_path in slides_data:
        add_slide(prs, title_text, bullets, img_path)

    # Save presentation
    output_filename = "Heart_Risk_Predictor_Presentation_v2.pptx"
    output_path = os.path.join(os.getcwd(), output_filename)
    prs.save(output_path)
    print(f"Presentation successfully created at: {output_path}")

if __name__ == "__main__":
    create_presentation()
