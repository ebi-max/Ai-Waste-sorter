import streamlit as st
import pandas as pd

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Waste Sorter",
    page_icon="♻️",
    layout="wide"
)

# =========================
# BRAND CONFIG
# =========================
APP_NAME = "AI Waste Sorter"
TAGLINE = "Smart AI for Sustainable Waste Management"
POWERED_BY = "Ebiklean Global"
FOUNDER = "Ebieme Bassey"

# =========================
# WELCOME / HERO SECTION
# =========================
def show_welcome():
    st.markdown(
        f"""
        <div style="
            padding:25px;
            border-radius:14px;
            background:linear-gradient(90deg,#0d6efd,#198754);
            color:white;
            text-align:center;
            margin-bottom:25px;
        ">
            <h1>{APP_NAME} ♻️</h1>
            <h4>Powered by <b>{POWERED_BY}</b></h4>
            <p>{TAGLINE}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Items Sorted", "1,245")
    col2.metric("AI Accuracy", "91%")
    col3.metric("CO₂ Saved", "2.3 Tons")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Get Started"):
        st.success("Use the sidebar to explore the app")

# =========================
# DEMO MODE (NO AUTH)
# =========================
authentication_status = True
name = f"{FOUNDER} (Demo)"
role = "Admin"

# =========================
# MAIN APP
# =========================
if authentication_status:
    show_welcome()

    st.sidebar.success(f"Welcome {name} ({role})")

    selected = st.sidebar.radio(
        "Menu",
        [
            "Home",
            "Dashboard",
            "Sort Waste",
            "AI Insights",
            "Community",
            "DeepTech Portfolio"
        ]
    )

    # -------------------------
    # HOME
    # -------------------------
    if selected == "Home":
        st.subheader("Recent Activity")
        st.write("♻️ Plastic detected – 92% confidence")
        st.write("🍌 Organic waste detected – 88% confidence")
        st.info("AI Waste Sorter is running smoothly.")

    # -------------------------
    # DASHBOARD
    # -------------------------
    elif selected == "Dashboard":
        st.subheader("Waste Sorting Dashboard")

        df = pd.DataFrame({
            "Waste Type": ["Plastic", "Paper", "Metal", "Organic"],
            "Count": [450, 300, 200, 295]
        })

        st.bar_chart(df.set_index("Waste Type"))

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Sorted", "1,245")
        col2.metric("Recyclable Rate", "72%")
        col3.metric("AI Accuracy", "91%")
        col4.metric("Active Users", "128")

    # -------------------------
    # SORT WASTE
    # -------------------------
    elif selected == "Sort Waste":
        st.subheader("Upload Waste Image")

        image = st.file_uploader("Choose an image (jpg or png)", type=["jpg", "png"])

        if image:
            st.image(image, width=300)

            # Placeholder AI prediction
            predicted_class = "Plastic ♻️"
            confidence = 0.92

            st.success(f"Detected: {predicted_class}")
            st.info(f"Confidence: {confidence * 100:.0f}%")

            st.toast("✅ Item successfully sorted!")

    # -------------------------
    # AI INSIGHTS
    # -------------------------
    elif selected == "AI Insights":
        st.subheader("AI Model Insights")
        st.write("Model Accuracy: 91%")
        st.write("Average Inference Time: 120ms")
        st.write("Model Type: CNN (placeholder)")
        st.info("Future versions will include real-time model analytics.")

    # -------------------------
    # COMMUNITY
    # -------------------------
    elif selected == "Community":
        st.subheader("Community & Leaderboard")

        leaderboard = pd.DataFrame({
            "User": ["Ebieme", "Jane", "Mike"],
            "Points": [25, 12, 18],
            "Badge": ["Eco Hero 🌟", "Eco Starter 🌱", "Recycler Pro 🏆"]
        })

        st.table(leaderboard)

        st.write("💬 Ebieme sorted 5 plastics today")
        st.write("💬 Jane joined the platform")

    # -------------------------
    # DEEPTECH PORTFOLIO
    # -------------------------
    elif selected == "DeepTech Portfolio":
        st.subheader("DeepTech Product Portfolio")

        st.markdown(
            f"""
            ### ♻️ AI Waste Sorter Platform
            **Founder:** {FOUNDER}  
            **Organization:** {POWERED_BY}

            #### 🚩 Problem
            Poor waste segregation leads to pollution, inefficient recycling, and environmental damage.

            #### 💡 Solution
            An AI-powered waste classification system using computer vision to assist
            individuals, communities, and waste managers.

            #### 🧠 Technology Stack
            - Python
            - Streamlit
            - Computer Vision (CNN – placeholder)
            - Data Analytics Dashboard

            #### 💰 Monetization Strategy
            - Licensing to waste management companies
            - Government & NGO environmental contracts
            - API access for smart bins
            - Data insights & analytics services

            #### 🌍 Impact
            - Improved recycling rates
            - Environmental sustainability
            - Youth engagement through gamification

            ---
            **Powered by Ebiklean Global**
            """
        )

# =========================
# FOOTER
# =========================
st.markdown(
    "<hr><center>Powered by <b>Ebiklean Global</b></center>",
    unsafe_allow_html=True
)