import streamlit as st

def configurar_estilos():
    st.markdown("""
    <style>
        .main-header {
            font-size: 3rem;
            font-weight: bold;
            background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            padding: 1rem 0;
        }
        .sub-header {
            text-align: center;
            color: #666;
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }
        .meal-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 15px;
            color: white;
            margin: 1rem 0;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        }
        .day-card {
            background: white;
            padding: 1.5rem;
            border-radius: 15px;
            border-left: 5px solid #667eea;
            margin: 1rem 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.07);
            color: black;
        }
        .nutrient-badge {
            display: inline-block;
            padding: 0.3rem 0.8rem;
            margin: 0.2rem;
            border-radius: 20px;
            background: #f0f0f0;
            font-size: 0.9rem;
            font-weight: 500;
        }
        .info-box {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 1.5rem;
            border-radius: 15px;
            color: white;
            margin: 1rem 0;
        }
    </style>
    """, unsafe_allow_html=True)
