from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.webview import WebView
from kivy.clock import Clock
import random


class LuminaApp(App):
    def build(self):
        # Main layout
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Welcome message
        self.layout.add_widget(Label(
            text="Welcome to Lumina! Your heart-centered leadership assistant.",
            font_size='18sp',
            halign='center'
        ))

        # Wearables Detection Button
        self.detect_wearables_button = Button(text="Detect Wearables")
        self.detect_wearables_button.bind(on_press=self.detect_wearables)
        self.layout.add_widget(self.detect_wearables_button)

        # Real-Time Feedback
        self.layout.add_widget(Label(
            text="Simulated Tone and Pace Feedback",
            font_size='16sp',
            halign='center'
        ))
        self.feedback_label = Label(text="", halign='center')
        self.layout.add_widget(self.feedback_label)
        self.tone_button = Button(text="Simulate Tone Feedback")
        self.tone_button.bind(on_press=self.simulate_tone_feedback)
        self.layout.add_widget(self.tone_button)

        # Stress Level Slider
        self.layout.add_widget(Label(
            text="Adjust Stress Level",
            font_size='16sp',
            halign='center'
        ))
        self.stress_slider = Slider(min=0, max=100, value=50)
        self.stress_slider.bind(value=self.update_stress_level)
        self.layout.add_widget(self.stress_slider)
        self.stress_label = Label(text="Stress Level: 50", halign='center')
        self.layout.add_widget(self.stress_label)

        # Google Maps WebView
        self.layout.add_widget(Label(
            text="Location-Based Feedback (Google Maps)",
            font_size='16sp',
            halign='center'
        ))
        self.webview = WebView(
            url="https://www.google.com/maps/embed/v1/place?key=AIzaSyAuity_NJAVniRBBGjy5CUWcIc6wEfbCEg&q=New+York"
        )
        self.layout.add_widget(self.webview)

        # Tip of the Day
        self.tip_label = Label(
            text="💡 Tip of the Day: Stay calm and confident during your sessions.",
            font_size='14sp',
            halign='center'
        )
        self.layout.add_widget(self.tip_label)
        Clock.schedule_interval(self.update_tip_of_the_day, 10)

        return self.layout

    def detect_wearables(self, instance):
        detected_wearables = ["Headphones", "Heart Rate Monitor"]  # Simulated detection
        self.feedback_label.text = f"Detected: {', '.join(detected_wearables)}"

    def simulate_tone_feedback(self, instance):
        tones = ["Neutral", "Fast", "Empathetic", "Hesitant"]
        tone = random.choice(tones)
        feedback = {
            "Fast": "You’re speaking too quickly. Try pausing between points.",
            "Empathetic": "Great job connecting with your audience! Keep it up.",
            "Hesitant": "You seem unsure. Focus on building confidence.",
            "Neutral": "Your tone is steady. Maintain this consistency.",
        }.get(tone, "Keep going, you’re doing well!")
        self.feedback_label.text = f"Tone: {tone}\nFeedback: {feedback}"

    def update_stress_level(self, instance, value):
        self.stress_label.text = f"Stress Level: {int(value)}"
        if value > 70:
            self.feedback_label.text = "🚨 High stress detected: Take a deep breath."
        elif value > 40:
            self.feedback_label.text = "🟡 Moderate stress: Consider a short break."
        else:
            self.feedback_label.text = "🟢 Low stress: You’re doing great!"

    def update_tip_of_the_day(self, dt):
        tips = [
            "💡 Remember to pause after key points.",
            "💡 Maintain eye contact with your audience.",
            "💡 Use gestures to emphasize your message.",
            "💡 Keep your tone warm and inviting.",
            "💡 Focus on clarity and confidence."
        ]
        self.tip_label.text = random.choice(tips)


if __name__ == '__main__':
    LuminaApp().run()
