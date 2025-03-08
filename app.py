import streamlit as st
import random
import datetime

# Growth mindset quotes
quotes = [
    "**Failure is simply the opportunity to begin again, this time more intelligently.**",
    "**Your only limit is your mind.**",
    "**The secret of getting ahead is getting started.**",
    "**Mistakes are proof that you are trying.**",
    "**Do not be embarrassed by your failures, learn from them and start again.**",
    "**A comfort zone is a beautiful place, but nothing ever grows there.**",
    "**Growth and comfort do not coexist.**",
    "**Believe you can, and you’re halfway there.**"
]

# Growth mindset challenges
challenges = [
    "**Write down 3 things you learned today.**",
    "**Step out of your comfort zone today.**",
    "**Turn a mistake into a learning opportunity.**",
    "**Give yourself positive self-talk for 5.**",
    "**Help someone without expecting anything in return.**"
]

# completed task
if "completed_tasks" not in st.session_state:
    st.session_state.completed_tasks = []

st.title("🌱 Growth Mindset App")
st.subheader("Start your day with motivation!")

# Display a random quote
if st.button("✨ Get Motivation"):
    st.write(random.choice(quotes))

# Display a daily challenge
st.subheader("💡 Daily Growth Challenge")
st.write(random.choice(challenges))

# Goal Setting
st.subheader("🎯 Set Your Goal")
goal = st.text_input("What is one goal you are working on?")
if goal:
    st.success(f"That's amazing! Keep pushing towards: {goal} 💪")

# Progress Tracker
st.subheader("✅ Track Your Progress")
task = st.text_input("Write a small task you completed today:")
if st.button("Mark as Completed"):
    if task:
        st.session_state.completed_tasks.append(task)
        st.success(f"Great job! Task added: {task}")

# Show completed tasks
if st.session_state.completed_tasks:
    st.write("### ✅ Completed Tasks")
    for t in st.session_state.completed_tasks:
        st.write(f"- {t}")

 # Create a checkbox list for tasks
    tasks_to_delete = st.multiselect(
        "Select tasks to delete:", st.session_state.completed_tasks
    )

# Delete selected tasks
    if st.button("❌ Delete Selected Tasks"):
        st.session_state.completed_tasks = [
            t for t in st.session_state.completed_tasks if t not in tasks_to_delete
        ]
        st.success("Selected tasks have been deleted! ✅")
        st.rerun()

# Journaling Feature
st.subheader("📖 Growth Mindset Journal")
journal_entry = st.text_area("Write about your learning today:")
if st.button("Save Entry"):
    if journal_entry:
        today = datetime.date.today()
        with open("journal.txt", "a") as f:
            f.write(f"{today}: {journal_entry}\n")
        st.success("Journal entry saved! 📝")

st.subheader("🌟 Stay Inspired!")


# Footer Section
st.markdown("---", unsafe_allow_html=True)
st.markdown(
    "<h6 style='text-align: center;'>👨‍💻 Created by <b>Subha Sajjad</b></h6>", 
    unsafe_allow_html=True
)


