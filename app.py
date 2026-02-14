import random
import streamlit as st
import time

st.title("💻 Quiz Game")



# Questions dictionary
questions = {
    "What does CPU stand for?": "central processing unit",
    "What does GPU stand for?": "graphics processing unit",
    "What does RAM stand for?": "random access memory",
    "What does PSU stand for?": "power supply",
    "What does HTML stand for?": "hyper text markup language",
    "What does CSS stand for?": "cascading style sheets"
}

# Initialize session state
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.score = 0
    st.session_state.current = 0
    st.session_state.selected_questions = random.sample(
        list(questions.items()), 5
    )

# Start Button
if not st.session_state.started:
    if st.button("Start Quiz"):
        st.session_state.started = True
        st.rerun()

# Quiz Logic
if st.session_state.started:

    if st.session_state.current < 5:

        ques, correct_ans = st.session_state.selected_questions[
            st.session_state.current
        ]

        answer = st.text_input(ques, key=st.session_state.current)

        if st.button("Submit", key=f"submit_{st.session_state.current}"):

            if answer.strip().lower() == correct_ans:
                st.success("Correct Answer ✅")
                time.sleep(5)
                st.session_state.score += 1
            else:
                st.error("Incorrect Answer ❌")
                time.sleep(5)

            st.session_state.current += 1
            st.rerun()

    else:
        st.subheader("🎉 Quiz Finished!")
        st.write(f"You got {st.session_state.score} correct out of 5!")
        percentage = (st.session_state.score / 5) * 100
        st.write(f"Your correct percentage = {percentage:.2f}%")

        if st.button("Restart Quiz"):
            st.session_state.started = False
            st.session_state.score = 0
            st.session_state.current = 0
            st.session_state.selected_questions = random.sample(
                list(questions.items()), 5
            )
            st.rerun()
