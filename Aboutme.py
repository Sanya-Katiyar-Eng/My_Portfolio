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

#intrest.....................
st.markdown("""<h4 style="text-align:center;color:lightblue"><e>Area of Interest</e></h4>""",unsafe_allow_html=True)

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
st.markdown("""<h4 style="text-align:center;color:lightblue"><e>Projects</e></h4>""",unsafe_allow_html=True)

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

# ---- CLEAN THEME SAFE CSS ----
st.markdown("""
<style>

/* Project Card */
.project-card {
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 18px;

    background: rgba(127, 127, 127, 0.08);  /* soft neutral */
    backdrop-filter: blur(6px);

    border: 1px solid rgba(127, 127, 127, 0.2);

    transition: 0.3s ease;
}

/* Hover (very soft) */
.project-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.1);
}

/* Title */
.project-card h3 {
    margin-bottom: 8px;
    font-size: 20px;
    color: inherit;  /* IMPORTANT */
}

/* Text */
.project-card p {
    font-size: 14px;
    line-height: 1.5;
    color: inherit;  /* IMPORTANT */
    opacity: 0.85;
}

/* Links */
.project-card a {
    display: inline-block;
    margin-top: 6px;
    color: #3b82f6;   /* soft blue */
    font-weight: 500;
    text-decoration: none;
}

.project-card a:hover {
    text-decoration: underline;
}

/* Heading */
.section-title {
    text-align: center;
    margin-bottom: 25px;
    font-size: 28px;
    font-weight: 600;
    color: inherit;
}

</style>
""", unsafe_allow_html=True)



# ---- Project 1 ----
st.markdown("""
<div class="project-card">
    <h3>Interactive Data Visualization Learning Platform</h3>
    <p>Developed an interactive Streamlit app to teach data visualization with real-time plotting and hands-on examples.</p>
    <a href="https://github.com/Sanya-Katiyar-Eng/DV_Full_Course" target="_blank">🔗 GitHub</a><br>
    <a href="https://dvfullcourse-dinshcjap3wxgyekyard49.streamlit.app/" target="_blank">🔗 Live Demo</a>
</div>
""", unsafe_allow_html=True)


# ---- Project 2 ----
st.markdown("""
<div class="project-card">
    <h3>Full-Stack Student Registration System</h3>
    <p>Backend-focused web app with PostgreSQL, supporting CRUD operations and deployed on cloud.</p>
    <a href="https://github.com/Sanya-Katiyar-Eng/first_project_using_cloud_database" target="_blank">🔗 GitHub</a><br>
    <a href="https://first-project-using-cloud-database-pr4a.onrender.com/" target="_blank">🔗 Live Demo</a>
</div>
""", unsafe_allow_html=True)


# ---- Project 3 ----
st.markdown("""
<div class="project-card">
    <h3>EDA & Visualization (Kaggle Dataset)</h3>
    <p>Performed data cleaning, preprocessing, and visualization to extract insights from real-world dataset.</p>
    <a href="https://www.kaggle.com/code/sanyasonikatiyar/notebookbebebed1a6" target="_blank">🔗 View Project</a>
</div>
""", unsafe_allow_html=True)


# ---- Project 4 ----
st.markdown("""
<div class="project-card">
    <h3>Power BI Dashboard</h3>
    <p>Created an interactive dashboard with KPIs and filters for business insights and decision-making.</p>
</div>
""", unsafe_allow_html=True)

















import streamlit as st

st.markdown("""
<style>

/* ===== TITLE ===== */
.skills-title {
    text-align: center;
    font-size: 36px;
    font-weight: 800;
    margin-bottom: 25px;
    color: inherit;
}

/* ===== SECTION CARD ===== */
.skill-section {
    margin: 20px 0;
}

/* ===== GLASS GRID CONTAINER ===== */
.skill-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    justify-content: center;
}

/* ===== SKILL CHIP ===== */
.skill-chip {
    padding: 10px 14px;
    border-radius: 999px;

    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);

    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);

    font-size: 14px;
    font-weight: 500;

    transition: all 0.25s ease-in-out;

    cursor: default;
}

/* Hover effect */
.skill-chip:hover {
    transform: translateY(-4px) scale(1.05);
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    background: rgba(59, 130, 246, 0.15);
    border: 1px solid rgba(59, 130, 246, 0.5);
}

/* Section heading */
.section-heading {
    text-align: center;
    font-size: 22px;
    font-weight: 700;
    margin: 20px 0 12px 0;
    color: inherit;
}

/* Responsive */
@media (max-width: 768px) {
    .skill-chip {
        font-size: 13px;
        padding: 8px 12px;
    }
}

</style>
""", unsafe_allow_html=True)


st.markdown('<div class="skills-title">Skills</div>', unsafe_allow_html=True)


# ---------------- DATA ----------------
technical_skills = [
    " Python",
    " SQL",
    " Power BI",
    " Pandas",
    " NumPy",
    " Matplotlib",
    " Seaborn",
    " Streamlit"
]

tools = [
    " Kaggle",
    " Render",
    " Git",
    " GitHub"
]

soft_skills = [
    " Problem Solving",
    " Analytical Thinking",
    " Time Management",
    " Communication",
    " Attention to Detail"
]


# ---------------- RENDER FUNCTION ----------------
def render_skills(title, skills):
    st.markdown(f'<div class="section-heading">{title}</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-grid">', unsafe_allow_html=True)

    for skill in skills:
        st.markdown(f"<div class='skill-chip'>{skill}</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ---------------- DISPLAY ----------------
render_skills("Technical Skills", technical_skills)
render_skills("Tools & Platforms", tools)
render_skills("Soft Skills", soft_skills)











st.markdown("""
<style>

/* ===== SECTION TITLE ===== */
.cert-title {
    text-align: center;
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 25px;
    color: inherit;
}

/* ===== GRID LAYOUT ===== */
.cert-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 18px;
    padding: 10px;
}

/* ===== CERT CARD ===== */
.cert-card {
    border-radius: 16px;
    overflow: hidden;

    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);

    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);

    box-shadow: 0 8px 25px rgba(0,0,0,0.15);

    transition: all 0.3s ease-in-out;
}

/* Hover effect */
.cert-card:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    border: 1px solid rgba(59, 130, 246, 0.5);
}

/* IMAGE */
.cert-card img {
    width: 100%;
    height: 160px;
    object-fit: cover;
}

/* TEXT */
.cert-content {
    padding: 12px;
}

.cert-content h4 {
    margin: 0;
    font-size: 16px;
    font-weight: 700;
}

.cert-content p {
    font-size: 13px;
    opacity: 0.8;
    margin-top: 5px;
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .cert-grid {
        grid-template-columns: 1fr;
    }
}

</style>
""", unsafe_allow_html=True)


st.markdown('<div class="cert-title"> Certifications </div>', unsafe_allow_html=True)


# ================= CERTIFICATES DATA =================
certificates = [
    {
        "title": "Hackathon Participation",
        "desc": "Participated in college-level hackathon and worked on real-world problem solving.",
        "img": "https://images.unsplash.com/photo-1552664730-d307ca884978"
    },
    {
        "title": "Conference Participation",
        "desc": "Attended technical conference and learned industry-level data science concepts.",
        "img": "https://images.unsplash.com/photo-1505373877841-8d25f7d46678"
    },
    {
        "title": "TATA Job Simulation",
        "desc": "Completed Tata virtual job simulation focused on analytics and business insights.",
        "img": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d"
    }
]


# ================= RENDER CARDS =================
st.markdown('<div class="cert-grid">', unsafe_allow_html=True)

for cert in certificates:
    st.markdown(f"""
    <div class="cert-card">
        <img src="{cert['img']}">
        <div class="cert-content">
            <h4>{cert['title']}</h4>
            <p>{cert['desc']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)











# ================= SECOND ROW ================
st.markdown('<div class="cert-title">Contact </div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

# ===== EMAIL =====
with c1:
    st.markdown("""
    <div style="text-align:center">
        <a href="sanyakatiyar01@gmail.com" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="70">
        </a>
        <p>Email</p>
    </div>
    """, unsafe_allow_html=True)

# ===== LINKEDIN =====
with c2:
    st.markdown("""
    <div style="text-align:center">
        <a href="https://www.linkedin.com/in/sanyakatiyar/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="70">
        </a>
        <p>LinkedIn</p>
    </div>
    """, unsafe_allow_html=True)

# ===== GITHUB =====
with c3:
    st.markdown("""
    <div style="text-align:center">
        <a href="https://github.com/Sanya-Katiyar-Eng" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" width="70">
        </a>
        <p>GitHub</p>
    </div>
    """, unsafe_allow_html=True)