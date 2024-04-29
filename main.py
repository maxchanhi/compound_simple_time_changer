
from melody import main_generate
from notation import fun_emoji_list
import asyncio,random
from asynchronous import score_generation
import streamlit as st
from streamlit_extras.let_it_rain import rain

st.set_page_config(
    page_title="Simple Compound Time Translation Quiz")

def display_question(question_data):
    st.write(question_data['question'])
    st.image("static/cropped_score_question_melody.png", caption='Question')
    """____________________________________"""
    # Display options as images
    for idx, option in enumerate(question_data['options']):
        container = st.container()
        col1, col2 = container.columns([5, 1])
        col1.image(f"static/cropped_score_wr_option_{idx}.png")
        col2.markdown(f"")
        col2.markdown(f"Option {idx + 1}")

    option_selected = st.radio("Choose the correct option:", 
                               options=[f'Option {i + 1}' for i in range(len(question_data['options']))])

    if st.button("Submit Answer"):
        correct_idx = None
        for idx, (time, melody) in enumerate(question_data["options"]):
            if time == question_data["answer"][0] and melody == question_data["answer"][1]:
                correct_idx = idx + 1
                print(correct_idx)
                break

        if option_selected == f"Option {correct_idx}":
            fun_emoji = random.choice(fun_emoji_list)
            st.success(f"Correct! {fun_emoji}")
            rain(emoji=fun_emoji, animation_length="1")
        else:
            st.error(f"Wrong answer! The correct answer is Option {correct_idx}")


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
    print(st.session_state.question_data)
