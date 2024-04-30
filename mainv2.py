
from melody import main_generate
from notation import fun_emoji_list
import asyncio,random
from asynchronous import score_generation
import streamlit as st
from streamlit_extras.let_it_rain import rain
if 'option_selected' not in st.session_state:
        st.session_state.option_selected = []
st.set_page_config(
    page_title="Simple Compound Time Translation Quiz")
def display_question(question_data):
    st.subheader(question_data['question'])
    st.image("static/cropped_score_question_melody.png", caption='Question')
    """_________________________"""

    if 'option_selected' not in st.session_state:
        st.session_state.option_selected = None

    def select_option(idx):
        if st.session_state.option_selected is not None:
            st.session_state[f"disabled_{st.session_state.option_selected}"] = False
        st.session_state.option_selected = idx
        st.session_state[f"disabled_{idx}"] = True

    for idx, option in enumerate(question_data['options']):
        container = st.container()
        col1, col2 = container.columns([5, 1])
        col1.image(f"static/cropped_score_wr_option_{idx}.png")
        
        if f"disabled_{idx}" not in st.session_state:
            st.session_state[f"disabled_{idx}"] = False

        col2.button(
            f'Option {idx + 1}',
            key=f"option_{idx}",
            on_click=select_option,
            args=(idx,),
            disabled=st.session_state[f"disabled_{idx}"]
        )

    if st.button("Submit Answer"):
        correct_idx = None
        for idx, (time, melody) in enumerate(question_data["options"]):
            if time == question_data["answer"][0] and melody == question_data["answer"][1]:
                correct_idx = idx
                break

        if st.session_state.option_selected == correct_idx:
            fun_emoji = random.choice(fun_emoji_list)
            st.success(f"Correct! {fun_emoji}")
            rain(emoji=fun_emoji, animation_length="1")
        else:
            st.error(f"Wrong answer! The correct answer is Option {correct_idx + 1}")


if __name__ == "__main__":
    st.title("Compound-simple-time Modulation Quiz")
    if 'question_data' not in st.session_state:
        
        st.session_state.question_data = main_generate()
        print(st.session_state.question_data)
        asyncio.run(score_generation(st.session_state.question_data))

    if st.button("Generate New Question"):
        st.session_state.question_data = main_generate()
        asyncio.run(score_generation(st.session_state.question_data))
    display_question(st.session_state.question_data)
    print(st.session_state.question_data)