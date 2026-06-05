import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title="My Portfolio")


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
    </div>
""", unsafe_allow_html=True)
col1 , col2=st.columns(2)
with col1:
    st.image("images/me.jpg",width=200)
with col2:
    st.markdown("""<h4 style="color:lightblue"><u>About me </u></h4>""",unsafe_allow_html=True)
    st.markdown("""I am a Computer Science student with a strong interest in Data Analytics and Programming. With a science background, I developed a curiosity for technology at an early stage and have been consistently working to build my skills in this field.""" , unsafe_allow_html=True)
    st.markdown("""I enjoy working with tools like Python, Power BI, and Excel to clean, analyze, and visualize data. Through my projects, I focus on transforming raw data into meaningful insights that can support better decision-making.""")         
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
###project................................................................................
st.markdown("""<h4 style="text-align:center"><u>Projects </u></h4>""",unsafe_allow_html=True)
col1, col2 = st.columns(2)

# 🔹 Project 1
with col1:
    st.markdown("""
    <div style="
        border-radius:15px;
        padding:15px;
        box-shadow: 0 4px 12px rgba(0,0.6,0,0.2);
        background-color:pink;
        text-align:center;
    ">
        <img src="https://via.placeholder.com/300" width="100%" style="border-radius:10px;">
        <h3>Sales Dashboard</h3>
        <p>Built an interactive Power BI dashboard to analyze sales trends and performance.</p>
        <a href="https://github.com/" target="_blank">
            <button style="
                background-color:#001f3f;
                color:white;
                border:none;
                padding:10px 20px;
                border-radius:8px;
                cursor:pointer;
            ">
                🔗 View on GitHub
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# 🔹 Project 2
with col2:
    st.markdown("""
    <div style="
        border-radius:15px;
        padding:15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        background-color:lightgreen;
        text-align:center;
    ">
        <img src="https://via.placeholder.com/300" width="100%" style="border-radius:10px;">
        <h3>Data Cleaning Project</h3>
        <p>Used Python Pandas to clean and preprocess raw datasets for analysis.</p>
        <a href="https://github.com/" target="_blank">
            <button style="
                background-color:#001f3f;
                color:white;
                border:none;
                padding:10px 20px;
                border-radius:8px;
                cursor:pointer;
            ">
                🔗 View on GitHub
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

#Skills...........................................................
st.markdown("""<h4 style="text-align:center"><u>Skills </u></h4>""",unsafe_allow_html=True)
#Contact...........................................................
st.markdown("""<h4 style="text-align:center"><u>Contact </u></h4>""",unsafe_allow_html=True)