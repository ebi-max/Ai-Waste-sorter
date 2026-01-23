import streamlit as st
from datetime import datetime
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Waste Sorter",
    layout="wide"
)

# ---------------- LOGIN / PROFILE SYSTEM ----------------
if "user" not in st.session_state:
    st.title("♻️ AI Waste Sorter")
    st.caption("Powered by Ebiklean Global")
    name = st.text_input("Enter your name")
    if st.button("Login") and name.strip():
        st.session_state.user = name.strip()
        st.rerun()
    st.stop()

# ---------------- PROFILE INIT ----------------
if "profile" not in st.session_state:
    st.session_state.profile = {"photo": None,"address": "","dob": "","status": "","education": "","nationality": "","state": "","language": ""}
if "verified" not in st.session_state:
    st.session_state.verified = True
if "stories" not in st.session_state:
    st.session_state.stories = []
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR ----------------
st.sidebar.title("Dashboard")
st.sidebar.write(f"User: {st.session_state.user}")
if st.session_state.verified:
    st.sidebar.success("✔ Verified by Ebiklean Global")

# ---------------- PROFILE FORM ----------------
st.subheader("👤 Edit Profile")
with st.expander("Edit Profile"):
    photo = st.file_uploader("Profile Picture", type=["png","jpg","jpeg"])
    address = st.text_input("Address", st.session_state.profile["address"])
    dob = st.date_input("Date of Birth")
    status = st.text_input("Status", st.session_state.profile["status"])
    education = st.text_input("Education", st.session_state.profile["education"])
    nationality = st.text_input("Nationality", st.session_state.profile["nationality"])
    state = st.text_input("State", st.session_state.profile["state"])
    language = st.text_input("Language", st.session_state.profile["language"])
    if st.button("Save Profile"):
        st.session_state.profile.update({
            "photo": photo or st.session_state.profile["photo"],
            "address": address,
            "dob": str(dob),
            "status": status,
            "education": education,
            "nationality": nationality,
            "state": state,
            "language": language
        })
        st.success("✅ Profile updated successfully")

# ---------------- PUBLIC PROFILE PREVIEW ----------------
show_profile = st.checkbox("Show public profile preview")
if show_profile:
    col1,col2 = st.columns([1,3])
    with col1:
        if st.session_state.profile["photo"]:
            st.image(st.session_state.profile["photo"], width=150)
        else:
            st.image("https://via.placeholder.com/150")
    with col2:
        st.markdown(f"**Name:** {st.session_state.user}")
        if st.session_state.verified:
            st.markdown("✅ Verified by Ebiklean Global")
        st.markdown(f"**Status:** {st.session_state.profile['status']}")
        st.markdown(f"**Education:** {st.session_state.profile['education']}")
        st.markdown(f"**Nationality:** {st.session_state.profile['nationality']}")
        st.markdown(f"**State:** {st.session_state.profile['state']}")
        st.markdown(f"**Language:** {st.session_state.profile['language']}")
    st.info("Sensitive info hidden in public preview.")

# ---------------- STORY SYSTEM ----------------
st.subheader("📖 Post a Story / Status")
with st.expander("Share a new story"):
    story_text = st.text_area("Your story", max_chars=280)
    story_image = st.file_uploader("Optional image", type=["png","jpg","jpeg"])
    if st.button("Post Story"):
        if story_text.strip() or story_image:
            st.session_state.stories.append({
                "user": st.session_state.user,
                "text": story_text.strip(),
                "image": story_image,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            st.success("✅ Story posted")
            st.rerun()
        else:
            st.warning("Add text or image to post story")

# ---------------- STORY FEED ----------------
st.subheader("📰 Story Feed")
if st.session_state.stories:
    for story in reversed(st.session_state.stories):
        st.markdown(f"**{story['user']}** • {story['time']}")
        if story["text"]:
            st.markdown(f"> {story['text']}")
        if story["image"]:
            st.image(story["image"], use_column_width=True)
        st.divider()
else:
    st.info("No stories yet.")

# ---------------- MY POSTS ----------------
st.subheader("📝 My Posts")
my_stories = [s for s in st.session_state.stories if s["user"]==st.session_state.user]
if my_stories:
    for story in reversed(my_stories):
        st.markdown(f"**{story['user']}** • {story['time']}")
        if story["text"]:
            st.markdown(f"> {story['text']}")
        if story["image"]:
            st.image(story["image"], use_column_width=True)
        st.divider()
else:
    st.info("You haven't posted any stories yet.")

# ---------------- AI CHAT ----------------
st.subheader("💬 AI Waste Advisor")
def ai_response(user_text):
    if "plastic" in user_text.lower() or "metal" in user_text.lower():
        return "♻️ Tip: Segregate waste into recyclable and non-recyclable bins."
    return "♻️ Tip: Dispose waste responsibly."

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask AI Waste Advisor")
if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    reply = ai_response(user_input)
    st.session_state.messages.append({"role":"assistant","content":reply})
    st.rerun()

# ---------------- DOWNLOAD REPORT ----------------
st.subheader("⬇️ Download Full Report")
if st.button("Generate Report"):
    report = f"""
Ebiklean Global AI Waste Sorter Report
User: {st.session_state.user}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Verified: {'Yes' if st.session_state.verified else 'No'}

--- Profile ---
Status: {st.session_state.profile['status']}
Education: {st.session_state.profile['education']}
Nationality: {st.session_state.profile['nationality']}
State: {st.session_state.profile['state']}
Language: {st.session_state.profile['language']}

--- Stories ---
"""
    for story in st.session_state.stories:
        report += f"{story['user']} • {story['time']}\n{story['text']}\n\n"

    report += "--- Chat ---\n"
    for msg in st.session_state.messages:
        report += f"{msg['role'].upper()}: {msg['content']}\n\n"

    st.download_button(
        "Download Report",
        report,
        file_name="ai_waste_sorter_report.txt",
        mime="text/plain"
    )

st.caption("© 2026 Ebiklean Global • AI Waste Sorter")