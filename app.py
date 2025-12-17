import streamlit as st
import speech_recognition as sr
import prompts
import evaluator
from llm_service import ask_ai, AI_AVAILABLE

st.set_page_config(page_title="AI Interview Coach", layout="wide")

# ---------------- SESSION STATE ----------------
if "questions" not in st.session_state:
    st.session_state.questions = []
    st.session_state.index = 0
    st.session_state.started = False
    st.session_state.feedback = ""

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎯 Interview Rounds")
mode = st.sidebar.selectbox(
    "Choose Round",
    ["HR Interview", "Technical Interview", "Coding Round"]
)

if AI_AVAILABLE:
    st.sidebar.success("🟢 AI Mode Enabled")
else:
    st.sidebar.warning("🟡 Offline Mode")

# ---------------- UI ----------------
st.markdown("<h1 style='text-align:center;'>🤖 Smart Interview Simulator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Hybrid Mode | Online + Offline</p>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("### 🎥 Video Presence Check")
st.camera_input("Please keep your camera ON")

# ---------------- START ----------------
if st.button("▶ Start Interview"):
    st.session_state.questions = prompts.get_questions(mode)
    st.session_state.index = 0
    st.session_state.feedback = ""
    st.session_state.started = True

# ---------------- INTERVIEW FLOW ----------------
if st.session_state.started and st.session_state.index < len(st.session_state.questions):
    question = st.session_state.questions[st.session_state.index]
    st.subheader(f"Q{st.session_state.index + 1}. {question}")

    # -------- CODING ROUND --------
    if mode == "Coding Round":
        code = st.text_area("Write your code here", height=200)

        if st.button("Evaluate Code"):
            ai_result = ask_ai(prompts.ai_evaluate_code(code))
            st.session_state.feedback = (
                ai_result if ai_result else evaluator.evaluate_code(code)
            )

    # -------- HR / TECH ROUND --------
    else:
        answer = st.text_area("Your Answer", height=150)
        col1, col2 = st.columns(2)

        if col1.button("Submit Text Answer"):
            ai_result = ask_ai(prompts.ai_evaluate_answer(question, answer))
            st.session_state.feedback = (
                ai_result if ai_result else evaluator.evaluate_answer(answer)
            )

        with col2:
            st.markdown("### 🎤 Voice Answer (WAV upload)")
            audio_file = st.file_uploader("Upload WAV", type=["wav"])

            if audio_file:
                recognizer = sr.Recognizer()
                with sr.AudioFile(audio_file) as source:
                    audio = recognizer.record(source)
                try:
                    text = recognizer.recognize_google(audio)
                    st.write("🗣 Recognized:", text)

                    ai_result = ask_ai(prompts.ai_evaluate_answer(question, text))
                    st.session_state.feedback = (
                        ai_result if ai_result else evaluator.evaluate_answer(text)
                    )
                except:
                    st.error("Audio not clear")

    # -------- FEEDBACK + NEXT --------
    if st.session_state.feedback:
        st.markdown("### 📝 Feedback")
        st.success(st.session_state.feedback)

        if st.button("➡ Next Question"):
            st.session_state.feedback = ""
            st.session_state.index += 1
            st.rerun()

elif st.session_state.started:
    st.balloons()
    st.success("🎉 Interview Completed Successfully!")

st.markdown("---")
st.markdown("<center>Open Innovation Project | AI Interview Coach</center>", unsafe_allow_html=True)
