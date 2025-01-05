# -*- coding: utf-8 -*-
"""CV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/152T3BFX1HG12aR7gX9xUtyH1K0fCuO4q
"""

import streamlit as st
def main():
    st.set_page_config(page_title="Passant El-Tonsy - CV", page_icon=":briefcase:", layout="centered")
    image_path = "cropped_image.png"
    st.image(image_path, width=200)
    
    # Header Section
    st.title("Passant El-Tonsy")
    st.markdown("**Aspiring Computer Engineer | Passionate about Machine Learning & Computer Vision| Data Annotation Specialist | Former EOI'2018**")
    st.write("Cairo, Egypt | +20 1158947220 ")
    st.write("[passanteltonsy@gmail.com](mailto:passanteltonsy@gmail.com)")
    st.write("[GitHub](https://github.com/PassantELTonsy) | [LinkedIn](https://www.linkedin.com/in/passant-el-tonsy-a52b42230) | [Kaggle](https://www.kaggle.com/passanteltonsy)")

    # Skills Section
    st.header("Skills")
    skills = [
        "**Programming**: C++, Java, Python, MATLAB, OOP, Data Structure",
        "**Machine Learning**: Neural Network, Pytorch, Deep Learning, NLP,Probability & Statistics , Discrete Mathematics",
        "**Data Analysis**: Exploratory Data Analysis, Data Cleaning, Data Mining, Text Preprocessing ",
        "**Software & Systems**: Software Engineering, Operating Systems, Computer Organization, Network Fundamentals",
        "**Soft Skills**: Self Learning, Technical Report Writing, Time Management, Multitasking"
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
        
        "Optimized Flight Trip": {
            "description": "This Project explores the application of AI searching algorithms e.g. BFS-DFS-A*-Greedy-UCS-IDS-DLS in optimizing flight trip planning. By harnessing the power of AI, we aim to develop a system capable of efficiently navigating complex flight networks to identify the most cost-effective and time-efficient routes. This project not only delves into the technical aspects of AI algorithms but also examines their real-world implications for travellers, airlines, and the broader travel industry.",
            "image":"Optimized flight Trip Poster.png",
            "video": "DEMO.mp4" ,  
           
        },
        "Event Registeration System": {
            "description": "The Event Registration System is designed to provide a comprehensive platform for managing events. Check Documentation HERE:https://drive.google.com/file/d/1pI7TWLScOuNfzwQFEXDGSs60WIyoQGSi/view?usp=drive_link",
            "image":"photo_2025-01-05_14-49-08.jpg",
            "video": None ,  
           
        },
        
         
        
        "TALKIN’ HANDS": {
            "description": "Converts spoken Arabic into sign language glosses rendered through a 3D avatar.",
            "image":None,
            "video":None
        },
       
        "Customer Service Expert System": {
            "description": "Replied to FAQs using Prolog.",
            "image":None,
            "video":"Customer Service Support Demo.mp4"
            
        },
        "Shutter Bug Game": {
            "description": "Developed an interactive 2D game in Processing.",  
            "video": "ShutterBugDemo.mp4" ,
            "image":None

        }
    }

    selected_project = st.selectbox("Select a project", list(projects.keys()))
    
    # Display the description and content (image/video) of the selected project
    if selected_project:
        st.write(f"**{selected_project}:** {projects[selected_project]['description']}")
        # Show the image if available
        if projects[selected_project]["image"]:
            st.image(projects[selected_project]["image"], width=400)  

        # Show the video if available
        if projects[selected_project]["video"]:
            st.video(projects[selected_project]["video"], format="video/mp4")







    
    
    # Courses Section
    st.header("Courses&Certificates")
    courses = [
        "Data Analysis Challenger Track (Udacity)",
        "**Machine Learning Specialization (Andrew Ng)**\nhttps://coursera.org/share/a97b04775f9d1d501fee1292f38ab285",
        "**Advanced Learning Algorithms**\nhttps://coursera.org/share/3090067024e664421f7daf295017f556"
        "**HCIA Cloud Computing V5.0 (Huawei ICT):**\nhttps://drive.google.com/file/d/10xjtHSDiFPDHQVtj2-UJa8yhc7pBnG5N/view?usp=sharing",
        "**Network Fundamentals (CompTIA Course, Maspero)**\nhttps://drive.google.com/file/d/1SQgRn047nTbwnAI3Md3XvWa1WoPQRK_T/view?usp=sharing",
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

