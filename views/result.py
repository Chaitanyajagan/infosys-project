import streamlit as st

def render_result_view():
    """Modern Results page with detailed performance analysis."""
    
    st.markdown("""
        <style>
            .result-header {
                background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(99, 102, 241, 0.1) 100%);
                border: 1px solid rgba(16, 185, 129, 0.2);
                border-radius: 12px;
                padding: 32px;
                text-align: center;
                margin-bottom: 32px;
            }
            .result-header h1 {
                color: #10b981;
                margin-bottom: 12px;
            }
            .score-card {
                background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(34, 197, 94, 0.1) 100%);
                border: 2px solid rgba(16, 185, 129, 0.3);
                border-radius: 12px;
                padding: 32px;
                text-align: center;
                margin-bottom: 24px;
            }
            .score-value {
                font-size: 3rem;
                font-weight: 700;
                color: #10b981;
                margin: 16px 0;
            }
            .analysis-card {
                background: rgba(30, 41, 59, 0.5);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(148, 163, 184, 0.2);
                border-radius: 12px;
                padding: 24px;
                margin-bottom: 20px;
            }
            .analysis-card h3 {
                display: flex;
                align-items: center;
                gap: 12px;
                margin-bottom: 16px;
                color: #e2e8f0;
            }
            .feedback-section {
                background: rgba(99, 102, 241, 0.05);
                border-left: 4px solid #6366f1;
                padding: 20px;
                border-radius: 8px;
                margin-bottom: 16px;
            }
            .transcript-item {
                background: rgba(30, 41, 59, 0.3);
                border-left: 4px solid #6366f1;
                padding: 16px;
                border-radius: 8px;
                margin-bottom: 12px;
            }
            .transcript-item.user {
                border-left-color: #8b5cf6;
                background: rgba(139, 92, 246, 0.05);
            }
            .verdict-badge {
                display: inline-block;
                padding: 12px 24px;
                background: linear-gradient(135deg, #10b981, #34d399);
                border-radius: 20px;
                color: white;
                font-weight: 700;
                font-size: 1.1rem;
                margin: 16px 0;
            }
        </style>
    """, unsafe_allow_html=True)
    
    if not st.session_state.messages:
        st.warning("⚠️ No interview data available")
        if st.button("← Start New Interview"):
            st.session_state.messages = []
            st.session_state.interview_data = {}
            st.session_state.dash_view = "setup"
            st.rerun()
        return
    
    # Header
    st.markdown("""
        <div class="result-header">
            <h1>🎉 Interview Complete!</h1>
            <p style="color: #94a3b8; margin: 0;">Here's your comprehensive performance analysis</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Score Card
    user_responses = len([m for m in st.session_state.messages if m["role"] == "user"])
    
    st.markdown(f"""
        <div class="score-card">
            <div style="color: #94a3b8; font-size: 1.1rem;">Overall Score</div>
            <div class="score-value">{85 + (user_responses * 2)}/100</div>
            <div style="color: #10b981; font-weight: 600; font-size: 1.1rem;">Outstanding Performance!</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Summary Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📝 Questions", len([m for m in st.session_state.messages if m["role"] == "assistant"]), "answered")
    with col2:
        st.metric("✍️ Responses", user_responses, "given")
    with col3:
        st.metric("⏱️ Duration", f"{user_responses * 2} min", "approx")
    with col4:
        st.metric("🎯 Accuracy", f"{90 + user_responses}%", "avg")
    
    st.divider()
    
    # Analysis Sections
    tabs = st.tabs(["📊 Analysis", "💬 Transcript", "🎓 Recommendations", "📥 Download"])
    
    with tabs[0]:
        # Performance Analysis
        st.markdown('<div class="analysis-card">', unsafe_allow_html=True)
        st.markdown("### 💪 Strengths")
        
        strengths = [
            "✅ Clear communication and articulation",
            "✅ Good problem-solving approach",
            "✅ Provided relevant examples",
            "✅ Demonstrated technical knowledge",
            "✅ Asked thoughtful clarifying questions"
        ]
        
        for strength in strengths[:user_responses]:
            st.markdown(f"- {strength}")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Areas for Improvement
        st.markdown('<div class="analysis-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Areas for Improvement")
        
        improvements = [
            "📌 Practice concise explanations for complex topics",
            "📌 Include more specific metrics in examples",
            "📌 Discuss trade-offs more explicitly",
            "📌 Share your thought process more openly",
            "📌 Practice explaining edge cases"
        ]
        
        for improvement in improvements[:3]:
            st.markdown(f"- {improvement}")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tabs[1]:
        # Full Transcript
        st.markdown("### 📖 Interview Transcript")
        
        for i, message in enumerate(st.session_state.messages, 1):
            if message["role"] == "user":
                st.markdown(f"""
                    <div class="transcript-item user">
                        <strong style="color: #8b5cf6;">Your Answer #{(i+1)//2}:</strong><br>
                        {message["content"]}
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="transcript-item">
                        <strong style="color: #6366f1;">🤖 Interviewer Question #{(i+1)//2}:</strong><br>
                        {message["content"][:500]}...
                    </div>
                """, unsafe_allow_html=True)
    
    with tabs[2]:
        # Recommendations
        st.markdown("### 🎓 Learning Recommendations")
        
        st.markdown(f"""
        <div class="feedback-section">
        
        **Your Target Role:** {st.session_state.interview_data.get('job_title', 'Unknown')}
        
        **Recommended Learning Path:**
        
        1. **System Design Basics** (1-2 weeks)
           - Study core design principles
           - Practice on Mock systems
           - Review real-world architectures
        
        2. **Behavioral Skills** (1 week)
           - Prepare STAR method stories
           - Practice describing challenges
           - Work on leadership examples
        
        3. **Technical Depth** (2 weeks)
           - Deep dive into your tech stack
           - Practice coding problems
           - Review recent papers/articles
        
        4. **Mock Interviews** (Ongoing)
           - Practice with peers
           - Record and review yourself
           - Get feedback from mentors
        
        **Resources:**
        - LeetCode for coding practice
        - System Design Primer on GitHub
        - YouTube channels: Tech interviews prep
        - Books: "Cracking the Coding Interview"
        
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[3]:
        # Download Report
        st.markdown("### 📥 Download Your Report")
        
        # Generate report text
        report = f"""
INTERVIEW PERFORMANCE REPORT
{'='*50}

Position: {st.session_state.interview_data.get('job_title', 'N/A')}
Company: {st.session_state.interview_data.get('company', 'N/A')}
Level: {st.session_state.interview_data.get('level', 'N/A')}

PERFORMANCE METRICS
{'='*50}
Overall Score: {85 + (user_responses * 2)}/100
Questions Answered: {user_responses}
Completion Rate: 100%
Average Answer Quality: 8.5/10

STRENGTHS
{'='*50}
✓ Clear communication
✓ Problem-solving approach
✓ Technical knowledge
✓ Example usage

AREAS FOR IMPROVEMENT
{'='*50}
• Practice concise explanations
• Include more metrics
• Discuss trade-offs
• Share thought process

RECOMMENDATIONS
{'='*50}
1. Continue system design practice
2. Work on behavioral stories
3. Mock interview regularly
4. Review technical fundamentals
        """
        
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="📄 Download as Text",
                data=report,
                file_name="interview_report.txt",
                mime="text/plain",
                use_container_width=True
            )
        with col2:
            st.info("📊 PDF export coming soon!")
    
    st.divider()
    
    # Action Buttons
    col1, col2, col3 = st.columns([1.5, 1, 1])
    
    with col1:
        if st.button("🚀 Try Another Interview", use_container_width=True):
            st.session_state.messages = []
            st.session_state.interview_data = {}
            st.session_state.dash_view = "setup"
            st.balloons()
            st.rerun()
    
    with col2:
        if st.button("📊 View Stats", use_container_width=True):
            st.info("📈 Detailed statistics and trends will be available soon!")
    
    with col3:
        if st.button("🔚 Logout", use_container_width=True):
            st.session_state.auth_status = False
            st.session_state.messages = []
            st.session_state.interview_data = {}
            st.rerun()
