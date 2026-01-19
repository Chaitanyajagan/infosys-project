import streamlit as st
import database as db

def page_login_signup():
    """Modern Login/Signup page with better UI."""
    
    # Custom CSS for auth page
    st.markdown("""
        <style>
            .auth-container {
                max-width: 900px;
                margin: 0 auto;
                padding: 40px 20px;
            }
            .auth-header {
                text-align: center;
                margin-bottom: 50px;
            }
            .auth-header h1 {
                font-size: 3rem;
                margin-bottom: 10px;
                background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            .auth-header p {
                color: #94a3b8;
                font-size: 1.1rem;
            }
            .auth-card {
                background: rgba(30, 41, 59, 0.5);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(148, 163, 184, 0.2);
                border-radius: 12px;
                padding: 32px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            }
            .tab-item {
                padding: 32px 0;
            }
            .divider-text {
                text-align: center;
                color: #64748b;
                margin: 24px 0;
                position: relative;
            }
            .divider-text::before {
                content: '';
                position: absolute;
                top: 50%;
                left: 0;
                width: 100%;
                height: 1px;
                background: linear-gradient(90deg, transparent, #475569, transparent);
                transform: translateY(-50%);
            }
            .divider-text span {
                background: rgba(30, 41, 59, 0.5);
                padding: 0 12px;
                position: relative;
                z-index: 1;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div class="auth-header">
                <h1>⚡ Coach.AI</h1>
                <p>Master Your Interview Skills</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Auth Container
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    
    # Tabs
    tab1, tab2 = st.tabs(["🔑 Login", "📝 Sign Up"])
    
    with tab1:
        st.markdown('<div class="tab-item">', unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="auth-card">', unsafe_allow_html=True)
            
            st.markdown("### Welcome Back")
            st.markdown("Sign in to continue your interview preparation")
            
            email = st.text_input(
                "📧 Email Address",
                placeholder="your@email.com",
                key="login_email"
            )
            
            password = st.text_input(
                "🔐 Password",
                type="password",
                placeholder="Enter your password",
                key="login_password"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🚀 Login", key="btn_login"):
                    if email and password:
                        if db.verify_user(email, password):
                            st.session_state.authenticated = True
                            st.session_state.user_data = {'name': email.split('@')[0], 'email': email}
                            st.session_state.current_view = 'setup'
                            st.success("✅ Login successful! Redirecting...")
                            st.balloons()
                            st.rerun()
                        else:
                            st.error("❌ Invalid email or password")
                    else:
                        st.warning("⚠️ Please enter email and password")
            
            with col2:
                if st.button("← Back", key="btn_back_login"):
                    pass
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="tab-item">', unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="auth-card">', unsafe_allow_html=True)
            
            st.markdown("### Create Your Account")
            st.markdown("Join thousands preparing for success")
            
            new_email = st.text_input(
                "📧 Email Address",
                placeholder="your@email.com",
                key="signup_email"
            )
            
            new_password = st.text_input(
                "🔐 Password",
                type="password",
                placeholder="Create a strong password",
                key="signup_password"
            )
            
            confirm_password = st.text_input(
                "✔️ Confirm Password",
                type="password",
                placeholder="Confirm your password",
                key="signup_confirm"
            )
            
            # Password strength indicator
            if new_password:
                strength = len(new_password)
                if strength < 6:
                    st.warning("🔓 Password is weak")
                elif strength < 10:
                    st.info("🔓 Password is medium")
                else:
                    st.success("🔐 Password is strong")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✨ Create Account", key="btn_signup"):
                    if new_email and new_password and confirm_password:
                        if new_password == confirm_password:
                            if db.create_user(new_email, new_password):
                                st.success("✅ Account created successfully!")
                                st.balloons()
                                st.markdown("**Ready to login?** Switch to the Login tab.")
                            else:
                                st.error("❌ Email already exists")
                        else:
                            st.error("❌ Passwords do not match")
                    else:
                        st.warning("⚠️ Please fill in all fields")
            
            with col2:
                if st.button("← Back", key="btn_back_signup"):
                    pass
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("""
            <div style="text-align: center; color: #64748b; font-size: 0.9rem;">
                <p>🔒 Your data is secure and encrypted</p>
            </div>
        """, unsafe_allow_html=True)
