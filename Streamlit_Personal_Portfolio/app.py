from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "MLH Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

PAGE_TITLE = "Digital CV | Yellanki Ekanth Sai Sundar"
PAGE_ICON = ":wave:"
NAME = "Yellanki Ekanth Sai Sundar"
DESCRIPTION = """
2nd year B.Tech student at Gokaraju Rangaraju Instiute of Engineering and Technology. \nAssistant Manager of Technical Team at Advanced Academic Center
"""
EMAIL = "ekanthsai.yellanki@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ekanth-sai-yellanki-3303742a2/",
    "GitHub": "https://github.com/Ekanth-Sai",
}
PROJECTS = {
    "🏆 Text Summarization and Information Extraction": "https://github.com/Ekanth-Sai/Text-Summarization-and-information-extraction",
    "🏆 Autonomous Car Driving Simulator": "https://github.com/AAC-Open-Source-Pool/Autonomous-Car-Driving-using-CNN",
    "🏆 Wine Quality Index": "https://github.com/Ekanth-Sai/Wine-Quality-Index"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Multiple Project Experience in Machine Learning and Deep Learning Field. Teaching experience in the mentioned domains
- ✔️ Strong hands on experience and knowledge in Python, Java, and C language. 
- ✔️ Proficient with front end technologies like HTML, CSS, JS and streamlit application of python. Has experience with SpringBoot Micro-Services and MySQL and PostgressSQL database. 
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, Java, C Language, Spring Boot microservices
- 📊 Data Visulization: Microsoft Excel, matplotlib
- 📚 Modeling: Logistic regression, linear regression, decision trees, Support Vector Machines
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)

st.write('\n')
st.subheader("Projects & Accomplishments")
#st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")