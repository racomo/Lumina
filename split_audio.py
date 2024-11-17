from pydub import AudioSegment

# Load the full audio file
full_audio = AudioSegment.from_mp3("audio/Lumina_Prompts.mp3")

# Define timestamps in milliseconds
segments = {
    "encouragement": (0, 10530),
    "feedback": (20000, 24230),
    "stress_management": (29870, 37490),
    "tone_adjustments": (39070, 50120)
}

# Export each segment as a separate file
for name, (start, end) in segments.items():
    print(f"Processing {name} from {start}ms to {end}ms")
    segment = full_audio[start:end]
    segment.export(f"audio/{name}.mp3", format="mp3")
    print(f"Exported {name}.mp3")
from pydub import AudioSegment

# Load the full audio file
full_audio = AudioSegment.from_mp3("audio/Lumina_Prompts.mp3")

# Define timestamps in milliseconds
segments = {
    "encouragement": (0, 10530),
    "feedback": (20000, 24230),
    "stress_management": (29870, 37490),
    "tone_adjustments": (39070, 50120)
}

# Export each segment as a separate file
for name, (start, end) in segments.items():
    segment = full_audio[start:end]
    segment.export(f"audio/{name}.mp3", format="mp3")

