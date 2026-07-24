import streamlit as st
from assets.theme import inject_base_css, sidebar_nav

st.set_page_config(
    page_title="ResumeIQ — AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_base_css()
sidebar_nav(active="home")

# ------------------------------------------------------------------ #
# Hero
# ------------------------------------------------------------------ #
with st.container(key="hero_main"):
    c1, c2 = st.columns([1.3, 1], vertical_alignment="center")
    with c1:
        st.markdown('<span class="pill">✨ Powered by Gemini AI</span>', unsafe_allow_html=True)
        st.markdown(
            """
            <h1 style="font-size:3.1rem; line-height:1.12; margin:14px 0 10px 0;">
                Land your next job with a
                <span class="agrad">resume that actually gets read</span>
            </h1>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """<p style="font-size:1.08rem; color:#aeb4cc; max-width:560px;">
            Upload your resume, tell us the role you're chasing, and let AI score it,
            find your gaps, and hand you an interview‑ready game plan — in seconds.
            </p>""",
            unsafe_allow_html=True,
        )
        b1, b2, _ = st.columns([1, 1, 2])
        logged_in = st.session_state.get("logged_in")
        with b1:
            label = "🚀 Analyze Resume" if logged_in else "🚀 Get Started"
            target = "pages/4_Upload_Resume.py" if logged_in else "pages/1_Register.py"
            if st.button(label, key="cta_start", use_container_width=True):
                st.switch_page(target)
        with b2:
            with st.container(key="ghost_login_cta"):
                if logged_in:
                    if st.button("📊 Dashboard", key="cta_login", use_container_width=True):
                        st.switch_page("pages/3_Dashboard.py")
                else:
                    if st.button("🔐 Login", key="cta_login", use_container_width=True):
                        st.switch_page("pages/2_Login.py")
    with c2:
        st.markdown(
            """
            <div style="display:flex; justify-content:center; gap:18px;">
                <div class="ring" style="--pct:87; --ring-color:#8b5cf6; --ring-glow:#8b5cf6;">
                    <div class="ring-inner">
                        <div class="ring-value">87</div>
                        <div class="ring-max">Resume</div>
                    </div>
                </div>
                <div class="ring" style="--pct:92; --ring-color:#22d3ee; --ring-glow:#22d3ee; margin-top:34px;">
                    <div class="ring-inner">
                        <div class="ring-value">92</div>
                        <div class="ring-max">ATS</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("<div style='height:34px'></div>", unsafe_allow_html=True)

# ------------------------------------------------------------------ #
# Stats strip
# ------------------------------------------------------------------ #
s1, s2, s3, s4 = st.columns(4)
stats = [
    ("⚡", "12s", "Avg. analysis time"),
    ("📈", "95%", "ATS pass‑rate boost"),
    ("🧠", "6", "Insight categories"),
    ("🎯", "24/7", "Always‑on feedback"),
]
for i, (col, (icon, val, label)) in enumerate(zip([s1, s2, s3, s4], stats)):
    with col:
        with st.container(key=f"card_stat_{i}"):
            st.markdown(
                f"""<div style="text-align:center;">
                    <div style="font-size:1.6rem;">{icon}</div>
                    <div class="agrad" style="font-size:1.7rem; font-weight:700;">{val}</div>
                    <div class="subtle" style="font-size:0.85rem;">{label}</div>
                </div>""",
                unsafe_allow_html=True,
            )

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

# ------------------------------------------------------------------ #
# Features
# ------------------------------------------------------------------ #
st.markdown('<h2 style="text-align:center;">Everything your job search needs, <span class="agrad">in one pass</span></h2>', unsafe_allow_html=True)
st.markdown('<p class="subtle" style="text-align:center;">One upload. A full breakdown of where you stand.</p>', unsafe_allow_html=True)
st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

features = [
    ("📤", "Upload PDF or DOCX", "Drop in your resume in whatever format you already have."),
    ("🤖", "AI Deep Analysis", "Gemini reads your resume the way a recruiter would."),
    ("🎯", "ATS Score", "See how applicant tracking systems will actually score you."),
    ("🧩", "Missing Skills", "Instantly spot the keywords and skills your target role expects."),
    ("💡", "Smart Suggestions", "Concrete, actionable edits — not generic advice."),
    ("🗣️", "Interview Questions", "Practice with questions tailored to your resume & role."),
]
cols = st.columns(3)
for i, (icon, title, desc) in enumerate(features):
    with cols[i % 3]:
        with st.container(key=f"card_feat_{i}"):
            st.markdown(
                f"""
                <div style="font-size:1.9rem;">{icon}</div>
                <div style="font-weight:700; font-size:1.08rem; margin:8px 0 4px 0; color:#f1f2fa;">{title}</div>
                <div class="subtle" style="font-size:0.9rem;">{desc}</div>
                """,
                unsafe_allow_html=True,
            )

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

# ------------------------------------------------------------------ #
# How it works
# ------------------------------------------------------------------ #
st.markdown('<h2 style="text-align:center;">How it <span class="agrad">works</span></h2>', unsafe_allow_html=True)
st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

steps = [
    ("1", "Create your account", "Quick sign up — no spam, just results."),
    ("2", "Upload your resume", "Pick your target role and drop your file in."),
    ("3", "Get your breakdown", "Scores, gaps, suggestions & interview prep instantly."),
]
cols = st.columns(3)
for col, (num, title, desc) in zip(cols, steps):
    with col:
        with st.container(key=f"card_step_{num}"):
            st.markdown(
                f"""
                <div class="step-num">{num}</div>
                <div style="font-weight:700; font-size:1.05rem; margin:10px 0 4px 0; color:#f1f2fa;">{title}</div>
                <div class="subtle" style="font-size:0.9rem;">{desc}</div>
                """,
                unsafe_allow_html=True,
            )

st.markdown("<div style='height:44px'></div>", unsafe_allow_html=True)

with st.container(key="hero_cta"):
    cc1, cc2 = st.columns([2, 1], vertical_alignment="center")
    with cc1:
        st.markdown(
            '<h3 style="margin:0;">Ready to see where your resume really stands?</h3>'
            '<p class="subtle" style="margin-top:6px;">It takes less than a minute to find out.</p>',
            unsafe_allow_html=True,
        )
    with cc2:
        if st.session_state.get("logged_in"):
            if st.button("Analyze My Resume →", key="cta_bottom", use_container_width=True):
                st.switch_page("pages/4_Upload_Resume.py")
        else:
            if st.button("Get Started Free →", key="cta_bottom", use_container_width=True):
                st.switch_page("pages/1_Register.py")

st.markdown(
    """<div style="text-align:center; margin-top:50px; padding-bottom:14px;" class="subtle">
    Built with 💜 for job seekers — ResumeIQ
    </div>""",
    unsafe_allow_html=True,
)
