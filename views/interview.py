import streamlit as st
import time

def render_interview_view():
    """Modern Interview page with enhanced UI and real-time feedback."""
    
    st.markdown("""
        <style>
            .interview-container {
                max-width: 1000px;
                margin: 0 auto;
            }
            .interview-header {
                background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
                border: 1px solid rgba(99, 102, 241, 0.2);
                border-radius: 12px;
                padding: 24px;
                margin-bottom: 24px;
            }
            .interview-timer {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 16px;
                background: rgba(30, 41, 59, 0.5);
                border-radius: 8px;
                margin-bottom: 24px;
                border-left: 4px solid #6366f1;
            }
            .chat-container {
                background: rgba(30, 41, 59, 0.3);
                border: 1px solid rgba(148, 163, 184, 0.2);
                border-radius: 12px;
                padding: 20px;
                height: 450px;
                overflow-y: auto;
                margin-bottom: 20px;
            }
            .message-user {
                background: rgba(139, 92, 246, 0.1);
                border-left: 4px solid #8b5cf6;
                padding: 16px;
                border-radius: 8px;
                margin-bottom: 12px;
                animation: slideIn 0.3s ease-out;
            }
            .message-ai {
                background: rgba(99, 102, 241, 0.1);
                border-left: 4px solid #6366f1;
                padding: 16px;
                border-radius: 8px;
                margin-bottom: 12px;
                animation: slideIn 0.3s ease-out;
            }
            .question-counter {
                text-align: center;
                padding: 12px;
                background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1));
                border-radius: 8px;
                margin-bottom: 16px;
                font-weight: 600;
            }
        </style>
    """, unsafe_allow_html=True)
    
    if not st.session_state.interview_data:
        st.warning("⚠️ Please complete job setup first")
        if st.button("← Go to Setup"):
            st.session_state.dash_view = "setup"
            st.rerun()
        return
    
    # Interview Header
    st.markdown("""
        <div class="interview-header">
            <h1>🎤 Interview in Progress</h1>
            <p style="color: #94a3b8; margin: 0;">Performing well? Answer thoughtfully and share your reasoning.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Job Details
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("💼 Position", st.session_state.interview_data.get("job_title", "N/A")[:15])
    with col2:
        st.metric("🏢 Company", st.session_state.interview_data.get("company", "N/A")[:15])
    with col3:
        st.metric("📊 Level", st.session_state.interview_data.get("level", "N/A"))
    with col4:
        st.metric("📝 Questions", f"{len([m for m in st.session_state.messages if m['role'] == 'assistant'])}/5")
    
    st.divider()
    
    # Question Counter
    q_count = len([m for m in st.session_state.messages if m['role'] == 'assistant'])
    st.markdown(f"""
        <div class="question-counter">
            Question {min(q_count + 1, 5)} of 5 ⏱️
        </div>
    """, unsafe_allow_html=True)
    
    # Chat Display
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    if not st.session_state.messages:
        st.markdown("""
            <div style="text-align: center; padding: 40px 20px; color: #94a3b8;">
                <h3>👋 Welcome to your interview!</h3>
                <p>The interviewer will appear here shortly. Ready to begin?</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"""
                    <div class="message-user">
                        <strong>You:</strong><br>{message["content"]}
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="message-ai">
                        <strong>🤖 Interviewer:</strong><br>{message["content"]}
                    </div>
                """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.divider()
    
    # Input Area
    st.markdown("### Your Response")
    user_input = st.text_area(
        "Type your answer here...",
        placeholder="Share your thoughts and be specific with examples...",
        height=100,
        label_visibility="collapsed"
    )
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        if st.button("✅ Submit Answer", use_container_width=True):
            if user_input.strip():
                st.session_state.messages.append({"role": "user", "content": user_input})
                
                with st.spinner("🤔 Interviewer is thinking..."):
                    time.sleep(1)  # Simulate processing
                    coach = st.session_state.coach
                    response = coach.ask_question(
                        user_input,
                        st.session_state.interview_data
                    )
                    st.session_state.messages.append({"role": "assistant", "content": response})
                
                st.success("✅ Response recorded!")
                st.rerun()
            else:
                st.warning("⚠️ Please enter a response")
    
    with col2:
        if st.button("⏸ Pause", use_container_width=True):
            st.info("💾 Your progress has been saved. You can continue later.")
    
    with col3:
        if st.button("⏹ End", use_container_width=True):
            if len(st.session_state.messages) > 0:
                st.session_state.dash_view = "result"
                st.rerun()
            else:
                st.warning("⚠️ Please answer at least one question before finishing")
    
    # Tips Section
    with st.expander("💡 Interview Tips"):
        st.markdown("""
        ✅ **Best Practices:**
        - Take a moment to understand the question
        - Provide specific examples from your experience
        - Explain your problem-solving approach
        - Ask clarifying questions if needed
        - Be authentic and genuine
        
        ⏱️ **Timing:** Answer concisely but thoroughly (1-2 minutes per answer)
        """)
