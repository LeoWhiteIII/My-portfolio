import streamlit as st

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Define navigation function
def nav_to(page):
    st.session_state.page = page

# Navigation buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏠 Home"):
        nav_to("Home")
with col2:
    if st.button("📄 Resume"):
        nav_to("Resume")
with col3:
    if st.button("🛠️ Projects"):
        nav_to("Projects")

st.divider()

# Display page based on selection
if st.session_state.page == "Home":
    st.title("Welcome to My Portfolio 👋")
    st.write("Hi! my name is Leo White and I am a currently enrolled computer science Sophmore (Jr credit standing) at Seattle University in Seattle Washington. This page is a a way for me to highlight my projects and resume's in a more simplistic way, please click any of the tabs above for more information.")
elif st.session_state.page == "Resume":
    st.title("📄 Resume")
    st.write("Here is a downloadable link to my resume:")

    pdf_path = "Resume.pdf"

    pdf_url = "https://drive.google.com/file/d/18wb_5f3nq1moZboHakXS7FJOjUDrJPQG/view?usp=drive_link"  # Replace with actual hosted link
    st.markdown(f'<iframe src="{pdf_url}" width="700" height="800"></iframe>', unsafe_allow_html=True)




    with open(pdf_path, "rb") as file:
        pdf_bytes = file.read()
        st.download_button(label="📥 Download Resume", 
                        data=pdf_bytes, 
                        file_name="Leo_Resume.pdf", 
                        mime="application/pdf")

elif st.session_state.page == "Projects":
    st.title("🛠️ Projects")
    st.write("Here are some cool projects I've done...")
