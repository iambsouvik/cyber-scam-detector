import streamlit as st
import re

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Cyber Scam Detector Pro",
    page_icon="🛡️",
    layout="wide"
)

# =========================
# HEADER
# =========================
st.markdown("""
# 🛡️ Cyber Scam Detector Pro

### AI-Powered Scam & Phishing Detection Tool

Detect suspicious messages, emails, SMS, and scam links instantly.

---
👨‍💻 Developed by Souvik Bhadra
""")

st.info("🔐 Stay Safe Online • Detect Scam Messages • Protect Your Data")

# =========================
# INPUT BOX
# =========================
message = st.text_area(
    "📩 Paste suspicious message, email, SMS or link below:",
    height=200
)

message = message or ""

# =========================
# SCAM KEYWORDS
# =========================
keywords = [
    # English
    "otp", "password", "bank", "click here", "urgent", "verify",
    "verify account", "winner", "prize", "claim now", "gift",
    "limited offer", "account suspended", "lottery", "free",

    # Bengali
    "অভিনন্দন", "পুরস্কার", "জিতেছেন", "ওটিপি", "ব্যাংক",
    "লিংকে ক্লিক করুন", "অ্যাকাউন্ট যাচাই", "জরুরি", "ফ্রি"
]

# =========================
# ANALYSIS BUTTON
# =========================
if st.button("🔍 Analyze Message"):

    score = 0
    detected_keywords = []

    # -------------------------
    # Keyword Detection
    # -------------------------
    for keyword in keywords:
        if keyword.lower() in message.lower():
            score += 1
            detected_keywords.append(keyword)

    # -------------------------
    # URL Detection
    # -------------------------
    urls = re.findall(r'https?://\S+|www\.\S+', message)
    if urls:
        score += 2

    # -------------------------
    # EMAIL Detection
    # -------------------------
    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        message
    )
    if emails:
        score += 1

    # =========================
    # RISK CALCULATION
    # =========================
    if score >= 4:
        risk_level = "🔴 HIGH RISK"
    elif score >= 2:
        risk_level = "🟠 MEDIUM RISK"
    else:
        risk_level = "🟢 LOW RISK"

    risk_percentage = min(score * 25, 100)

    # =========================
    # RESULTS UI
    # =========================
    st.subheader("📊 Risk Analysis")
    st.progress(risk_percentage)
    st.success(f"Risk Percentage: {risk_percentage}%")

    st.subheader("🚨 Result")
    st.markdown(f"## {risk_level}")

    # =========================
    # DETECTED DATA
    # =========================
    st.subheader("🔍 Detected Keywords")
    if detected_keywords:
        st.write(detected_keywords)
    else:
        st.write("No suspicious keywords detected.")

    if urls:
        st.subheader("🌐 Detected URLs")
        st.warning(urls)

    if emails:
        st.subheader("📧 Detected Emails")
        st.warning(emails)

    # =========================
    # SECURITY ADVICE
    # =========================
    st.subheader("💡 Security Advice")

    if score >= 4:
        st.error(
            "⚠️ Highly suspicious message. Do NOT click links or share OTP, password, or banking details."
        )

    elif score >= 2:
        st.warning(
            "⚠️ Be careful. Verify sender before taking any action."
        )

    else:
        st.success(
            "✅ No major scam indicators found. Still stay alert online."
        )

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("🛡️ Cyber Scam Detector Pro | Developed by Souvik Bhadra")