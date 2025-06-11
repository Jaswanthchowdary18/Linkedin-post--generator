import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
import streamlit.components.v1 as components

# --- Configuration ---
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

st.set_page_config(
    page_title="LinkedIn Post Generator",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.codebasics.io/contact',
        'Report a bug': "https://github.com/codebasics/linkedin-post-generator/issues",
        'About': "# This is a LinkedIn Post Generator by Codebasics. AI-powered content creation for professionals!"
    }
)

def main():
    st.markdown(
        """
        <style>
        .header-title {
            text-align: center;
            color: #2F80ED;
            font-size: 2.5em;
            margin-bottom: 0.5em;
            font-weight: bold;
        }
        .header-subtitle {
            text-align: center;
            color: #555555;
            font-size: 1.1em;
            margin-bottom: 1.5em;
        }
        .stButton>button {
            background-color: #2F80ED;
            color: white;
            border-radius: 8px;
            height: 3em;
            font-size: 1.1em;
            font-weight: bold;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #286FCA;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # --- Header ---
    st.markdown("<h1 class='header-title'>🚀 Pro LinkedIn Post Generator</h1>", unsafe_allow_html=True)
    st.markdown("<p class='header-subtitle'>Craft engaging LinkedIn posts effortlessly with AI!</p>", unsafe_allow_html=True)
    st.markdown("---")

    fs = FewShotPosts()
    tags = fs.get_tags()

    st.header("⚙️ Post Settings")
    st.write("Configure your post's topic, length, and language:")

    col1, col2, col3 = st.columns(3)
    with col1:
        selected_tag = st.selectbox("🔖 **Select Topic:**", options=tags)
    with col2:
        selected_length = st.selectbox("📏 **Select Length:**", options=length_options)
    with col3:
        selected_language = st.selectbox("🗣️ **Select Language:**", options=language_options)

    st.markdown("---")

    st.subheader("✨ Generate Your Post")
    st.write("Click the button below to instantly create a LinkedIn post based on your selections.")

    col_gen_btn_1, col_gen_btn_2, col_gen_btn_3 = st.columns([1, 2, 1])
    with col_gen_btn_2:
        if st.button("🚀 Generate Post", use_container_width=True):
            with st.spinner("Generating your professional LinkedIn post..."):
                try:
                    post = generate_post(selected_length, selected_language, selected_tag)
                    st.session_state['generated_post'] = post
                    st.session_state['trigger_scroll'] = True
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.warning("Please try again or contact support.")

    # --- Inject Scroll Script ---
    if st.session_state.get("trigger_scroll"):
        components.html(
            """
            <script>
            window.scrollBy({ top: 200, left: 0, behavior: 'smooth' });
            </script>
            """,
            height=0,
        )
        st.session_state["trigger_scroll"] = False

    # --- Show Post ---
    if 'generated_post' in st.session_state and st.session_state['generated_post']:
        st.markdown("---")
        st.subheader("🎯 Your Generated Post:")
        st.text_area(
            "Generated Post:",
            st.session_state['generated_post'],
            height=250,
            key="generated_post_textarea",
            help="Your AI-generated LinkedIn post. Select and copy to use!"
        )

    st.markdown("---")
    st.markdown(
        """
        <p style='text-align: center; color: gray; font-size: 0.9em;'>
            Powered by AI | Developed by <a href='https://www.linkedin.com/in/jaswanth-chowdary-5b4113253/' target='_blank' style='color: #2F80ED;'>Jaswanth</a>
        </p>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
