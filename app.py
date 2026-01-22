import streamlit as st
from datetime import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI Waste Sorter", page_icon="♻️", layout="centered")

# ---------------- SESSION STATE ----------------
for key, default in {
    "logged_in": False,
    "name": "",
    "scan_count": 0,
    "chat": [],
    "leaderboard": {},
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ---------------- LOGIN ----------------
if not st.session_state.logged_in:
    st.title("♻️ AI Waste Sorter")
    st.markdown("**Powered by Ebiklean Global**")
    name = st.text_input("Enter your name")

    if st.button("Login"):
        if name.strip():
            st.session_state.logged_in = True
            st.session_state.name = name
            st.experimental_rerun()
        else:
            st.warning("Name required")
    st.stop()

# ---------------- SIDEBAR ----------------
st.sidebar.success(f"👤 {st.session_state.name}")

st.sidebar.subheader("🔔 Notifications")
notifications = [
    "♻️ Sort waste correctly to save the planet",
    "🌍 New feature: Community leaderboard",
    "💬 Chat now available"
]
for n in notifications:
    st.sidebar.info(n)

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.experimental_rerun()

# ---------------- MAIN ----------------
st.title("♻️ AI Waste Sorter")
st.caption("Smart waste classification & community learning")
st.markdown("**Powered by Ebiklean Global**")

# ---------------- CLASSIFICATION ----------------
st.subheader("📸 Waste Classification")
waste_type = st.selectbox(
    "Select waste type (demo):",
    ["Plastic", "Organic", "Metal", "Glass", "Paper"]
)

if st.button("Classify"):
    st.success(f"✅ Classified as {waste_type}")
    st.session_state.scan_count += 1

    # leaderboard scoring
    st.session_state.leaderboard.setdefault(st.session_state.name, 0)
    st.session_state.leaderboard[st.session_state.name] += 10

# ---------------- CHAT ----------------
st.divider()
st.subheader("💬 Community Chat")

msg = st.text_input("Say something about recycling")
if st.button("Send"):
    if msg.strip():
        st.session_state.chat.append(f"🧑 {st.session_state.name}: {msg}")
        st.session_state.chat.append("🤖 AI: Great job helping the environment!")

for c in st.session_state.chat[-8:]:
    st.write(c)

# ---------------- LEADERBOARD ----------------
st.divider()
st.subheader("🏆 Leaderboard")

if st.session_state.leaderboard:
    sorted_lb = sorted(
        st.session_state.leaderboard.items(),
        key=lambda x: x[1],
        reverse=True
    )
    for i, (user, score) in enumerate(sorted_lb[:5], 1):
        st.write(f"{i}. **{user}** — {score} pts")
else:
    st.info("No scores yet. Start classifying!")

# ---------------- DOWNLOAD ----------------
st.divider()
report = f"""
AI WASTE SORTER REPORT
Powered by Ebiklean Global

User: {st.session_state.name}
Total Scans: {st.session_state.scan_count}
Score: {st.session_state.leaderboard.get(st.session_state.name, 0)}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""

st.download_button(
    "📥 Download Report",
    report,
    file_name="ai_waste_sorter_report.txt"
)

# ---------------- IMPACT ----------------
st.divider()
st.subheader("💰 Investor & Impact")
st.write("""
• Gamified recycling education  
• Community-driven engagement  
• Scalable across schools & cities  
""")