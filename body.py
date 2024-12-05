# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import nltk
from nltk.stem import WordNetLemmatizer
import pyttsx3
import speech_recognition as sr
import pyaudio

# Download NLTK data
nltk.download('wordnet')
nltk.download('punkt')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Define training data
train_data = pd.DataFrame({
    'input': ['hello', 'hi', 'how are you', 'what is your name'],
    'response': ['Hi, how can I help?', 'Hello!', 'I\'m doing well, thanks.', 'My name is AI Assistant.']
})

# Vectorize input data
vectorizer = TfidfVectorizer()
input_vectors = vectorizer.fit_transform(train_data['input'])

# Define model architecture
def create_model(input_shape):
    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape=(input_shape,)))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(len(train_data), activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Train model
input_train, input_test, response_train, response_test = train_test_split(input_vectors, train_data['response'], test_size=0.2)
model = create_model(input_vectors.shape[1])
model.fit(input_train, response_train, epochs=100, batch_size=8)

# Define function to generate response
def generate_response(input_text):
    input_vector = vectorizer.transform([input_text])
    prediction = model.predict(input_vector)
    response_index = np.argmax(prediction)
    return train_data['response'].iloc[response_index]

# Define function for text-to-speech
def speak(text, voice='female'):
    engine.setProperty('voice', voice)
    engine.say(text)
    engine.runAndWait()

# Define function for speech recognition
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return 'Sorry, I didn\'t understand.'

# Test AI
def test_ai():
    print('Welcome to AI Chatbot!')
    voice_type = input('Choose voice type (male/female): ')
    while True:
        print('Type "listen" to switch to voice input.')
        user_input = input('You: ')
        if user_input.lower() == 'listen':
            while True:
                user_input = listen()
                print('You:', user_input)
                response = generate_response(user_input)
                print('AI:', response)
                speak(response, voice_type)
        else:
            response = generate_response(user_input)
            print('AI:', response)
            speak(response, voice_type)

if __name__ == "__main__":
    test_ai()
