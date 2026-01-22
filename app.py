import streamlit as st
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Waste Sorter",
    page_icon="♻️",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "name" not in st.session_state:
    st.session_state.name = ""

if "scan_count" not in st.session_state:
    st.session_state.scan_count = 0

if "scan_results" not in st.session_state:
    st.session_state.scan_results = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "stories" not in st.session_state:
    st.session_state.stories = [
        {"user": "Alice", "post": "Recycled 5 plastic bottles today! ♻️"},
        {"user": "Bob", "post": "Learned how to separate organic waste."},
    ]

# ---------------- LOGIN SCREEN ----------------
if not st.session_state.logged_in:
    st.title("♻️ AI Waste Sorter")
    st.caption("Sort your waste and learn proper disposal methods")
    st.markdown("**Powered by Ebiklean Global**")

    name = st.text_input("Enter your name")

    if st.button("Login"):
        if name.strip() == "":
            st.warning("Please enter your name to continue.")
        else:
            st.session_state.name = name
            st.session_state.logged_in = True
            st.rerun()

# ---------------- MAIN APP ----------------
else:
    st.sidebar.success(f"Logged in as {st.session_state.name}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.scan_count = 0
        st.session_state.scan_results = []
        st.session_state.chat_history = []
        st.rerun()

    st.title("♻️ AI Waste Sorter")
    st.markdown("**Powered by Ebiklean Global**")

    # ---------------- UPLOAD & CLASSIFY ----------------
    st.subheader("Upload Waste Image for Classification")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        waste_type = st.selectbox(
            "Select predicted waste type (for demo purposes):",
            ["Organic", "Plastic", "Metal", "Glass", "Paper"]
        )

        if st.button("Classify Waste"):
            st.success(f"✅ Classified as: **{waste_type}**")
            st.session_state.scan_count += 1

            scan_entry = {
                "user": st.session_state.name,
                "waste_type": waste_type,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.scan_results.append(scan_entry)

            # ---------------- DOWNLOADABLE REPORT ----------------
            report_lines = [
                "♻️ AI WASTE SORTER REPORT",
                "Powered by Ebiklean Global",
                f"User: {st.session_state.name}",
                "",
                "Scan Results:",
            ]
            for i, r in enumerate(st.session_state.scan_results, 1):
                report_lines.append(f"{i}. {r['waste_type']} at {r['date']}")

            report_lines.append("\nKeep sorting responsibly! 🌍")
            report = "\n".join(report_lines)

            st.download_button(
                label="📥 Download Scan Report",
                data=report,
                file_name="ai_waste_scan_report.txt",
                mime="text/plain"
            )

    st.divider()

    # ---------------- DASHBOARD ----------------
    st.subheader("📊 Waste Sorting Dashboard")
    st.write(f"**Total Scans:** {st.session_state.scan_count}")
    if st.session_state.scan_count > 0:
        st.write("**Recent Scans:**")
        for r in st.session_state.scan_results[-5:]:
            st.write(f"- {r['waste_type']} at {r['date']}")

    st.divider()

    # ---------------- CHAT ----------------
    st.subheader("💬 Ask AI Tips / Chat")
    user_msg = st.text_input("Type your message:")
    if st.button("Send Message"):
        if user_msg.strip():
            response = f"AI Tip: Here's a recycling tip for '{user_msg}'"
            st.session_state.chat_history.append(f"You: {user_msg}")
            st.session_state.chat_history.append(response)

    for msg in st.session_state.chat_history[-10:]:
        st.write(msg)

    st.divider()

    # ---------------- NOTIFICATIONS ----------------
    st.sidebar.subheader("🔔 Notifications")
    notifications = [
        "Remember: Recycle plastic bottles today!",
        "Tip: Organic waste can become compost.",
        "New feature added: Chat with AI Tips."
    ]
    for note in notifications:
        st.sidebar.info(note)

    # ---------------- STORY / FEED ----------------
    st.subheader("📖 Community Story Feed")
    for story in st.session_state.stories[-5:]:
        st.write(f"**{story['user']}**: {story['post']}")

    st.divider()

    # ---------------- INVESTOR / IMPACT ----------------
    st.subheader("💰 Investor & Impact Overview")
    st.write(
        """
        - AI-assisted waste classification improves recycling efficiency  
        - Engaging chat & community feed increase user retention  
        - Scalable for schools, NGOs, and recycling programs  
        - Potential for monetization through local partnerships  
        """
    )