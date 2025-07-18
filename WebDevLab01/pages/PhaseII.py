import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import altair as alt  

with open("data.json", "r") as f:
    data = json.load(f)

st.title("More About Me!")


min_hours = st.slider("Minimum hours spent on hobby", 0, 20, 5)  # NEW
filtered_hobbies = [h for h in data["hobbies"] if h["hours"] >= min_hours]

st.subheader("Hobbies with hours above threshold")
if filtered_hobbies:
    hobby_df = pd.DataFrame(filtered_hobbies)
    st.bar_chart(hobby_df.set_index("name")["hours"])
else:
    st.write("No hobbies meet the minimum hours criteria.")


selected_skill = st.selectbox("Select a programming language to focus on:", list(data["skills"].keys()))  # NEW

st.subheader(f"Skill Level: {selected_skill}")
skill_pct = data["skills"][selected_skill]
fig1, ax1 = plt.subplots()
ax1.pie([skill_pct, 100 - skill_pct], labels=["Proficiency", " "], autopct='%1.1f%%')
st.pyplot(fig1)



show_mood = st.checkbox("Show mood over the week?")  # NEW

if show_mood:
    mood_df = pd.DataFrame(data["mood_over_time"])
    chart = alt.Chart(mood_df).mark_line(point=True).encode(
        x='day',
        y='mood'
    ).properties(title="Mood Over the Week")
    st.altair_chart(chart, use_container_width=True)

if 'click_count' not in st.session_state:
    st.session_state.click_count = 0

if st.button("Click me!"):
    st.session_state.click_count += 1

st.write(f"Button clicked {st.session_state.click_count} times.")
