import streamlit as st
from auth.auth_utils import register_user, user_exists
from assets.theme import inject_base_css, sidebar_nav, is_valid_email

st.set_page_config(page_title="Register — ResumeIQ", page_icon="📝", layout="wide")
inject_base_css()
sidebar_nav(active="register")

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
    with st.container(key="card_register"):
        st.markdown('<span class="pill">Join ResumeIQ</span>', unsafe_allow_html=True)
        st.markdown(
            '<h2 style="margin:10px 0 2px 0;">Create your <span class="agrad">account</span></h2>',
            unsafe_allow_html=True,
        )
        st.markdown('<p class="subtle">Start getting AI feedback on your resume, free.</p>', unsafe_allow_html=True)

        with st.form("register_form", border=False):
            full_name = st.text_input("Full Name", placeholder="Jane Doe")
            email = st.text_input("Email", placeholder="jane@example.com")
            password = st.text_input("Password", type="password", placeholder="At least 6 characters")
            confirm = st.text_input("Confirm Password", type="password", placeholder="••••••••")

            submit = st.form_submit_button("Create Account →", use_container_width=True)

            if submit:
                full_name = (full_name or "").strip()
                email = (email or "").strip().lower()

                if not full_name or not email or not password:
                    st.error("Fill all fields.")
                elif not is_valid_email(email):
                    st.error("Enter a valid email address.")
                elif len(password) < 6:
                    st.error("Password must be at least 6 characters.")
                elif password != confirm:
                    st.error("Passwords don't match.")
                else:
                    try:
                        if user_exists(email):
                            st.error("Email already registered. Try logging in instead.")
                        else:
                            register_user(full_name, email, password)
                            st.success("Registration successful 🎉 You can log in now.")
                    except Exception:
                        st.error("We couldn't reach the server right now. Please try again in a moment.")

        st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
        st.markdown(
            '<p class="subtle" style="text-align:center;">Already have an account? '
            'Head to the <b>Login</b> page from the sidebar →</p>',
            unsafe_allow_html=True,
        )

