import streamlit as st
import enchant
d = enchant.Dict("en_US")
st.title("UNLIMITED WORD GAME")
def check_word():
    count = 0
    found = []
    try:

        if 'count' not in st.session_state:
            st.session_state.count = 0
        if 'found' not in st.session_state:
            st.session_state.found = []
        word = st.text_input("Enter a 7 letter word", max_chars=7)
        word = word.lower()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(' ')
        with col2:
            quit = st.button(label = "QUIT GAME")
        with col3:
            st.write(' ')

        if (d.check(word) and word not in st.session_state.found):
            st.session_state.found.append(word)
            st.session_state.count += 1
            st.write(":smile:" + "GREAT")
        elif quit:
            st.balloons()
            st.write("**YOUR FINAL SCORE WAS : **", st.session_state.count)

        elif (d.check(word) and word in st.session_state.found):
            st.warning("ALREADY FOUND")
        else:
            st.write("Try again")
    except ValueError:
        st.write("INPUT CANT BE BLANK")

        if quit:
            st.ballons()
            st.write("**YOUR FINAL SCORE WAS : **", st.session_state.count)





check_word()
st.write('the count is : ', st.session_state.count)
with st.expander("WORDS FOUND"):

    st.write('words found : ', st.session_state.found)
