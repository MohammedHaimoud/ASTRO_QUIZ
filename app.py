from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "animation_space.json"
QUIZ_FILE = ASSETS / "astronomy_quiz.json"


# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# Function to load quiz questions
def load_quiz(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# Function to apply snowfall effect (optional)
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")


# Function to get the name from query parameters
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Friend"])[0]


# Function to display the quiz
def display_quiz(quiz):
    st.subheader("Astronomy and Space Quiz")
    score = 0
    for question in quiz:
        st.markdown(f"**{question['question']}**")
        options = question["options"]
        answer = st.radio("", options, key=question['id'])
        if answer == question["answer"]:
            score += 1
    st.markdown(f"### Your Score: {score}/{len(quiz)}")


# Page configuration
st.set_page_config(page_title="Astronomy Quiz", page_icon="🚀")

# Run snowfall animation (optional)
# run_snow_animation()

# Apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Display header with personalized name
PERSON_NAME = get_person_name()
st.header(f"Welcome to the Astronomy Quiz, {PERSON_NAME}! 🚀", anchor=False)

# Display the Lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-space", height=300)

# Load and display the quiz
quiz = load_quiz(QUIZ_FILE)
display_quiz(quiz)
