import streamlit as st
from services.resume_service import analyze_uploaded_resume
from assets.theme import inject_base_css, sidebar_nav, ring_html, chips_html, require_login

st.set_page_config(page_title="Analyze Resume — ResumeIQ", page_icon="🚀", layout="wide")
inject_base_css()
sidebar_nav(active="upload")
require_login("Log in (or create a free account) to analyze your resume.")

st.markdown('<span class="pill">AI Analysis</span>', unsafe_allow_html=True)
st.markdown('<h1 style="margin:10px 0 4px 0;">Analyze your <span class="agrad">resume</span></h1>', unsafe_allow_html=True)
st.markdown('<p class="subtle">Pick your target role, drop your resume in, and let the AI do the rest.</p>', unsafe_allow_html=True)
st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

with st.container(key="card_upload_form"):
    ic1, ic2 = st.columns([1, 1.4])
    with ic1:
        job_role = st.selectbox(
            "🎯 Target Job",
            [
                "Python Developer",
                "Web Developer",
                "Data Analyst",
                "AI Engineer",
                "Software Engineer",
            ],
        )
    with ic2:
        uploaded_file = st.file_uploader("📎 Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    if st.button("🚀 Analyze Resume", use_container_width=True):
        st.session_state.pop("analysis",None)
        st.session_state["analysis"]=analyze_uploaded_resume(uploaded_file,job_role)

if "analysis" in st.session_state:
    analysis=st.session_state["analysis"]

    

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    st.success("Analysis complete ✅")
    st.markdown("<div style='height:22px'></div>", unsafe_allow_html=True)

    # ---------------- Score rings ---------------- #
    with st.container(key="card_scores"):
        st.markdown('<h3 style="margin-top:0;">Your scores</h3>', unsafe_allow_html=True)
        r1, r2 = st.columns(2)
        with r1:
            st.markdown(
                ring_html(analysis["resume_score"], "Resume Score", color="#8b5cf6", glow="#8b5cf6"),
                unsafe_allow_html=True,
            )
        with r2:
            st.markdown(
                ring_html(analysis["ats_score"], "ATS Score", color="#22d3ee", glow="#22d3ee"),
                unsafe_allow_html=True,
            )

    st.markdown("<div style='height:22px'></div>", unsafe_allow_html=True)

    # ---------------- Strengths / Weaknesses / Missing skills ---------------- #
    g1, g2 = st.columns(2)
    with g1:
        with st.container(key="card_strengths"):
            st.markdown('<h4 style="margin-top:0;">💪 Strengths</h4>', unsafe_allow_html=True)
            st.markdown(chips_html(analysis.get("strengths", []), kind="green", icon="✓"), unsafe_allow_html=True)

    with g2:
        with st.container(key="card_missing"):
            st.markdown('<h4 style="margin-top:0;">🧩 Missing Skills</h4>', unsafe_allow_html=True)
            st.markdown(chips_html(analysis.get("missing_skills", []), kind="red", icon="✕"), unsafe_allow_html=True)

    if analysis.get("weaknesses"):
        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
        with st.container(key="card_weak"):
            st.markdown('<h4 style="margin-top:0;">⚠️ Areas to Improve</h4>', unsafe_allow_html=True)
            st.markdown(chips_html(analysis.get("weaknesses", []), kind="amber", icon="!"), unsafe_allow_html=True)

    st.markdown("<div style='height:22px'></div>", unsafe_allow_html=True)

    # ---------------- Suggestions ---------------- #
    with st.container(key="card_suggestions"):
        st.markdown('<h4 style="margin-top:0;">💡 Suggestions to Improve</h4>', unsafe_allow_html=True)
        for i, s in enumerate(analysis.get("suggestions", []), start=1):
            st.markdown(
                f"""<div style="display:flex; gap:12px; align-items:flex-start; margin-bottom:10px;">
                    <div class="step-num" style="width:28px; height:28px; font-size:0.8rem; flex:none;">{i}</div>
                    <div style="padding-top:3px; color:#dfe2f2;">{s}</div>
                </div>""",
                unsafe_allow_html=True,
            )

    st.markdown("<div style='height:22px'></div>", unsafe_allow_html=True)

    # ---------------- Interview questions ---------------- #
    with st.container(key="card_interview"):
        st.markdown('<h4 style="margin-top:0;">🗣️ Interview Questions to Practice</h4>', unsafe_allow_html=True)
        for i, q in enumerate(analysis.get("interview_questions", []), start=1):
            with st.expander(f"Q{i}. {q}"):
                st.markdown(
                    '<p class="subtle">Take a moment to draft your answer out loud — '
                    'structure it around a real example from your resume.</p>',
                    unsafe_allow_html=True,
                )
else:
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    with st.container(key="card_empty_state"):
        st.markdown(
            """<div style="text-align:center; padding: 18px 0;">
                <div style="font-size:2.4rem;">🗂️</div>
                <div style="font-weight:700; font-size:1.1rem; margin-top:6px; color:#f1f2fa;">
                    No resume uploaded yet
                </div>
                <p class="subtle">Choose a target role and upload a PDF above to get your instant AI breakdown.</p>
            </div>""",
            unsafe_allow_html=True,
        )
