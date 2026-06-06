import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title="My Portfolio")

#import streamlit as st

# ---- Initialize Theme ----
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# ---- Toggle (Sidebar Recommended) ----
if st.sidebar.toggle("🌙 Dark Mode"):
    st.session_state.theme = "dark"
else:
    st.session_state.theme = "light"

# ---- Theme Colors ----
def get_theme():
    if st.session_state.theme == "dark":
        return {
            "bg": "#0e1117",
            "text": "#ffffff",
            "border": "#2c2f36"
        }
    else:
        return {
            "bg": "#ffffff",
            "text": "#000000",
            "border": "#d1d5db"
        }

theme = get_theme()

# ---- Apply Theme Globally ----
st.markdown(f"""
<style>
.stApp {{
    background-color: {theme['bg']};
    color: {theme['text']};
}}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
html {
    scroll-behavior: smooth;
}
</style>
""", unsafe_allow_html=True)


# ---- Navigation Links ----
st.markdown("""
<div style="display:flex; gap:20px;">
    <a href="#about">About</a>
    <a href="#projects">Projects</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

#Abiut me section........................

st.markdown("""
    <style>
    .top-bar {
        width: 100%;
        background-color: #001f3f;  /* 🔵 navy blue */
        padding: 25px;
        color: white;
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        font-family: 'Brush Script MT', cursive;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1000;
        letter-spacing: 2px;
    }

    .block-container {
        padding-top: 110px;
    }
    </style>

    <div class="top-bar">
        Sanya Katiyar
    </div>""",unsafe_allow_html=True)

# ---- Columns Layout ----
col1, col2 = st.columns([1, 2])

# ---- LEFT SIDE IMAGE ----
with col1:
    st.image("images/me.jpg", width=200)  # apni image ka naam yaha do

# ---- RIGHT SIDE ABOUT SECTION ----
with col2:
    st.markdown("""<h4 style="color:lightblue"><u>About Me</u></h4>""", unsafe_allow_html=True)

    st.markdown("""
    I am a Computer Science student with a strong interest in Data Analytics and Programming. 
    With a science background, I developed a curiosity for technology at an early stage and have been consistently working to build my skills in this field.
    """)

    st.markdown("""
    I enjoy working with tools like Python, Power BI, and Excel to clean, analyze, and visualize data. 
    Through my projects, I focus on transforming raw data into meaningful insights that can support better decision-making.
    """)

            
            
st.markdown("""I am a quick learner, detail-oriented, and highly motivated to continuously improve my skills. I believe in staying updated with the latest technologies and applying my knowledge to real-world problems.""")
st.markdown("""My goal is to build a successful career in Data Analytics, where I can gain practical experience, contribute effectively to an organization, and grow professionally.""")
st.markdown("""<h4 style="color:lightblue">Few Keywords which define me are :- </h4>""",unsafe_allow_html=True)
st.markdown("""
            1. Problem-Solving
            2. Analytical Thinking
            3. Detail-Oriented
            4. Logical Reasoning
            5. Curious Mindset
            6. Time Management""")
#resume...........................................................
st.markdown("""<h4 style="text-align:center"><u>Resume </u></h4>""",unsafe_allow_html=True)

st.header("📄 Resume")

import base64

# Open PDF
with open("RESUME.pdf (2).pdf (1).pdf", "rb") as file:
    pdf_data = file.read()

# ---------------- DOWNLOAD BUTTON ----------------
st.download_button(
    label="⬇️ Download Resume",
    data=pdf_data,
    file_name="Sanya_Katiyar_Resume.pdf",
    mime="application/pdf"
)

# ---------------- PREVIEW ----------------
st.subheader(" View Resume")

base64_pdf = base64.b64encode(pdf_data).decode("utf-8")

pdf_display = f"""
<iframe 
    src="data:application/pdf;base64,{base64_pdf}" 
    width="100%" 
    height="600px" 
    type="application/pdf">
</iframe>
"""

st.markdown(pdf_display, unsafe_allow_html=True)
#intrest.....................
st.markdown("""<h4 style="text-align:center"><e>Area of Interest</e></h4>""",unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# -------- COLUMN 1 --------
with col1:
    st.image("https://img.icons8.com/color/96/data-configuration.png", width=70)
    st.markdown("<p style='text-align:center; font-weight:500;'>Data Analytics</p>", unsafe_allow_html=True)

# -------- COLUMN 2 --------
with col2:
    st.image("https://img.icons8.com/color/96/combo-chart.png", width=70)
    st.markdown("<p style='text-align:center; font-weight:500;'>Data Visualization</p>", unsafe_allow_html=True)

# -------- COLUMN 3 --------
with col3:
    st.image("https://img.icons8.com/color/96/broom.png", width=70)
    st.markdown("<p style='text-align:center; font-weight:500;'>Data Cleaning & Preprocessing</p>", unsafe_allow_html=True)
# 🔹 Project 1
st.markdown("""<h4 style="text-align:center"><e>Projects</e></h4>""",unsafe_allow_html=True)

# ---- CSS for Animated Cards ----
st.markdown("""
<style>
.project-card {
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    background: linear-gradient(135deg, #e0f7ff, #f0f9ff);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transition: 0.3s;
}

.project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# ---- Project 1 ----
st.markdown("""
<div class="project-card">
    <h3>📈 Sales Dashboard (Power BI)</h3>
    <p>Built an interactive dashboard to analyze sales trends, revenue, and performance metrics.</p>
    <a href="https://github.com/" target="_blank">🔗 View on GitHub</a>
</div>
""", unsafe_allow_html=True)

# ---- Project 2 ----
st.markdown("""
<div class="project-card">
    <h3>🧹 Data Cleaning Project (Python)</h3>
    <p>Used Pandas to clean raw datasets, handle missing values, and prepare data for analysis.</p>
    <a href="https://github.com/" target="_blank">🔗 View on GitHub</a>
</div>
""", unsafe_allow_html=True)
#project 3
st.markdown("""
<div class="project-card">
    <h3>🧹 Data Cleaning Project (Python)</h3>
    <p>Used Pandas to clean raw datasets, handle missing values, and prepare data for analysis.</p>
    <a href="https://github.com/" target="_blank">🔗 View on GitHub</a>
</div>
""", unsafe_allow_html=True)
# project 4
st.markdown("""
<div class="project-card">
    <h3>🧹 Data Cleaning Project (Python)</h3>
    <p>Used Pandas to clean raw datasets, handle missing values, and prepare data for analysis.</p>
    <a href="https://github.com/" target="_blank">🔗 View on GitHub</a>
</div>
""", unsafe_allow_html=True)
st.markdown("""<h4 style="text-align:center"><e>Projects</e></h4>""",unsafe_allow_html=True)