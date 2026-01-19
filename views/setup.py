import streamlit as st

def render_home_view():
    """Modern Job Setup page with improved UI and animations."""
    
    st.markdown("""
        <style>
            .setup-header {
                background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
                border: 1px solid rgba(99, 102, 241, 0.2);
                border-radius: 12px;
                padding: 32px;
                margin-bottom: 32px;
                text-align: center;
            }
            .setup-header h1 {
                margin-bottom: 12px;
            }
            .form-section {
                background: rgba(30, 41, 59, 0.5);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(148, 163, 184, 0.2);
                border-radius: 12px;
                padding: 24px;
                margin-bottom: 20px;
                transition: all 0.3s ease;
            }
            .form-section:hover {
                border-color: rgba(99, 102, 241, 0.3);
            }
            .section-title {
                display: flex;
                align-items: center;
                gap: 12px;
                margin-bottom: 20px;
                color: #e2e8f0;
                font-weight: 600;
            }
            .progress-steps {
                display: flex;
                justify-content: space-between;
                gap: 12px;
                margin-bottom: 32px;
            }
            .step {
                flex: 1;
                text-align: center;
                padding: 12px;
                background: rgba(30, 41, 59, 0.5);
                border-radius: 8px;
                border: 2px solid rgba(148, 163, 184, 0.1);
                transition: all 0.3s ease;
            }
            .step.active {
                background: rgba(99, 102, 241, 0.2);
                border-color: #6366f1;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
        <div class="setup-header">
            <h1>⚙️ Configure Your Interview</h1>
            <p style="color: #94a3b8; margin: 0;">Set up your profile for a personalized interview experience</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Progress Indicator
    st.markdown("""
        <div class="progress-steps">
            <div class="step active">
                <span style="font-weight: 600;">📋 Job Info</span>
            </div>
            <div class="step">
                <span style="font-weight: 600;">🎯 Experience</span>
            </div>
            <div class="step">
                <span style="font-weight: 600;">🚀 Skills</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Job Information Section
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📋 Job Information</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        job_title = st.text_input(
            "Job Title",
            placeholder="e.g., Senior Software Engineer",
            help="The position you're interviewing for"
        )
    with col2:
        company = st.text_input(
            "Company Name",
            placeholder="e.g., Google, Amazon",
            help="Company or organization"
        )
    
    col1, col2 = st.columns(2)
    with col1:
        job_type = st.selectbox(
            "Job Type",
            ["Full-time", "Part-time", "Contract", "Internship"],
            help="Select the employment type"
        )
    with col2:
        level = st.selectbox(
            "Seniority Level",
            ["Junior", "Mid-Level", "Senior", "Lead/Principal"],
            help="Your target career level"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Experience Section
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Your Experience</div>', unsafe_allow_html=True)
    
    experience = st.slider(
        "Years of Experience",
        min_value=0,
        max_value=50,
        value=5,
        step=1,
        help="Your total years of professional experience"
    )
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Experience", f"{experience} years", "🔧")
    with col2:
        st.metric("Profile Level", level, "📊")
    with col3:
        st.metric("Job Type", job_type, "💼")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Skills Section
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Key Skills</div>', unsafe_allow_html=True)
    
    all_skills = [
        "Python", "JavaScript", "TypeScript", "Java", "C++", "Go", "Rust",
        "React", "Vue", "Angular", "Node.js", "Django", "FastAPI",
        "AWS", "GCP", "Azure", "Docker", "Kubernetes", "Terraform",
        "SQL", "MongoDB", "Redis", "PostgreSQL",
        "System Design", "Microservices", "REST API", "GraphQL"
    ]
    
    skills = st.multiselect(
        "Select your core skills",
        all_skills,
        help="Choose skills relevant to the position",
        max_selections=10
    )
    
    # Display selected skills as badges
    if skills:
        badge_html = '<div style="display: flex; gap: 8px; flex-wrap: wrap; margin: 16px 0;">'
        for skill in skills:
            badge_html += f'<span class="badge">{skill}</span>'
        badge_html += '</div>'
        st.markdown(badge_html, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Resume Section
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📄 Background</div>', unsafe_allow_html=True)
    
    resume_text = st.text_area(
        "Tell us about your background",
        placeholder="Share your work experience, notable projects, or achievements...",
        height=120,
        help="This helps personalize your interview",
        label_visibility="collapsed"
    )
    
    # Character count
    if resume_text:
        st.caption(f"📝 {len(resume_text)} characters")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Action Buttons
    st.markdown("---")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        if st.button("🚀 Start Interview", use_container_width=True):
            if job_title and company:
                st.session_state.interview_data = {
                    "job_title": job_title,
                    "company": company,
                    "experience": experience,
                    "job_type": job_type,
                    "level": level,
                    "skills": skills,
                    "resume": resume_text
                }
                st.session_state.dash_view = "interview"
                st.success("✅ Configuration saved! Starting interview...")
                st.rerun()
            else:
                st.error("❌ Please enter job title and company name")
    
    with col2:
        if st.button("↻ Reset", use_container_width=True):
            st.session_state.interview_data = {}
            st.rerun()
    
    with col3:
        if st.button("ⓘ Help", use_container_width=True):
            st.info("💡 Complete all sections to get the best interview experience tailored to your target role!")
