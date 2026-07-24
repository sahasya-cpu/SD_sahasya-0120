"""
Central design system for the AI Resume Analyzer.
Injects the "Aurora" dark glassmorphic theme and provides small HTML
component builders (score rings, chips, cards) used across pages.
Backend/business logic is untouched — this module is purely visual.
"""

import streamlit as st

# ------------------------------------------------------------------ #
#  Palette
# ------------------------------------------------------------------ #
VIOLET = "#8b5cf6"
CYAN = "#22d3ee"
PINK = "#ec4899"
GREEN = "#34d399"
RED = "#f87171"
AMBER = "#fbbf24"


def inject_base_css():
    st.markdown(
        """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');

    :root{
        --violet:#8b5cf6;
        --cyan:#22d3ee;
        --pink:#ec4899;
        --green:#34d399;
        --red:#f87171;
        --amber:#fbbf24;
        --glass: rgba(255,255,255,0.045);
        --glass-border: rgba(255,255,255,0.09);
    }

    html, body, [class*="css"]  { font-family:'Inter', sans-serif; }
    h1,h2,h3,h4, .agrad { font-family:'Space Grotesk', sans-serif !important; }

    /* ---------- animated aurora backdrop ---------- */
    [data-testid="stAppViewContainer"]{
        background: #0a0e1a;
        position: relative;
        overflow-x: hidden;
    }
    [data-testid="stAppViewContainer"]::before{
        content:"";
        position: fixed;
        inset: -20% -20% -20% -20%;
        z-index: 0;
        pointer-events: none;
        background:
            radial-gradient(38% 32% at 15% 20%, rgba(139,92,246,0.32), transparent 70%),
            radial-gradient(35% 30% at 85% 15%, rgba(34,211,238,0.24), transparent 70%),
            radial-gradient(40% 35% at 75% 85%, rgba(236,72,153,0.22), transparent 70%),
            radial-gradient(30% 28% at 10% 85%, rgba(52,211,153,0.14), transparent 70%);
        filter: blur(10px);
        animation: auroraDrift 22s ease-in-out infinite alternate;
    }
    @keyframes auroraDrift{
        0%   { transform: translate3d(0,0,0) scale(1); }
        50%  { transform: translate3d(-2%, 2%, 0) scale(1.06); }
        100% { transform: translate3d(2%, -2%, 0) scale(1.02); }
    }
    [data-testid="stHeader"]{ background: transparent; height: 2.2rem; }
    [data-testid="stAppViewContainer"] > .main{ position: relative; z-index: 1; }
    [data-testid="stToolbar"]{ display:none; }
    #MainMenu{ visibility:hidden; }
    footer{ visibility:hidden; }
    [data-testid="stSidebarNav"]{ display:none; }
    [data-testid="stDecoration"]{ display:none; }

    /* ---------- kill the default oversized top gap so short pages don't scroll ---------- */
    .block-container{
        padding-top: 2.4rem !important;
        padding-bottom: 2.5rem !important;
        max-width: 1180px;
    }
    [data-testid="stMainBlockContainer"]{
        padding-top: 2.4rem !important;
        padding-bottom: 2.5rem !important;
    }

    /* ---------- typography ---------- */
    .agrad{
        background: linear-gradient(90deg, #a78bfa 0%, #67e8f9 45%, #f9a8d4 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        font-weight: 700;
    }
    p, li, span, label, .stMarkdown { color: #cbd2e6; }
    .subtle{ color:#8a91ad; }

    /* ---------- sidebar ---------- */
    section[data-testid="stSidebar"]{
        background: linear-gradient(180deg, #0d1120 0%, #0a0e1a 100%);
        border-right: 1px solid rgba(255,255,255,0.06);
    }
    section[data-testid="stSidebar"] .stPageLink{
        border-radius: 10px;
        margin-bottom: 4px;
        transition: all .2s ease;
    }
    section[data-testid="stSidebar"] .stPageLink:hover{
        background: rgba(139,92,246,0.12);
        transform: translateX(3px);
    }
    section[data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"] p{
        font-weight: 500;
    }

    /* ---------- buttons ---------- */
    .stButton>button, .stFormSubmitButton>button{
        background: linear-gradient(90deg, var(--violet), var(--pink));
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.6rem 1.4rem;
        font-weight: 600;
        letter-spacing: .2px;
        box-shadow: 0 4px 18px rgba(139,92,246,0.35);
        transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
    }
    .stButton>button:hover, .stFormSubmitButton>button:hover{
        transform: translateY(-2px) scale(1.015);
        box-shadow: 0 8px 26px rgba(236,72,153,0.4);
        filter: brightness(1.08);
        color: white;
    }
    .stButton>button:active, .stFormSubmitButton>button:active{
        transform: translateY(0) scale(0.99);
    }
    .stButton>button p, .stFormSubmitButton>button p{ color: white !important; font-weight:600; }

    /* secondary / ghost buttons via key prefix ghost_ */
    [class*="st-key-ghost_"] .stButton>button{
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.16);
        box-shadow: none;
    }
    [class*="st-key-ghost_"] .stButton>button:hover{
        background: rgba(255,255,255,0.1);
        box-shadow: 0 4px 14px rgba(0,0,0,0.25);
    }

    /* ---------- inputs ---------- */
    .stTextInput input, .stTextArea textarea, .stSelectbox [data-baseweb="select"] > div, .stNumberInput input{
        background: rgba(255,255,255,0.04) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 10px !important;
        color: #e9ecf5 !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus{
        border-color: var(--violet) !important;
        box-shadow: 0 0 0 3px rgba(139,92,246,0.22) !important;
    }
    label, .stSelectbox label, .stTextInput label{ color:#aeb4cc !important; font-weight:500; }

    /* ---------- file uploader ---------- */
    [data-testid="stFileUploaderDropzone"]{
        background: rgba(139,92,246,0.06) !important;
        border: 1.5px dashed rgba(139,92,246,0.45) !important;
        border-radius: 16px !important;
        transition: all .2s ease;
    }
    [data-testid="stFileUploaderDropzone"]:hover{
        border-color: var(--cyan) !important;
        background: rgba(34,211,238,0.06) !important;
    }

    /* ---------- generic glass cards (key prefixed with card_) ---------- */
    [class*="st-key-card_"]{
        background: linear-gradient(160deg, rgba(255,255,255,0.055), rgba(255,255,255,0.015));
        border: 1px solid var(--glass-border);
        border-radius: 18px;
        padding: 1.4rem 1.5rem !important;
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.25);
        transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
        animation: fadeUp .5s ease both;
    }
    [class*="st-key-card_"]:hover{
        transform: translateY(-4px);
        border-color: rgba(139,92,246,0.5);
        box-shadow: 0 14px 40px rgba(139,92,246,0.18);
    }
    [class*="st-key-hero_"]{
        background: linear-gradient(160deg, rgba(255,255,255,0.06), rgba(255,255,255,0.015));
        border: 1px solid var(--glass-border);
        border-radius: 22px;
        padding: 2rem 2rem !important;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }
    @keyframes fadeUp{
        from{ opacity:0; transform: translateY(14px); }
        to{ opacity:1; transform: translateY(0); }
    }

    /* ---------- metrics ---------- */
    [data-testid="stMetric"]{
        background: linear-gradient(160deg, rgba(255,255,255,0.06), rgba(255,255,255,0.015));
        border: 1px solid var(--glass-border);
        border-radius: 16px;
        padding: 1rem 1.1rem;
        backdrop-filter: blur(12px);
    }
    [data-testid="stMetricValue"]{
        background: linear-gradient(90deg, #a78bfa, #67e8f9);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }
    [data-testid="stMetricLabel"]{ color:#9aa1bd !important; }

    /* ---------- expander ---------- */
    [data-testid="stExpander"]{
        background: rgba(255,255,255,0.035);
        border: 1px solid var(--glass-border);
        border-radius: 14px !important;
        overflow: hidden;
    }
    [data-testid="stExpander"] summary{ font-weight:600; }

    /* ---------- alerts ---------- */
    [data-testid="stAlert"]{
        border-radius: 12px;
        backdrop-filter: blur(8px);
        border: 1px solid var(--glass-border);
    }

    /* ---------- divider ---------- */
    hr{ border-color: rgba(255,255,255,0.08) !important; }

    /* ---------- scrollbar ---------- */
    ::-webkit-scrollbar{ width:10px; height:10px; }
    ::-webkit-scrollbar-track{ background: transparent; }
    ::-webkit-scrollbar-thumb{
        background: linear-gradient(180deg, var(--violet), var(--pink));
        border-radius: 8px;
    }

    /* ---------- chips ---------- */
    .chip-row{ display:flex; flex-wrap:wrap; gap:8px; margin: 4px 0 2px 0; }
    .chip{
        display:inline-flex; align-items:center; gap:6px;
        padding: 7px 14px; border-radius: 999px;
        font-size: 0.86rem; font-weight: 600;
        border: 1px solid transparent;
        animation: fadeUp .4s ease both;
    }
    .chip-green{ background: rgba(52,211,153,0.12); color:#6ee7b7; border-color: rgba(52,211,153,0.35); }
    .chip-red{ background: rgba(248,113,113,0.12); color:#fca5a5; border-color: rgba(248,113,113,0.35); }
    .chip-amber{ background: rgba(251,191,36,0.12); color:#fcd34d; border-color: rgba(251,191,36,0.35); }
    .chip-violet{ background: rgba(139,92,246,0.14); color:#c4b5fd; border-color: rgba(139,92,246,0.4); }

    /* ---------- score ring ---------- */
    .ring-wrap{ display:flex; flex-direction:column; align-items:center; gap:10px; }
    .ring{
        width:150px; height:150px; border-radius:50%;
        display:flex; align-items:center; justify-content:center;
        background: conic-gradient(var(--ring-color) calc(var(--pct) * 1%), rgba(255,255,255,0.07) 0);
        box-shadow: 0 0 34px -6px var(--ring-glow);
        animation: fadeUp .6s ease both;
    }
    .ring-inner{
        width: 118px; height:118px; border-radius:50%;
        background: #0d1120;
        display:flex; flex-direction:column; align-items:center; justify-content:center;
        border: 1px solid rgba(255,255,255,0.06);
    }
    .ring-value{ font-family:'Space Grotesk',sans-serif; font-size:1.9rem; font-weight:700; color:#f2f3fb; line-height:1; }
    .ring-max{ font-size:0.72rem; color:#7d84a0; margin-top:2px; }
    .ring-label{ font-weight:600; color:#c9cee4; letter-spacing:.2px; }

    /* ---------- badge / pill top tag ---------- */
    .pill{
        display:inline-block; padding:5px 14px; border-radius:999px;
        background: rgba(139,92,246,0.14); border:1px solid rgba(139,92,246,0.4);
        color:#c4b5fd; font-size:0.78rem; font-weight:600; letter-spacing:.4px;
        text-transform: uppercase;
    }

    /* step number bubble */
    .step-num{
        width:38px; height:38px; border-radius:50%;
        background: linear-gradient(135deg, var(--violet), var(--cyan));
        display:flex; align-items:center; justify-content:center;
        font-weight:700; color:white; font-family:'Space Grotesk',sans-serif;
        box-shadow: 0 4px 14px rgba(139,92,246,0.4);
    }
    </style>
        """,
        unsafe_allow_html=True,
    )


def sidebar_nav(active: str = ""):
    """Custom glassy sidebar navigation, replacing default Streamlit page list."""
    with st.sidebar:
        st.markdown(
            """
            <div style="padding: 6px 4px 18px 4px;">
                <div style="font-family:'Space Grotesk',sans-serif; font-size:1.25rem; font-weight:700;">
                    <span class="agrad">📄 ResumeIQ</span>
                </div>
                <div class="subtle" style="font-size:0.78rem;">AI-Powered Resume Analysis</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link("pages/3_Dashboard.py", label="Dashboard", icon="📊")
        st.page_link("pages/4_Upload_Resume.py", label="Analyze Resume", icon="🚀")
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        if st.session_state.get("logged_in"):
            st.markdown(
                f"""<div class="pill" style="margin-left:2px;">Signed in</div>
                <div style="margin-top:6px; color:#dfe2f2; font-weight:600;">👋 {st.session_state.get('user_name','')}</div>""",
                unsafe_allow_html=True,
            )
            if st.button("🚪 Logout", key="ghost_logout", use_container_width=True):
                st.session_state.clear()
                st.rerun()
        else:
            st.page_link("pages/2_Login.py", label="Login", icon="🔐")
            st.page_link("pages/1_Register.py", label="Register", icon="📝")


def require_login(message: str = "You need to be logged in to view this page."):
    """Auth gate: stops the page and shows a friendly login/register prompt
    if the user isn't authenticated. Use at the top of protected pages."""
    if st.session_state.get("logged_in"):
        return
    st.markdown("<div style='height:26px'></div>", unsafe_allow_html=True)
    left, mid, right = st.columns([1, 1.2, 1])
    with mid:
        with st.container(key="card_authgate"):
            st.markdown(
                f"""
                <div style="text-align:center; padding:14px 4px;">
                    <div style="font-size:2.4rem;">🔒</div>
                    <div style="font-weight:700; font-size:1.2rem; margin-top:8px; color:#f1f2fa;">
                        Login required
                    </div>
                    <p class="subtle" style="margin-top:4px;">{message}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            b1, b2 = st.columns(2)
            with b1:
                if st.button("🔐 Login", key="authgate_login", use_container_width=True):
                    st.switch_page("pages/2_Login.py")
            with b2:
                with st.container(key="ghost_authgate_register"):
                    if st.button("📝 Register", key="authgate_register", use_container_width=True):
                        st.switch_page("pages/1_Register.py")
    st.stop()


def is_valid_email(email: str) -> bool:
    import re
    return bool(re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", (email or "").strip()))

def ring_html(value, label, color=VIOLET, glow=None, max_value=100):
    glow = glow or color
    pct = max(0, min(100, (value / max_value) * 100 if max_value else 0))
    return f"""
    <div class="ring-wrap">
        <div class="ring" style="--pct:{pct}; --ring-color:{color}; --ring-glow:{glow};">
            <div class="ring-inner">
                <div class="ring-value">{value}</div>
                <div class="ring-max">/ {max_value}</div>
            </div>
        </div>
        <div class="ring-label">{label}</div>
    </div>
    """


def chips_html(items, kind="violet", icon=""):
    kind_class = f"chip-{kind}"
    if not items:
        return '<div class="subtle" style="padding:4px 0;">None found 🎉</div>'
    spans = "".join(f'<span class="chip {kind_class}">{icon} {i}</span>' for i in items)
    return f'<div class="chip-row">{spans}</div>'
