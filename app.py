"""
AI Interview Coach - Professional Streamlit Application
A comprehensive interview preparation platform powered by AI
Author: Interview Coach Team
Version: 2.0
"""

import streamlit as st
from views.auth import page_login_signup
from views.setup import render_home_view
from views.interview import render_interview_view
from views.result import render_result_view
from styles import apply_styles, get_global_styles
import database as db
import os
from dotenv import load_dotenv
from datetime import datetime
from langchain_utils import InterviewCoach

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load environment variables
load_dotenv()

# Initialize database
db.init_db()

# Apply custom CSS styling - both methods for compatibility
apply_styles()
st.markdown(get_global_styles(), unsafe_allow_html=True)

# ==========================================
# SESSION STATE INITIALIZATION
# ==========================================

def initialize_session_state():
    """Initialize all required session state variables"""
    
    session_defaults = {
        'authenticated': False,
        'current_view': 'landing',  # landing, auth, setup, interview, result
        'user_data': {},
        'interview_data': {},
        'messages': [],
        'show_landing': True,
        'interview_started': False,
        'current_question': 0,
        'feedback_received': False,
        'interview_complete': False,
        'user_answers': [],
        'interview_scores': {},
    }
    
    for key, value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
    
    # Initialize AI Coach
    if 'coach' not in st.session_state:
        st.session_state.coach = InterviewCoach()
        api_key = os.getenv('GOOGLE_API_KEY') or os.getenv('GEMINI_API_KEY')
        if api_key:
            st.session_state.coach.configure(api_key)

# Initialize session
initialize_session_state()

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

def render_sidebar():
    """Render professional sidebar with navigation and progress"""
    
    with st.sidebar:
        # Logo and branding
        st.markdown("""
            <div style='text-align: center; padding: 20px 0;'>
                <h2 style='color: #0066ff; margin: 0; font-size: 28px;'>🎯 Interview Coach</h2>
                <p style='color: #666; font-size: 0.85rem; margin: 5px 0 0 0;'>
                    Master Your Interview Skills with AI
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # User Profile Section (if authenticated)
        if st.session_state.authenticated:
            user_name = st.session_state.user_data.get('name', 'User')
            user_role = st.session_state.user_data.get('job_role', 'Position')
            experience = st.session_state.user_data.get('experience_level', 'N/A')
            
            st.markdown(f"""
                <div style='background: linear-gradient(135deg, #f0f4ff 0%, #e6f0ff 100%); 
                            padding: 15px; border-radius: 10px; margin-bottom: 15px;
                            border-left: 4px solid #0066ff;'>
                    <p style='margin: 0; font-weight: 600; color: #0066ff;'>👤 {user_name}</p>
                    <p style='margin: 5px 0 0 0; color: #666; font-size: 0.85rem;'>
                        {user_role} • {experience}
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Progress Indicator
            if st.session_state.interview_data:
                progress = st.session_state.interview_data.get('current_question', 0)
                total = st.session_state.interview_data.get('total_questions', 5)
                
                if total > 0:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.progress(progress / total, text=f"Progress: {progress}/{total}")
            
            st.divider()
            
            # Navigation Buttons
            st.subheader("🗂️ Navigation", anchor=False)
            
            nav_items = [
                ("⚙️ Job Setup", "setup"),
                ("🎤 Start Interview", "interview"),
                ("📊 View Results", "result"),
            ]
            
            for label, view in nav_items:
                if st.button(label, use_container_width=True, key=f"nav_{view}"):
                    st.session_state.current_view = view
                    st.rerun()
            
            st.divider()
            
            # Interview Stats (if any)
            if st.session_state.interview_complete and st.session_state.interview_scores:
                st.subheader("📈 Performance", anchor=False)
                
                avg_score = sum(st.session_state.interview_scores.values()) / len(st.session_state.interview_scores)
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Overall", f"{avg_score:.1f}/10")
                col2.metric("Q's", len(st.session_state.interview_scores))
                col3.metric("Accuracy", f"{(avg_score/10)*100:.0f}%")
            
            st.divider()
            
            # API Configuration
            st.subheader("🔑 API Configuration", anchor=False)
            api_key = os.getenv('GOOGLE_API_KEY')
            
            if not api_key:
                api_key = st.text_input(
                    "Enter Google API Key",
                    type="password",
                    placeholder="sk-...",
                    key="api_key_input"
                )
                if api_key:
                    st.session_state.coach.configure(api_key)
                    st.success("✅ API Configured")
            else:
                st.success("✅ API Key Loaded")
            
            st.divider()
            
            # Logout button
            if st.button("🚪 Logout", use_container_width=True, key="btn_logout"):
                st.session_state.authenticated = False
                st.session_state.current_view = 'landing'
                st.session_state.user_data = {}
                st.session_state.interview_data = {}
                st.rerun()
        
        else:
            # Non-authenticated sidebar
            st.markdown("""
                <div style='padding: 20px 0;'>
                    <p style='color: #666; text-align: center; font-size: 0.95rem;'>
                        👋 Sign in to start practicing interviews with our AI coach.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            st.divider()
            
            st.subheader("✨ Key Features", anchor=False)
            st.markdown("""
                - 🤖 AI-powered realistic questions
                - 📝 Instant feedback on answers
                - 📊 Performance analytics
                - 🎯 Role-specific preparation
                - 💾 Interview history tracking
                - 🏆 Performance metrics
            """)
            
            st.divider()
            
            st.subheader("🎯 How It Works", anchor=False)
            st.markdown("""
                **1. Create Account** → Set up your profile
                
                **2. Choose Role** → Select target position
                
                **3. Practice** → Complete mock interviews
                
                **4. Get Feedback** → Improve with AI insights
            """)

# ==========================================
# LANDING PAGE
# ==========================================

def show_landing_page():
    """Display professional landing page"""
    
    # Hero Section
    col1, col2 = st.columns([1.2, 0.8], gap="large")
    
    with col1:
        st.markdown("""
            <h1 style='color: #0066ff; font-size: 2.8em; margin: 0; line-height: 1.1;'>
                Master Your Interviews with AI
            </h1>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <p style='font-size: 1.1em; color: #555; line-height: 1.6; margin: 20px 0;'>
                Practice real interview questions with an <strong>AI interviewer</strong> that provides 
                <strong>instant feedback</strong> on your responses. Get better prepared for your dream job.
            </p>
        """, unsafe_allow_html=True)
        
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        with col_btn1:
            if st.button("🚀 Get Started", use_container_width=True, key="btn_start"):
                st.session_state.current_view = 'auth'
                st.session_state.show_landing = False
                st.rerun()
        with col_btn2:
            if st.button("📖 Learn More", use_container_width=True, key="btn_learn"):
                st.session_state.show_features = True
        with col_btn3:
            if st.button("👥 Sign In", use_container_width=True, key="btn_signin"):
                st.session_state.current_view = 'auth'
                st.rerun()
    
    with col2:
        st.markdown("""
            <div style='text-align: center; padding: 40px 20px;'>
                <div style='font-size: 120px; margin-bottom: 20px;'>🎯</div>
                <div style='font-size: 1.2em; color: #0066ff; font-weight: 600;'>
                    AI-Powered Interview Coach
                </div>
                <div style='font-size: 0.9em; color: #666; margin-top: 10px;'>
                    100% Free. Unlimited Practice.
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Features Section
    st.markdown("""
        <h2 style='text-align: center; color: #0066ff; margin-bottom: 40px;'>
            ✨ Why Choose AI Interview Coach?
        </h2>
    """, unsafe_allow_html=True)
    
    features = [
        {
            "icon": "🤖",
            "title": "AI Interviewer",
            "description": "Realistic AI that adapts to your experience level with intelligent follow-ups."
        },
        {
            "icon": "📊",
            "title": "Real-Time Feedback",
            "description": "Get instant feedback on communication, technical accuracy, and overall performance."
        },
        {
            "icon": "🎯",
            "title": "Personalized Questions",
            "description": "Questions tailored to your role, company, and experience level."
        },
        {
            "icon": "📈",
            "title": "Progress Tracking",
            "description": "Track your improvement over time with detailed analytics and insights."
        },
        {
            "icon": "💼",
            "title": "Role-Specific Prep",
            "description": "Prepare for different positions with role-specific interview questions."
        },
        {
            "icon": "🏆",
            "title": "Success Proven",
            "description": "Thousands of users successfully prepared for interviews at top companies."
        }
    ]
    
    cols = st.columns(3)
    for idx, feature in enumerate(features):
        with cols[idx % 3]:
            st.markdown(f"""
                <div style='background: #f8f9ff; padding: 25px; border-radius: 12px; 
                            border-left: 4px solid #0066ff; margin-bottom: 20px;
                            transition: transform 0.3s ease;'>
                    <p style='font-size: 2.2em; margin: 0; text-align: center;'>{feature['icon']}</p>
                    <p style='font-weight: 600; margin: 12px 0 8px 0; text-align: center;'>{feature['title']}</p>
                    <p style='color: #666; margin: 0; font-size: 0.95em; line-height: 1.5;'>{feature['description']}</p>
                </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # How It Works
    st.markdown("""
        <h2 style='text-align: center; color: #0066ff; margin-bottom: 40px;'>
            📋 How It Works in 4 Simple Steps
        </h2>
    """, unsafe_allow_html=True)
    
    steps = [
        {
            "num": "1️⃣",
            "title": "Create Account",
            "desc": "Sign up and set up your profile with your target role and experience level."
        },
        {
            "num": "2️⃣",
            "title": "Start Interview",
            "desc": "Begin an AI-powered mock interview tailored to your background."
        },
        {
            "num": "3️⃣",
            "title": "Get Feedback",
            "desc": "Receive detailed analysis and tips on how to improve your answers."
        },
        {
            "num": "4️⃣",
            "title": "Track Progress",
            "desc": "Review your performance and track improvement over time."
        },
    ]
    
    for step in steps:
        col1, col2 = st.columns([0.15, 0.85])
        with col1:
            st.markdown(f"<p style='font-size: 2em; margin: 10px 0;'>{step['num']}</p>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div style='padding: 15px 0;'>
                    <p style='font-weight: 600; margin: 0; color: #0066ff; font-size: 1.1em;'>{step['title']}</p>
                    <p style='color: #666; margin: 8px 0 0 0; font-size: 0.95em; line-height: 1.5;'>{step['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # Statistics
    st.markdown("""
        <h2 style='text-align: center; color: #0066ff; margin-bottom: 40px;'>
            🎓 Join Thousands of Successful Interview Candidates
        </h2>
    """, unsafe_allow_html=True)
    
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    
    stats = [
        ("50K+", "Active Users"),
        ("1M+", "Interviews Completed"),
        ("4.9★", "Average Rating"),
        ("95%", "Success Rate"),
    ]
    
    for col, (num, label) in zip([stat_col1, stat_col2, stat_col3, stat_col4], stats):
        with col:
            st.markdown(f"""
                <div style='text-align: center; padding: 20px;'>
                    <p style='font-size: 2em; font-weight: 700; color: #0066ff; margin: 0;'>{num}</p>
                    <p style='color: #666; margin: 10px 0 0 0; font-size: 0.95em;'>{label}</p>
                </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # CTA
    st.markdown("""
        <div style='text-align: center; padding: 50px 30px; 
                    background: linear-gradient(135deg, #0066ff 0%, #00a8ff 100%); 
                    border-radius: 15px; color: white;'>
            <h3 style='margin: 0 0 10px 0; color: white; font-size: 1.8em;'>Ready to ace your interviews?</h3>
            <p style='margin: 10px 0 25px 0; opacity: 0.95; font-size: 1.05em;'>
                Start practicing with AI today - completely free! No credit card required.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Start Your Free Interview Practice Now", use_container_width=True, key="btn_cta"):
        st.session_state.current_view = 'auth'
        st.rerun()

# ==========================================
# MAIN APPLICATION FLOW
# ==========================================

def main():
    """Main application router"""
    
    # Render sidebar
    render_sidebar()
    
    # Route to appropriate page
    if not st.session_state.authenticated and st.session_state.current_view == 'landing':
        show_landing_page()
    elif not st.session_state.authenticated:
        page_login_signup()
    elif st.session_state.current_view == 'setup':
        render_home_view()
    elif st.session_state.current_view == 'interview':
        render_interview_view()
    elif st.session_state.current_view == 'result':
        render_result_view()
    else:
        # Default to setup if no view specified
        render_home_view()

# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    main()
