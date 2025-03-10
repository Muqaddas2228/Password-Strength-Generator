import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔹 Password should be at least 8 characters long. ❗")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("🔹 Password should contain at least one uppercase letter. 🔠")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔹 Password should contain at least one lowercase letter. 🔡")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔹 Password should contain at least one digit (0-9). 🔢")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔹 Password should contain at least one special character (!@#$%^&*). ✨")
    
    return score, feedback

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")

# Add background image and animations
st.markdown(
    """
    <style>
        .stApp {
            background-image: url('https://media.istockphoto.com/id/1425479353/photo/pin-code-entry-and-padlock-locked-password-field-fraud-protection-cybersecurity-of-data.jpg?s=612x612&w=0&k=20&c=kTMn-l412wwi1bs5gAxHCxGU2UN9L99FgmbtsPqxPDo=');
            background-size: cover;
            background-position: center;
            animation: fadeIn 2s ease-in-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        .password-box {
            animation: bounceIn 1s ease;
        }
        
        @keyframes bounceIn {
            0% { transform: scale(0.9); opacity: 0; }
            50% { transform: scale(1.1); opacity: 1; }
            100% { transform: scale(1); }
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔒 Password Strength Meter 🔥")

username = st.text_input("👤 Enter your username:")
password = st.text_input("🔑 Enter your password:", type="password", key="password_input")

if st.button("🔍 Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)
        
        if score == 5:
            st.success("✅ Strong Password! Your password is secure. 🔥")
            st.balloons()
        elif score >= 3:
            st.warning("⚠️ Moderate Password. Consider improving it. ⚡")
        else:
            st.error("❌ Weak Password! Please follow the suggestions below. 🚨")
        
        if feedback:
            st.write("### 🛠 Suggestions to improve your password:")
            for tip in feedback:
                st.write(f"✅ {tip}")
    else:
        st.error("⚠️ Please enter a password to check its strength.")

# Footer
st.markdown("""
    🚀 Developed with ❤️ Muqaddas | © 2025 All Rights Reserved
""", unsafe_allow_html=True)