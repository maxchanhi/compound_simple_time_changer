
from melody import main_generate
import asyncio
from asynchronous import score_generation
import streamlit as st

st.set_page_config(
    page_title="Simple Compound Time Translation Quiz")
st.header('Simple Time and Compound Time Translation Quiz')
def display_question(question_data):
    st.write(question_data['question'])
    st.image("static/cropped_score_question_melody.png", caption='Question')
    st.divider()
    # Display options as images
    for idx, option in enumerate(question_data['options']):
        st.image(f"static/cropped_score_wr_option_{idx}.png", caption=f'Option {idx + 1}')

    # Radio button for options
    option_selected = st.radio("Choose the correct option:", 
                               options=[f'Option {i + 1}' for i in range(len(question_data['options']))],horizontal=True)

    if st.button("Submit Answer"):
        for idx in range(len(question_data["options"])):
            if question_data["options"][idx][1]==question_data["answer"][1]:
                correct_idx = idx+1
        if option_selected == f"Option {correct_idx}":
            st.success("Correct answer!")
        else:
            st.error(f"Wrong answer! The correct answer is Option {correct_idx} ")


if __name__ == "__main__":
    st.title("Compound-simple-time Modulation Quiz")
    if 'question_data' not in st.session_state:
        
        st.session_state.question_data = main_generate()
        print(st.session_state.question_data)
        asyncio.run(score_generation(st.session_state.question_data))
        #score_generation(st.session_state.question_data)
    if st.button("Generate New Question"):
        st.session_state.question_data = main_generate()
        asyncio.run(score_generation(st.session_state.question_data))
        #score_generation(st.session_state.question_data)
    display_question(st.session_state.question_data)
