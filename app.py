import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import pandas as pd
from PIL import Image

# ===== BRAND CONFIG =====
APP_NAME = "AI Waste Sorter"
TAGLINE = "Smart AI for Sustainable Waste Management"
POWERED_BY = "Ebiklean Global"

# ===== DEMO MODE SWITCH =====
DEMO_MODE = True

# ===== PAGE CONFIG =====
st.set_page_config(page_title="AI Waste Sorter", layout="wide")

# ===== WELCOME / HERO SECTION =====
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
        st.success("Select a feature from the sidebar to begin")

# ===== FOOTER / BRANDING =====
def add_footer():
    st.markdown("<hr><center>Powered by <b>Ebiklean Global</b></center>", unsafe_allow_html=True)
add_footer()

# ===== LOAD USERS =====
with open('auth/users.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

# ===== LOGIN (Sidebar) =====
if DEMO_MODE:
    authentication_status = True
    name = "Ebieme Bassey (Demo)"
    username = "ebieme"
else:
    name, authentication_status, username = authenticator.login("Login", "main")

# ===== INITIALIZE SESSION STATE =====
if "points" not in st.session_state:
    st.session_state.points = 0
if "badge" not in st.session_state:
    st.session_state.badge = "Novice Recycler"

# ===== POINTS & BADGES =====
def update_points(points_earned):
    st.session_state.points += points_earned
    if st.session_state.points >= 20:
        st.session_state.badge = "Eco Hero 🌟"
    elif st.session_state.points >= 10:
        st.session_state.badge = "Recycler Pro 🏆"
    elif st.session_state.points >= 5:
        st.session_state.badge = "Eco Starter 🌱"

# ===== AUTHENTICATED USER =====
if authentication_status:
    show_welcome()
    user_info = config['credentials']['usernames'][username]
    role = user_info.get('role', 'user')

    if not DEMO_MODE:
        authenticator.logout("Logout", "sidebar")

    st.sidebar.success(f"Welcome {name} ({role})")

    selected = st.sidebar.radio(
        "Menu",
        ["Home","Dashboard","Sort Waste","AI Insights","Community","DeepTech Portfolio","Admin"]
    )

    # Logout button in sidebar
    if not DEMO_MODE:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Welcome {name} ({role})")

    # ===== SIDEBAR MENU =====
    selected = st.sidebar.radio("Menu", ["Home","Dashboard","Sort Waste","AI Insights","Community","Admin"])

    # ---------- HOME ----------
    if selected == "Home":
        st.subheader("Recent Activity")
        st.write("Plastic ♻️ - 92% confidence")
        st.write("Organic 🍌 - 88% confidence")

    # ---------- DASHBOARD ----------
    elif selected == "Dashboard":
        st.subheader("Waste Statistics")
        df = pd.DataFrame({"Waste":["Plastic","Paper","Metal","Organic"],"Count":[450,300,200,295]})
        st.bar_chart(df.set_index("Waste"))
        col1,col2,col3,col4 = st.columns(4)
        col1.metric("Total Sorted","1,245")
        col2.metric("Recyclable","72%")
        col3.metric("AI Accuracy","91%")
        col4.metric("Active Users","128")

    # ---------- SORT WASTE ----------
    elif selected == "Sort Waste":
        st.subheader("Upload Waste Image")
        image = st.file_uploader("Choose image", type=["jpg","png"])
        if image:
            st.image(image,width=250)

            # =========================
            # PLACEHOLDER FOR AI MODEL
            # =========================
            predicted_class = "Plastic ♻️"  
            confidence = 0.92
            st.success(f"Detected: {predicted_class} ({confidence*100:.0f}%)")

            # ===== GAMIFICATION =====
            points_earned = 1
            update_points(points_earned)
            st.info(f"Points earned: +{points_earned}")
            st.success(f"Total Points: {st.session_state.points}")
            st.success(f"Badge: {st.session_state.badge}")

    # ---------- AI INSIGHTS ----------
    elif selected == "AI Insights":
        st.subheader("Model Insights")
        st.write("Accuracy: 91%")
        st.write("Inference Time: 120ms")
        st.write("Placeholder: You can add your AI metrics here")

    # ---------- COMMUNITY ----------
    elif selected == "Community":
        st.subheader("Community Feed & Leaderboard")
        leaderboard = pd.DataFrame({
            "User":["Ebieme","Jane","Mike"],
            "Points":[st.session_state.points,8,12],
            "Badge":[st.session_state.badge,"Eco Starter 🌱","Recycler Pro 🏆"]
        })
        st.table(leaderboard)
        st.write("Ebieme: Sorted 15 plastics today ♻️")
        st.write("Jane: Sorted 8 items ♻️")

    # ---------- ADMIN ----------
    elif selected == "Admin":
        if role=="admin":
            st.subheader("Admin Dashboard")
            st.write("Manage users, view reports, download analytics")
        else:
            st.warning("Access Denied")

elif authentication_status is False:
    st.error("Invalid email or password")
elif authentication_status is None:
    st.warning("Please login")