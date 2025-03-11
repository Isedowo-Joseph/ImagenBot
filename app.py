import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()

# Set OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')



st.title("AI Image Generator App")

st.write("Enter a prompt and click 'Generate' to create an image")

prompt = st.text_input("Enter your image prompt:")

if st.button("Generate"):
    if prompt:
        try:
            client = openai.OpenAI()
            response = client.images.generate(
                model="dall-e-3",  # Specify the model (dall-e-2 or dall-e-3)
                prompt=prompt,
                n=1,
                size="1024x1024"
            )

            image_url = response.data[0].url
            
            # Fetch the image
            image_response = requests.get(image_url)
            img = Image.open(BytesIO(image_response.content))

            st.image(img, caption="Generated Image", use_column_width=True)

        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        st.error("Please enter a prompt to generate an image")
