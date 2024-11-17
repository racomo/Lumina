import streamlit as st
import random  # Simulates real-time changes for demo purposes

# Title and description
st.title("Lumina MVP")
st.write("Welcome to Lumina! Your real-time feedback and well-being assistant.")

# Real-Time Feedback Section
st.header("Real-Time Feedback")
st.write("Analyze communication tone and pacing.")

# Simulate a tone and pacing analyzer
tone = st.radio(
    "Select a tone to simulate:",
    ["Neutral", "Fast", "Empathetic", "Hesitant"],
    key="tone_radio"
)
if tone == "Fast":
    st.write("⚡ **Tip:** Slow down your pace to ensure clarity.")
elif tone == "Empathetic":
    st.write("💡 **Great job!** You're connecting emotionally.")
elif tone == "Hesitant":
    st.write("❓ **Tip:** Pause for clarity and confidence.")
else:
    st.write("✅ **Neutral tone detected:** Maintain consistency.")

# Well-Being Monitoring Section
st.header("Well-Being Monitoring")
st.write("Simulate stress levels and receive tips for well-being.")

# Simulate stress levels with a slider
stress_level = st.slider(
    "Stress Level (simulated):",
    min_value=0,
    max_value=100,
    value=random.randint(30, 70),
    key="stress_slider"
)
if stress_level > 70:
    st.write("🚨 **High Stress Detected:** Take a deep breath and relax.")
elif 40 < stress_level <= 70:
    st.write("🟡 **Moderate Stress:** Consider taking a short break.")
else:
    st.write("🟢 **Low Stress:** You're doing great. Keep it up!")

# Simulated feedback loop
if st.button("Refresh Simulation"):
    st.experimental_rerun()