import streamlit as st
import random

# Title and introduction
st.title("Lumina MVP")
st.write("Welcome to Lumina! Your heart-centered leadership assistant.")

# Define feedback logic
def simulate_feedback(tone, stress_level):
    if tone == "Fast" and stress_level > 70:
        return "Your pace and stress levels are high. Try slowing down and taking a breath."
    elif tone == "Empathetic":
        return "Great job connecting emotionally! Balance emotions with clear points."
    elif tone == "Hesitant":
        return "Confidence is key. Practice pauses to deliver your message with clarity."
    elif tone == "Neutral" and stress_level <= 40:
        return "You’re calm and steady. Keep up the great work!"
    else:
        return "Keep refining your communication style to achieve better engagement."

# Welcome Flow
st.header("Welcome to Lumina!")
st.write("Put on your headphones and let's get started.")
if st.button("Start Session"):
    st.write("🎧 Detecting your wearables...")
    st.success("Wearables connected successfully! Let's begin.")

# Simulated Wearables Detection
def detect_wearables():
    detected_wearables = ["Headphones", "Heart Rate Monitor"]
    return detected_wearables

if st.button("Detect Wearables"):
    wearables = detect_wearables()
    if wearables:
        st.success(f"Detected: {', '.join(wearables)}")
    else:
        st.error("No wearables detected. Please try again.")

# Real-Time Feedback
st.header("Real-Time Feedback")
tone = st.selectbox("Choose a simulated tone:", ["Neutral", "Fast", "Empathetic", "Hesitant"])
if st.button("Start Real-Time Feedback"):
    simulated_tone = random.choice(["Neutral", "Fast", "Empathetic", "Hesitant"])
    simulated_stress = random.randint(0, 100)
    st.write(f"Detected Tone: {simulated_tone}")
    st.write(f"Stress Level: {simulated_stress}")
    st.write(f"✨ Coaching Advice: {simulate_feedback(simulated_tone, simulated_stress)}")

# Well-Being Monitoring
st.header("Well-Being Monitoring")
stress_level = st.slider("Stress Level (simulated):", 0, 100, random.randint(30, 70))
if stress_level > 70:
    st.error("🚨 High stress detected: Take a deep breath.")
    st.audio("audio/take_a_breath.mp3")
elif stress_level > 40:
    st.warning("🟡 Moderate stress: Consider a short break.")
else:
    st.success("🟢 Low stress: You're doing great!")

# Motivational Tip
tips = [
    "Remember to pause after key points.",
    "Maintain eye contact with your audience.",
    "Use gestures to emphasize your message.",
    "Keep your tone warm and inviting."
]
st.write(f"💡 Tip of the Day: {random.choice(tips)}")

# Location-Based Feedback
st.header("Location-Based Feedback")
if st.button("Detect Location"):
    st.write("🏠 Detected Location: New York, NY (Mock Data)")

# Footer
st.write("---")
st.write("© 2024 Lumina - Empowering Heart Leadership")