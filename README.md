# 🫀 Heart Disease Risk Predictor & Machine Learning Analytics

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

An interactive **Machine Learning web application** built with Python, Streamlit, and Scikit-Learn designed to assess cardiovascular risk based on clinical patient health indicators. The system utilizes an optimized `RandomForestClassifier` algorithm to evaluate key biomarkers and provide instant risk probability assessments, feature importance insights, and automated executive PowerPoint report generation.

---

## 🌟 Key Features

- 🔬 **Random Forest Classification Engine**: Predicts heart disease likelihood with high accuracy using multi-tree ensemble evaluation.
- 📊 **Interactive Clinical Analytics**: Real-time evaluation of patient biomarkers with interactive sliders, select boxes, and visual risk gauges.
- 💡 **Biomarker Importance Analysis**: Ranks clinical factors (e.g., ST Slope, Chest Pain Type, Max Heart Rate, Cholesterol levels) by predictive weight.
- 📑 **Automated Executive Presentation Generator**: Generates styled PowerPoint slide decks (`Heart_Risk_Predictor_Presentation.pptx`) containing model performance metrics, dataset summaries, and clinical insights.
- ⚡ **One-Click Local Execution**: Includes `start app.bat` for seamless environment bootstrapping and launch.

---

## 📋 Evaluated Clinical Parameters

| Biomarker | Description | Scale / Range |
| :--- | :--- | :--- |
| **Age** | Patient age in years | 18 - 100 |
| **Sex** | Biological Sex | Male / Female |
| **Chest Pain Type** | Type of chest pain experienced | Typical Angina, Atypical Angina, Non-Anginal, Asymptomatic |
| **Resting BP** | Resting blood pressure (mmHg) | 80 - 200 |
| **Cholesterol** | Serum cholesterol level (mg/dl) | 100 - 600 |
| **Fasting Blood Sugar** | Fasting blood sugar > 120 mg/dl | 0 (False) / 1 (True) |
| **Resting ECG** | Resting electrocardiographic results | Normal, ST-T Wave Abnormality, LV Hypertrophy |
| **Max Heart Rate** | Maximum heart rate achieved during exercise | 60 - 220 |
| **Exercise Angina** | Exercise-induced angina | Yes / No |
| **ST Slope** | Peak exercise ST segment slope | Upsloping, Flat, Downsloping |

---

## 🏗️ Architecture Overview

```
                                ┌────────────────────────────────┐
                                │    Patient Health Metrics      │
                                └───────────────┬────────────────┘
                                                │ Input Data
                                ┌───────────────▼────────────────┐
                                │     Streamlit Web Frontend     │
                                └───────────────┬────────────────┘
                                                │
                     ┌──────────────────────────┴──────────────────────────┐
                     │                                                     │
     ┌───────────────▼────────────────┐                   ┌────────────────▼───────────────┐
     │   Random Forest Classifier     │                   │   PowerPoint Report Generator  │
     │  (Scikit-Learn ML Model)       │                   │    (python-pptx Engine)        │
     └───────────────┬────────────────┘                   └────────────────┬───────────────┘
                     │ Probability %                                       │ Styled PPTX
     ┌───────────────▼────────────────┐                   ┌────────────────▼───────────────┘
     │   Risk Level Assessment UI     │                   │  Executive Slide Deck Export   │
     └────────────────────────────────┘                   └────────────────────────────────┘
```

---

## ⚡ Quick Start Guide

### Prerequisites
- **Python**: `v3.9` or higher

### Option A: One-Click Windows Launch
Double-click `start app.bat` in the project directory. The script will automatically create a virtual environment, install necessary requirements, and launch the Streamlit application in your default browser.

### Option B: Manual Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AIwithVinay/Heart-health-risk-predictor.git
   cd Heart-health-risk-predictor
   ```

2. **Set up Virtual Environment & Install Dependencies**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Linux/macOS:
   source .venv/bin/activate

   pip install -r requirements.txt
   ```

3. **Run the Streamlit Web Application**
   ```bash
   streamlit run app.py
   ```

4. **Generate Presentation Deck (Optional)**
   ```bash
   python generate_ppt.py
   ```

---

## 📊 Dataset & Model Metrics

- **Algorithm**: Scikit-Learn `RandomForestClassifier` (100 Decision Trees, Gini Impurity criterion)
- **Train/Test Split**: 80% Training / 20% Validation
- **Outputs**: Binary Risk Flag (High Risk / Low Risk) & Continuous Risk Probability Percentage.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
