import google.generativeai as genai
import os
import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Gemini Text Generator",
    page_icon="✨",
    layout="centered",
)

# --- Sidebar ---
st.sidebar.title("⚙️ Settings")
st.sidebar.write("Choose your model and start generating text!")

model_choice = st.sidebar.radio(
    "Select Gemini Model:",
    ["gemini-1.5-flash", "gemini-1.5-pro"],
    index=0
)

# Get API from Environment Variable
key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=key)

# Initialize model
model = genai.GenerativeModel(model_choice)

# --- Main UI ---
st.title("✨ Gemini Text Generator")
st.markdown("Write a prompt and let **Google Gemini** generate creative responses!")

prompt = st.text_area(
    "📝 Enter your prompt below:",
    placeholder="e.g. Write a short story about a robot who learns to paint...",
    height=150,
    max_chars=10000
)

if st.button("🚀 Generate"):
    if prompt.strip():
        with st.spinner("Generating response..."):
            response = model.generate_content(prompt)

        # Styled response card
        st.success("✅ Response Generated!")
        st.markdown(
            f"""
            <div style="
                background-color:#f0f2f6;
                padding:15px;
                border-radius:10px;
                box-shadow:0 4px 8px rgba(0,0,0,0.1);">
                <p style="font-size:16px; color:#333;">{response.text}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("⚠️ Please enter a prompt before generating.")

# --- Footer ---
st.markdown(
    """
    <hr>
    <div style="text-align:center; color:gray;">
    Built with ❤️ using Streamlit & Google Gemini
    </div>
    """,
    unsafe_allow_html=True
)
