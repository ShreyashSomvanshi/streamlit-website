import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieURL(url):
    r=requests.get(url);
    if r.status_code != 200:
        return None
    return r.json()

# Load CSS for contact form
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# Load assests
lottie_coding = load_lottieURL("https://assets4.lottiefiles.com/packages/lf20_dews3j6m.json")

# Header section
with st.container():
    st.subheader("Hi, I am Shreyash :wave:")
    st.title("An AI Researcher and Data Scientist from India")
    st.write("I am passionate about finding new ways to use Python to be more efficient.")
    st.write("[Learn More >](https://shreyashsomvanshi.github.io/portfolio/)")

# What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            Will add later:
            -hi
            -hello
            -working on it
            """
            )
        st.write("[GitHub >](https://github.com/ShreyashSomvanshi/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="data")


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        # insert image
        st.write("coming soon !")

    with text_column:
        # insert text
        st.write("coming soon !")

# Contact Form
with st.container():
    st.write("---")
    st.header("Get In Touch with Me!")
    st.write("##")

    # Reference: formsubmit.co
    contact_form = """
    <form action="https://formsubmit.co/shreyashsomvanshi03@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your Name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea>
         <button type="submit">Send</button>
     </form>

    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html = True)
    with right_column:
        st.empty()
