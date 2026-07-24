import streamlit as st
from assets.theme import inject_base_css, sidebar_nav, require_login

st.set_page_config(page_title="Dashboard — ResumeIQ", page_icon="📊", layout="wide")
inject_base_css()
sidebar_nav(active="dashboard")
require_login("Log in to see your dashboard, saved scores and quick actions.")

st.markdown('<span class="pill">Dashboard</span>', unsafe_allow_html=True)
st.markdown(
    f'<h1 style="margin:10px 0 4px 0;">Welcome back, <span class="agrad">{st.session_state["user_name"]}</span> 👋</h1>',
    unsafe_allow_html=True,
)
st.markdown('<p class="subtle">Here\'s a snapshot of your resume activity.</p>', unsafe_allow_html=True)
st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("📤 Uploaded Resumes", "0")
with col2:
    st.metric("📈 Average ATS", "--")
with col3:
    st.metric("🏆 Highest Score", "--")

st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)
st.markdown('<h3>Quick Actions</h3>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    with st.container(key="card_qa_upload"):
        st.markdown(
            """<div style="font-size:1.7rem;">📤</div>
            <div style="font-weight:700; font-size:1.05rem; margin:6px 0 4px 0;">Upload a Resume</div>
            <p class="subtle" style="font-size:0.88rem;">Get a fresh AI breakdown, ATS score and suggestions in seconds.</p>""",
            unsafe_allow_html=True,
        )
        if st.button("📤 Upload Resume", key="btn_upload", use_container_width=True):
            st.switch_page("pages/4_Upload_Resume.py")

with c2:
    with st.container(key="card_qa_logout"):
        st.markdown(
            """<div style="font-size:1.7rem;">🚪</div>
            <div style="font-weight:700; font-size:1.05rem; margin:6px 0 4px 0;">Sign Out</div>
            <p class="subtle" style="font-size:0.88rem;">Done for now? Log out securely from this device.</p>""",
            unsafe_allow_html=True,
        )
        with st.container(key="ghost_logout_dash"):
            if st.button("🚪 Logout", key="btn_logout", use_container_width=True):
                st.session_state.clear()
                st.success("Logged out successfully!")
                st.rerun()
