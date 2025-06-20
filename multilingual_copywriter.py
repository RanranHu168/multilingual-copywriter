import streamlit as st
from prompts import generate_prompt
from openai_api import get_copy
from dotenv import load_dotenv

load_dotenv()  

st.set_page_config(page_title="Multilingual AI Copywriting Tool", page_icon="🌍")
st.title(" Multilingual Product Copywriting Generator")


product_name = st.text_input("Product Name")
product_features = st.text_area("Product Features (separate with commas)")
tone = st.selectbox("Writing Tone", ["Formal", "Enthusiastic", "Playful"])
languages = st.multiselect("Select Output Languages", ["English", "中文", "Français"])


if st.button("Generate Copy"):
    if not product_name or not product_features or not languages:
        st.warning("Please complete all fields before generating.")
    else:
        for lang in languages:
            prompt = generate_prompt(product_name, product_features, tone, lang)
            with st.spinner(f"Generating copy in {lang}..."):
                result = get_copy(prompt)
            st.markdown(f"### ✨ Generated Copy ({lang}")
            st.text_area(f"{lang} Output", result, height=200)
