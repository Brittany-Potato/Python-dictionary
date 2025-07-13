
#* Google Gemini API
# Requiring an API key and NOT a service account certificate

# Gemini is Googles family of multimodal models (like Gemini 1.5 pro or flash). 
# You can access it via the Google Generative AI API using an API key (simpler than OAuth or service accounts)

#* Prerequisites 
# Python 3.7+, A Google Cloud Project, Biling enabled on the project, Gemini API enabled on your project and an API key (Generated via Google CLoud Console)

#* Steps: Setup and use

# Step One
# Enable the Gemini API
# Go to Google Cloud Console -> Select or create a project -> Go to "APIs & Services" -> Library -> Search and enable: Generative Language API
# Go to "APIs & services" -> credentials -> Click + CREATE CREDENTIALS -> API key -> #! Copy the key securely

# Step Two
# Install Googles offical SDK:
# pip install google-generativeai

# Step Three
# You'll use the 'google.generativeai' library.

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# You can also use dotenv / enviroment variables for safety

# export GOOGLE_API_KEY = "Your-api-key-here"

import os 
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#* Gemini has different models:

# "models/gemini-pro" - Text based
# "models/gemini-pro-vision" - multimodal (Image & Text)
# "models/gemini-1.5-pro-latest" - most powerful (streaming, longer context)
# "models/gemini-1.5-flash-latest" - fastest and cheapest

#* Example: Text prompt(chat)

model = genai.GenerativeModel(model_name="models/gemini-.15-pro-latest")

response = model.generate_content("What is the capital of France?")
print(response.text)

#* Chat with History (for memory-style bots)

chat = model.start_chat(history=[])

response = chat.send_message("Who was Ada Lovelace?")
print(response.text)

response = chat.send_message("What did she do?")
print(response.text)

#* Vision example (Image + Text)

# from PIL import Image

model = genai.GenerativeModel("models/gemini-pro-vision")

image = Image.open("your_image.jpg")

response = model.generate_content([
    image,
    "Describe what is happening"
])

print(response.text)

#* Gemini API parameters you should know

# temperature -> Controls randomness (0 = determinitic)
# top_k -> Sample from top K options
# top_p -> Nucleus samplin
# max_output_tokens -> Max length of response
# safety_settings -> Filter unsafe content

#* Example

model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro-latest",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 2048
    }
)

#* Handling responses 
# Responses are returned as response.text, but you can also access JSON-like data:

print(response.candidates) # raw data

#* Quote and limits

# Free tier available via Google AI studio
# Paid usage requires biling enabled 
# Daily usage quota and rate limits apply

#* Security & Best Practices

# Don't hardcode API keys in code pushed to Github
# Use ".env" or enviroment variables
# Restrict API key (via HTTP referrer or IP address)
# Handle errors gracefully using try/except

#* Safe error handling Example

try:
    response = model.generate_content("Write a poem about the moon")
    print(response.text)
except Exception as e:
    print("Error:", e)
    
