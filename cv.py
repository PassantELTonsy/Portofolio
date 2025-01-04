# -*- coding: utf-8 -*-
"""CV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/152T3BFX1HG12aR7gX9xUtyH1K0fCuO4q
"""

import streamlit as st
def main():
    st.set_page_config(page_title="Passant El-Tonsy - CV", page_icon=":briefcase:", layout="centered")
    image_path = "photo_2025-01-03_12-05-21.jpg"  

    st.image(image_path, width=200)
    # Header Section
    st.title("Passant El-Tonsy")
    st.markdown("**Aspiring Computer Engineer | Passionate about Machine Learning & Computer Vision**")
    st.write("Cairo, Egypt | +20 1158947220 | [passanteltonsy@gmail.com](mailto:passanteltonsy@gmail.com)")
    st.write("[GitHub](https://github.com/PassantELTonsy) | [LinkedIn](https://www.linkedin.com/in/passant-el-tonsy-a52b42230) | [Kaggle](https://www.kaggle.com/passanteltonsy)")

    # Skills Section
    st.header("Skills")
    skills = [
        "Programming: C++, Java, Python, MATLAB",
        "Machine Learning: Pytorch, Deep Learning, NLP",
        "Data Analysis: Exploratory Data Analysis, Data Cleaning, Data Mining",
        "Software & Systems: Operating Systems, Computer Organization, Network Fundamentals",
        "Other: Technical Report Writing, Time Management, Multitasking"
    ]
  for skill in skills:
    st.markdown(f"- {skill}")
    
    # Education Section
    st.header("Education")
    st.write("**Faculty of Engineering at Shoubra - Benha University**")
    st.write("B.Sc. in Computer Engineering 2020-2025")
    st.write("Current GPA: 2.83")

    # Experience Section
    st.header("Experience")
    st.write("**Team Leader (2024-2025)**")
    st.markdown("- Developed a project timeline and milestones for ML-based projects.")
    st.markdown("- Proposed solutions in Speech Recognition, NLP, and Rendering Avatars.")

    st.write("**Search Quality Rater at RWSGroup (2024)**")
    st.markdown("- Evaluated search results and annotated data.")

    st.write("**Lead Swimming Coach at Go Swimming Academy (2018-present)**")
    st.markdown("- Provided technical instruction and team management.")

    # Projects Section
    st.header("Projects")
    projects = {
        "TALKIN’ HANDS": "Converts spoken Arabic into sign language glosses rendered through a 3D avatar.",
        "Optimized Flight Trip": "Applied AI algorithms to optimize flight itineraries, deployed via Streamlit.",
        "Customer Service Expert System": "Replied to FAQs using Prolog.",
        "Shutter Bug Game": "Developed an interactive 2D game in Processing."
    }
    for project, description in projects.items():
        st.markdown(f"**{project}:** {description}")

    # Courses Section
    st.header("Courses")
    courses = [
        "Data Analysis Challenger Track (Udacity)",
        "Machine Learning Specialization (Andrew Ng)",
        "HCIA Cloud Computing V5.0 (Huawei ICT)",
        "Network Fundamentals (CompTIA Course, Maspero)",
        "NLP Workshop (People of Data)"
    ]
    for course in courses:
        st.markdown(f"- {course}")

    # Languages & Extracurricular Activities
    st.header("Languages")
    st.markdown("- English, German, French")

    st.header("Extracurricular Activities")
    st.write("**Vice President at East Nasr-City Student Union (2015-2018)**")
    st.markdown("- Managed website design, content, and SEO.")
    st.markdown("- Worked on marketing, branding, and logo design.")


if __name__ == "__main__":
    main()

