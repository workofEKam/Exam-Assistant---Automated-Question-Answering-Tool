import speech_recognition as sr
import pyttsx3
import time
import requests
import asyncio
import aiohttp

# Initialize the TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set a slower speech rate

# API details
API_URL = "https://api.hyperbolic.xyz/v1/chat/completions"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJla3Nob3J0c3l0QGdtYWlsLmNvbSIsImlhdCI6MTczNTc5NDc1OH0.OtnU0PYVPVBFKwOyPFRLXO2upa2EBhiIkhWe27wUbRU"

def speak(text, delay=False):
    """Function to speak the given text. Add delay after full stops only if delay=True."""
    if delay:
        sentences = text.split('.')  # Split text into sentences based on full stops
        for sentence in sentences:
            if sentence.strip():  # Ignore empty sentences
                words = sentence.split()  # Split sentence into words
                engine.say(sentence.strip())  # Speak the sentence
                engine.runAndWait()
                pause = 1 * len(words)  # Reduced delay: 1 * number of words
                time.sleep(pause)  # Pause for the calculated delay
    else:
        engine.say(text)  # Speak the text without delay
        engine.runAndWait()

def listen_to_command():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 2.5 
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Reduced ambient noise adjustment
        speak("Listening...")

        try:
            # Listen for audio with a reduced timeout
            audio = recognizer.listen(source, timeout=2)
            print("Processing...")

            # Use Google Web Speech API to recognize the audio
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command

        except sr.WaitTimeoutError:
            print("Listening timed out. Please speak again.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; check your network connection. Error: {e}")
    
    return None

async def call_api(query):
    """Function to call the API with the user's query asynchronously."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "messages": [
            {
                "role": "system",  # System message to instruct the API
                "content": "it is a quiz of probability and statistics , give me the final answer avoid any explanation  ."
            },
            {
                "role": "user",
                "content": query
            }
        ],
        "model": "deepseek-ai/DeepSeek-V3",
        "max_tokens": 500,  # Reduced max_tokens for faster response
        "temperature": 0.1,
        "top_p": 0.9
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(API_URL, headers=headers, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    return result["choices"][0]["message"]["content"].strip()  # Extract the response text
                else:
                    print(f"Error: {response.status}")
                    return None
        except Exception as e:
            print(f"Failed to call API: {e}")
            return None

def confirm_question(question):
    """Function to confirm the question with the user."""
    speak(f"You said: {question}")  # Repeat the question (no delay)
    speak("Are we good to go, or do you want to make a change?")  # Ask for confirmation (no delay)
    confirmation = listen_to_command()
    return confirmation

async def main():
    while True:
        print("Speak your question...")
        question = listen_to_command()
        if question:
            # Confirm the question
            confirmation = confirm_question(question)
            if confirmation and "no change" in confirmation.lower():
                # Proceed to call the API
                response = await call_api(question)
                if response:
                    print(f"API says: {response}")
                    speak(response, delay=True)  # Speak the API response with delay
                else:
                    print("Failed to get a response from the API.")
            elif confirmation and "change" in confirmation.lower():
                # Listen to the question again
                continue
            else:
                print("Confirmation not understood. Please try again.")
        else:
            print("No question received. Try again.")

if __name__ == "__main__":
    asyncio.run(main())