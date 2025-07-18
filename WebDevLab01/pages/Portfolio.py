
import streamlit as st
import pandas as pd
import info

def about_me_section():
    st.header("About Me")
    st.image(info.profile_picture, width=200)
    st.write(info.about_me)
    st.write("---")

about_me_section()

def links_section():
    st.sidebar.header("Links")
    for url, icon, label in [
        (info.linkedin_url, info.linkedin_icon, "LinkedIn"),
        (info.github_url, info.github_icon, "GitHub"),
        (f"mailto:{info.email}", info.email_icon, "Email"),
    ]:
        link_html = f'<a href="{url}"><img src="{icon}" width="75" height="75"></a>'
        st.sidebar.markdown(link_html, unsafe_allow_html=True)

links_section()


def education_section():
    st.header("Education")
    ed = info.education_data
    st.subheader(ed["institution"])
    st.write(f"**Degree:** {ed['degree']}")
    st.write(f"**Graduation Date:** {ed['graduation_date']}")
    st.write(f"**GPA:** {ed['GPA']}")
    st.write("")

    st.write("**Relevant Coursework**")
    df = pd.DataFrame(info.course_data)
    st.dataframe(df, column_config={
        "code": "Course Code",
        "name": "Course Name",
        "semester taken": "Semester Taken",
        "skills": "What I Learned"
    }, hide_index=True)
    st.write("")

education_section()


def experience_section():
    st.header("Professional Experience")
    for title, (desc_list, img) in info.experience_data.items():
        with st.expander(title):
            st.image(img, width=250)
            for d in desc_list:
                st.write(f"- {d}")
    st.write("")

experience_section()



def projects_section():
    st.header("Projects")
    for title, desc in info.projects_data.items():
        with st.expander(title):
            st.write(desc)
    st.write("")

projects_section()

def skills_section():
    st.header("Skills")
    st.subheader("Programming Languages")
    for lang, pct in info.programming_data.items():
        st.write(f"{lang} {info.programming_icons.get(lang,'')}")
        st.progress(pct)
    st.write("")
    st.subheader("Spoken Languages")
    for lang, pct in info.spoken_data.items():
        st.write(f"{lang} {info.spoken_icons.get(lang,'')} – {pct}%")
    st.write("")

skills_section()

def activities_section():
    st.header("Activities")
    tabs = st.tabs(["Leadership", "Community Service"])
    with tabs[0]:
        st.subheader("Leadership")
        for title, (details, img) in info.leadership_data.items():
            with st.expander(title):
                st.image(img, width=250)
                for d in details:
                    st.write(f"- {d}")
    with tabs[1]:
        st.subheader("Community Service")
        for detail in info.activity_data["Community Service"]:
            with st.expander("Community Service"):
                st.write(f"- {detail}")
    st.write("")

activities_section()
