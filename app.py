import streamlit as st
from datetime import datetime

st.set_page_config(page_title="AI Waste Sorter", layout="wide")

# ---------------- LOGIN ----------------
if "user" not in st.session_state:
    st.title("♻️ AI Waste Sorter")
    st.caption("Powered by Ebiklean Global")
    name = st.text_input("Enter your name")
    if st.button("Login") and name.strip():
        st.session_state.user = name.strip()
        st.rerun()
    st.stop()

# ---------------- PROFILE ----------------
if "profile" not in st.session_state:
    st.session_state.profile = {"photo": None,"address": "","dob": "","status": "","education": "","nationality": "","state": "","language": ""}
if "verified" not in st.session_state:
    st.session_state.verified = True
if "stories" not in st.session_state:
    st.session_state.stories = []
if "messages" not in st.session_state:
    st.session_state.messages = []
if "friends" not in st.session_state:
    st.session_state.friends = []
if "friend_requests" not in st.session_state:
    st.session_state.friend_requests = []
if "reels" not in st.session_state:
    st.session_state.reels = []

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

# ---------------- PUBLIC PROFILE ----------------
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

# ---------------- FRIEND SYSTEM ----------------
st.subheader("🤝 Friends")
friend_name = st.text_input("Enter friend's name to send request")
if st.button("Send Friend Request") and friend_name.strip():
    st.session_state.friend_requests.append({"from": st.session_state.user, "to": friend_name.strip()})
    st.success(f"Friend request sent to {friend_name.strip()}")

st.subheader("📨 Incoming Friend Requests")
for req in st.session_state.friend_requests:
    if req["to"] == st.session_state.user:
        col1, col2 = st.columns(2)
        col1.write(f"{req['from']} wants to be friends")
        if col2.button(f"Accept {req['from']}"):
            st.session_state.friends.append(req['from'])
            st.session_state.friend_requests.remove(req)
            st.success(f"You are now friends with {req['from']}")
        if col2.button(f"Reject {req['from']}"):
            st.session_state.friend_requests.remove(req)
            st.info(f"Rejected {req['from']}")

st.subheader("👥 Friend List")
if st.session_state.friends:
    st.write(", ".join(st.session_state.friends))
else:
    st.info("You have no friends yet")

# ---------------- LIVE CHAT ----------------
st.subheader("💬 Live Chat with Friends")
if st.session_state.friends:
    friend = st.selectbox("Select a friend to chat with", st.session_state.friends)
    if friend:
        if f"chat_with_{friend}" not in st.session_state:
            st.session_state[f"chat_with_{friend}"] = []
        for msg in st.session_state[f"chat_with_{friend}"]:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
        user_input = st.chat_input(f"Message {friend}")
        if user_input:
            st.session_state[f"chat_with_{friend}"].append({"role": "user", "content": user_input})
            st.session_state[f"chat_with_{friend}"].append({"role": "friend", "content": f"Simulated reply to {user_input}"})
            st.rerun()
else:
    st.info("Add friends to start live chat")

# ---------------- LIVE VIDEO ----------------
st.subheader("🎥 Live Video")
video_file = st.file_uploader("Upload short video or simulate live", type=["mp4","mov"])
if video_file:
    st.video(video_file)

# ---------------- REELS ----------------
st.subheader("📽️ Reels / Short Videos")
reel_file = st.file_uploader("Upload Reel", type=["mp4","mov"])
if st.button("Upload Reel") and reel_file:
    st.session_state.reels.append({"user": st.session_state.user, "video": reel_file})
    st.success("Reel uploaded!")

for r in reversed(st.session_state.reels):
    st.markdown(f"**{r['user']}**")
    st.video(r["video"])
    st.divider()

# ---------------- AI CHAT ----------------
st.subheader("💬 AI Waste Assistant")
def ai_response(user_text):
    if "plastic" in user_text.lower():
        return "♻️ Tip: Recycle plastics properly and avoid single-use plastics."
    if "organic" in user_text.lower():
        return "♻️ Tip: Compost organic waste to reduce landfill."
    return "♻️ Tip: Sort waste into categories to reduce pollution."

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask AI Waste Assistant")
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

    report += "--- Friends ---\n"
    report += ", ".join(st.session_state.friends) + "\n\n"

    report += "--- Chat ---\n"
    for msg in st.session_state.messages:
        report += f"{msg['role'].upper()}: {msg['content']}\n\n"

    report += "--- Reels ---\n"
    for r in st.session_state.reels:
        report += f"{r['user']} uploaded a reel\n"

    st.download_button(
        "Download Report",
        report,
        file_name="ai_waste_sorter_full_report.txt",
        mime="text/plain"
    )

st.caption("© 2026 Ebiklean Global • AI Waste Sorter")