"""
Professional CSS Styling Module for AI Interview Coach
Provides beautiful, modern, and responsive styling for Streamlit components
"""

def apply_styles():
    """
    Apply professional CSS styling to the entire Streamlit application
    Includes custom colors, typography, spacing, and animations
    """
    
    css = """
    <style>
    /* ==========================================
       ROOT VARIABLES & COLOR PALETTE
       ========================================== */
    
    :root {
        --primary: #1e7e5b;
        --primary-light: #2d5f4a;
        --primary-dark: #155a44;
        --secondary: #0099cc;
        --accent: #00d084;
        --success: #00d084;
        --warning: #ffa500;
        --danger: #ff4757;
        --bg-primary: #0a0e27;
        --bg-secondary: #1a1f3a;
        --bg-tertiary: #242b3a;
        --text-primary: #e0e0e0;
        --text-secondary: #b0b0b0;
        --text-tertiary: #808080;
        --border: #404855;
        --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
        --shadow-md: 0 8px 20px rgba(0, 0, 0, 0.5);
        --shadow-lg: 0 15px 40px rgba(0, 0, 0, 0.7);
    }
    
    /* ==========================================
       GENERAL PAGE STYLING
       ========================================== */
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        background-color: var(--bg-primary) !important;
        color: var(--text-primary) !important;
    }
    
    /* ==========================================
       STREAMLIT SPECIFIC OVERRIDES
       ========================================== */
    
    /* Streamlit Container */
    .stApp {
        background-color: var(--bg-primary) !important;
    }
    
    /* Streamlit Sidebar */
    section[data-testid="stSidebar"] {
        background-color: var(--bg-secondary) !important;
        border-right: 1px solid var(--border) !important;
    }
    
    section[data-testid="stSidebar"] > div {
        padding: 20px !important;
    }
    
    /* Main Content Area */
    [data-testid="stMainBlockContainer"] {
        padding: 30px !important;
        max-width: 1200px !important;
    }
    
    /* ==========================================
       TYPOGRAPHY
       ========================================== */
    
    h1 {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        line-height: 1.2 !important;
        margin-bottom: 1.5rem !important;
        color: var(--primary) !important;
    }
    
    h2 {
        font-size: 2rem !important;
        font-weight: 700 !important;
        line-height: 1.3 !important;
        margin-bottom: 1.2rem !important;
        color: var(--text-primary) !important;
    }
    
    h3 {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        line-height: 1.4 !important;
        margin-bottom: 1rem !important;
        color: var(--text-primary) !important;
    }
    
    h4 {
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        margin-bottom: 0.8rem !important;
        color: var(--text-secondary) !important;
    }
    
    p {
        font-size: 1rem !important;
        line-height: 1.6 !important;
        color: var(--text-secondary) !important;
    }
    
    /* ==========================================
       BUTTONS
       ========================================== */
    
    .stButton > button {
        width: 100%;
        padding: 12px 24px !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        border: none !important;
        background: linear-gradient(135deg, var(--primary), var(--secondary)) !important;
        color: white !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: var(--shadow-sm) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-md) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0) !important;
    }
    
    /* ==========================================
       INPUT FIELDS
       ========================================== */
    
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select,
    .stNumberInput > div > div > input {
        padding: 12px 16px !important;
        border: 2px solid var(--border) !important;
        border-radius: 8px !important;
        font-size: 1rem !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        background-color: var(--bg-tertiary) !important;
        color: var(--text-primary) !important;
        transition: all 0.3s ease !important;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus,
    .stNumberInput > div > div > input:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(30, 126, 91, 0.2) !important;
        background-color: var(--bg-secondary) !important;
        padding: 20px !important;
        box-shadow: var(--shadow-sm) !important;
    }
    
    /* ==========================================
       EXPANDER (COLLAPSIBLE)
       ========================================== */
    
    .streamlit-expanderHeader {
        background-color: var(--primary-light) !important;
        border-radius: 8px !important;
        padding: 12px 16px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: var(--primary) !important;
        color: white !important;
    }
    
    /* ==========================================
       TABS
       ========================================== */
    
    .stTabs > div > div > div {
        background-color: transparent !important;
    }
    
    [data-testid="stTabBar"] button {
        padding: 10px 20px !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        color: var(--text-secondary) !important;
        border: none !important;
        border-bottom: 3px solid transparent !important;
        transition: all 0.3s ease !important;
    }
    
    [data-testid="stTabBar"] button:hover {
        color: var(--primary) !important;
    }
    
    [data-testid="stTabBar"] button[aria-selected="true"] {
        color: var(--primary) !important;
        border-bottom-color: var(--primary) !important;
    }
    
    /* ==========================================
       ALERTS & MESSAGES
       ========================================== */
    
    .stAlert {
        border-radius: 8px !important;
        padding: 15px 20px !important;
        border-left: 4px solid var(--primary) !important;
    }
    
    [data-testid="stSuccess"] {
        background-color: rgba(0, 208, 132, 0.1) !important;
        border-left-color: var(--success) !important;
        color: var(--success) !important;
    }
    
    [data-testid="stError"] {
        background-color: rgba(255, 71, 87, 0.1) !important;
        background-color: rgba(0, 208, 132, 0.15) !important;
        border-left-color: var(--success) !important;
        color: var(--success) !important;
    }

    [data-testid="stError"] {
        background-color: rgba(255, 71, 87, 0.15) !important;
        border-left-color: var(--danger) !important;
        color: var(--danger) !important;
    }

    [data-testid="stWarning"] {
        background-color: rgba(255, 165, 0, 0.15) !important;
        border-left-color: var(--warning) !important;
        color: var(--warning) !important;
    }

    [data-testid="stInfo"] {
        background-color: rgba(30, 126, 91, 0.15) !important;
        border-left-color: var(--primary) !important;
        color: var(--text-primary) !important;   border-top: 2px solid var(--border) !important;
        margin: 20px 0 !important;
    }
    
    /* ==========================================
       PROGRESS BAR
       ========================================== */
    
    .stProgress > div > div {
        background: linear-gradient(90deg, var(--primary), var(--secondary)) !important;
    }
    
    /* ==========================================
       METRICS
       ========================================== */
    
    [data-testid="metric-container"] {
        background-color: var(--primary-light) !important;
        border-radius: 8px !important;
        padding: 20px !important;
        border: 1px solid rgba(0, 102, 255, 0.2) !important;
    }
    
    [data-testid="metric-container"] > div > div > div > div:first-child {
        color: var(--text-secondary) !important;
        background-color: var(--bg-secondary) !important;
        border-radius: 8px !important;
        padding: 20px !important;
        border: 1px solid rgba(30, 126, 91, 0.2) !important;   color: var(--primary) !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }
    
    /* ==========================================
       COLUMNS
       ========================================== */
    
    [data-testid="column"] {
        padding: 10px !important;
    }
    
    /* ==========================================
       DATAFRAME
       ========================================== */
    
    .stDataFrame {
        border-radius: 8px !important;
        overflow: hidden !important;
    }
    
    .dataframe {
        border-collapse: collapse !important;
    }
    
    .dataframe thead {
        background: linear-gradient(135deg, var(--primary-light), var(--primary)) !important;
        color: var(--primary) !important;
        background: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
    }

    .dataframe tbody tr:hover {
        background-color: var(--bg-tertiary) !important;* ==========================================
       CUSTOM CLASSES
       ========================================== */
    
    .card {
        background-color: var(--bg-secondary) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        border: 1px solid var(--border) !important;
        box-shadow: var(--shadow-sm) !important;
        transition: all 0.3s ease !important;
    }
    
    .card:hover {
        box-shadow: var(--shadow-md) !important;
        transform: translateY(-2px) !important;
    }
    
    .badge {
        display: inline-block;
        background-color: var(--primary-light) !important;
        color: var(--primary) !important;
        padding: 6px 12px !important;
        background-color: rgba(30, 126, 91, 0.15) !important;
        color: var(--primary) !important;
        padding: 6px 12px !important;
        border-radius: 20px !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        border: 1px solid rgba(30, 126, 91, 0.3) !important;
    }

    .badge-success {
        background-color: rgba(0, 208, 132, 0.15) !important;
        color: var(--success) !important;
        border-color: var(--success) !important;
    }

    .badge-danger {
        background-color: rgba(255, 71, 87, 0.15) !important;==
       ANIMATIONS
       ========================================== */
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.7;
        }
    }
    
    @keyframes float {
        0%, 100% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
    }
    
    .animate-fadeIn {
        animation: fadeIn 0.6s ease-out !important;
    }
    
    .animate-slideInLeft {
        animation: slideInLeft 0.6s ease-out !important;
    }
    
    .animate-slideInRight {
        animation: slideInRight 0.6s ease-out !important;
    }
    
    .animate-pulse {
        animation: pulse 1.5s ease-in-out infinite !important;
    }
    
    .animate-float {
        animation: float 3s ease-in-out infinite !important;
    }
    
    /* ==========================================
       RESPONSIVE DESIGN
       ========================================== */
    
    @media (max-width: 768px) {
        h1 {
            font-size: 1.8rem !important;
        }
        
        h2 {
            font-size: 1.5rem !important;
        }
        
        h3 {
            font-size: 1.2rem !important;
        }
        
        p {
            font-size: 0.95rem !important;
        }
        
        [data-testid="stMainBlockContainer"] {
            padding: 15px !important;
        }
    }
    
    @media (max-width: 480px) {
        h1 {
            font-size: 1.5rem !important;
        }
        
        h2 {
            font-size: 1.2rem !important;
        }
        
        h3 {
            font-size: 1rem !important;
        }
        
        .stButton > button {
            padding: 10px 16px !important;
            font-size: 0.9rem !important;
        }
        
        [data-testid="stMainBlockContainer"] {
            padding: 10px !important;
        }
    }
    
    /* ==========================================
       SCROLLBAR STYLING
       ========================================== */
    
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-secondary);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--bg-tertiary);
    }

    ::-webkit-scrollbar-thumb {
        background: var(--primary);
        border-radius: 5px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #155a44;
    }
    </style>
    """
    
    import streamlit as st
    st.markdown(css, unsafe_allow_html=True)


def get_global_styles():
    """Returns CSS styling as a string"""
    return '<style>' + \
        ':root{--primary:#0066ff;--primary-light:#1a4d99;--secondary:#00d9ff;' + \
        '--success:#00d084;--warning:#ffa500;--danger:#ff4757;' + \
        '--bg-primary:#0a0e27;--bg-secondary:#1a1f3a;' + \
        '--text-primary:#e0e0e0;--text-secondary:#b0b0b0;}' + \
        '*{margin:0;padding:0;box-sizing:border-box;}' + \
        'body{font-family:"Segoe UI",Tahoma,Geneva,Verdana,sans-serif;' + \
        'background-color:var(--bg-primary);color:var(--text-primary);}' + \
        'h1{font-size:2.5rem;font-weight:700;margin-bottom:1.5rem;color:var(--primary);}' + \
        'h2{font-size:2rem;font-weight:700;margin-bottom:1.2rem;color:var(--text-primary);}' + \
        'h3{font-size:1.5rem;font-weight:600;margin-bottom:1rem;color:var(--text-primary);}' + \
        '.stButton>button{padding:12px 24px!important;font-size:1rem!important;font-weight:600!important;' + \
        'border-radius:8px!important;border:none!important;' + \
        'background:linear-gradient(135deg,var(--primary),var(--secondary))!important;color:white!important;' + \
        'cursor:pointer!important;transition:all 0.3s ease!important;}' + \
        '.stButton>button:hover{transform:translateY(-2px)!important;box-shadow:0 8px 20px rgba(0,102,255,0.3)!important;}' + \
        '.stAlert{border-radius:8px!important;padding:15px 20px!important;}' + \
        '.card{background-color:var(--bg-secondary);border-radius:12px;padding:20px;' + \
        'box-shadow:0 2px 8px rgba(0,0,0,0.3);transition:all 0.3s ease;}' + \
        '.card:hover{box-shadow:0 8px 20px rgba(0,0,0,0.5);transform:translateY(-2px);}' + \
        '</style>'
