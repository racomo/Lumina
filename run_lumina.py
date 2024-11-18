import os

# Path to your virtual environment
venv_path = os.path.expanduser("~/lumina_venv/bin/activate")

# Activate the virtual environment and run Streamlit
os.system(f"source {venv_path} && streamlit run lumina_app.py")

