import streamlit as st
from auth.auth_utils import login_user
from assets.theme import inject_base_css, sidebar_nav

st.set_page_config(page_title="Login — ResumeIQ", page_icon="🔐", layout="wide")
inject_base_css()
sidebar_nav(active="login")

if st.session_state.get("logged_in"):
    st.markdown("<div style='height:26px'></div>", unsafe_allow_html=True)
    left, mid, right = st.columns([1, 1.2, 1])
    with mid:
        with st.container(key="card_already_in"):
            st.markdown(
                f"""<div style="text-align:center; padding:10px 0;">
                    <div style="font-size:2.2rem;">✅</div>
                    <div style="font-weight:700; font-size:1.1rem; margin-top:6px; color:#f1f2fa;">
                        You're already signed in as {st.session_state.get('user_name','')}
                    </div>
                </div>""",
                unsafe_allow_html=True,
            )
            if st.button("Go to Dashboard →", key="already_dash", use_container_width=True):
                st.switch_page("pages/3_Dashboard.py")
    st.stop()

left, mid, right = st.columns([1, 1.2, 1])
with mid:
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    with st.container(key="card_login"):
        st.markdown('<span class="pill">Welcome back</span>', unsafe_allow_html=True)
        st.markdown(
            '<h2 style="margin:10px 0 2px 0;">Log in to <span class="agrad">ResumeIQ</span></h2>',
            unsafe_allow_html=True,
        )
        st.markdown('<p class="subtle">Pick up right where you left off.</p>', unsafe_allow_html=True)

        with st.form("login_form", border=False):
            email = st.text_input("Email", placeholder="jane@example.com")
            password = st.text_input("Password", type="password", placeholder="••••••••")

            login = st.form_submit_button("Login →", use_container_width=True)

            if login:
                email_clean = (email or "").strip().lower()
                if not email_clean or not password:
                    st.error("Enter both email and password.")
                else:
                    try:
                        user = login_user(email_clean, password)
                    except Exception:
                        user = None
                        st.error("We couldn't reach the server right now. Please try again in a moment.")
                    else:
                        if user:
                            st.session_state["logged_in"] = True
                            st.session_state["user_id"] = user["id"]
                            st.session_state["user_name"] = user["name"]
                            st.success(f"Welcome {user['name']} 🎉")
                            st.rerun()
                        else:
                            st.error("Invalid email or password.")

        st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
        st.markdown(
            '<p class="subtle" style="text-align:center;">New here? '
            'Head to the <b>Register</b> page from the sidebar →</p>',
            unsafe_allow_html=True,
        )

