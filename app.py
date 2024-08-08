import streamlit as st
from OpenAI_Screen import OpenAI_App
# from HuggingFace_Screen import HuggingFace_App
from Gemanai_Screen import Gemanai_App
from styles import overall_css

# Set page configuration
st.set_page_config(layout="wide")

# Apply the CSS styles
st.markdown(overall_css, unsafe_allow_html=True)

def main():
    st.title("Generative Artifical Intellegence")

    col1,  col3 = st.columns(2)

    with col1:
        if st.button("OpenAI"):
            st.session_state.page = "OpenAI"
    with col3:
        if st.button("Gemanai"):
            st.session_state.page = "Gemanai"

    # Set default page
    if "page" not in st.session_state:
        st.session_state.page = "OpenAI"

    # Navigation
    if st.session_state.page == "OpenAI":
        OpenAI_App()

    elif st.session_state.page == "Gemanai":
        Gemanai_App()

if __name__ == "__main__":
    main()
