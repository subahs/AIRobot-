from neuralintents import GenericAssistant
from numpy.core.fromnumeric import take
import speech_recognition as sr
import pyttsx3 as tts
import sys
import pyaudio
recognizer = sr.Recognizer()
# recognizer.energy_threshold = 4000
speaker = tts.init()
speaker.setProperty("rate", 120)
programs = ['electronics', 'computer', 'civil']
hod = ["Shivahari Aacharya", 'Resha Deo', 'Madan Kadariya']
contact = ['9 8 6 6 1 0 6 6 0 0', '9 8 4 3 6 8 4 6 2 2', '9 8 6 3 2 5 2 5 1 5']
def takeInput() :
    with sr.Microphone() as mic :
        recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
        audio = recognizer.listen(mic)
        note = recognizer.recognize_google(audio)
        note = note.lower()
    return note
def giveOutput(str):
    global recognizer
    speaker.say(str)
    speaker.runAndWait()
def admission():

    giveOutput('Can you please let me know in which program you want to get admitted?')
    done = False
    while not done :
        try:
            with sr.Microphone() as mic :
                print('speak')
                note = takeInput()
                print(note)
                if note in programs :
                    ind = programs.index(note)
                    giveOutput(f'you can contact {hod[ind]} for admission in {programs[ind]}. Please note down the contact number {contact[ind]}')
                    done = True
                else :
                    giveOutput('I did not get that, please repeat')
        except sr.UnknownValueError :
            recognizer = sr.Recognizer()
            speaker.say('I did not get that, Please repeat')
            speaker.runAndWait()

                    
def hello():
    giveOutput('Hello there I am joe. I am here to assist you. Please tell me how can I help you')
def feedback() :
    giveOutput('What feedback do you want to provide?')
    done = False
    while not done :
        try :
            with sr.Microphone() as mic :
                print('speak')
                note = takeInput()
                print(note)

                giveOutput('Choose a filename')
                print('speak')
                filename = takeInput()
                print(filename)
            with open(filename, 'w' ) as f :
                f.write(note)
                done = True
                giveOutput(f'I have created a file named {filename} and recorded your feedback in textual form. Thankyou for your precious time.')
        except sr.UnknownValueError :
            recognizer = sr.Recognizer()
            speaker.say('I did not get that, Please repeat')
            speaker.runAndWait()
def thank():
    print('thankyou')
    giveOutput('Thankyou.')
    
    quit()
            
mappings = {'greetings' : hello,
            'admission' : admission,
            'feedback' : feedback,
            'thank' : thank

            }

assistant = GenericAssistant('audio.json', intent_methods = mappings)
assistant.train_model()
def sound():
    done = False
    while not done :
        try:
            with sr.Microphone() as mic :
                print('speak')
                recognizer = sr.Recognizer()
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                message = recognizer.recognize_google(audio)
                message = message.lower()
                print(message)
                assistant.request(message)
            
        except sr.UnknownValueError :
            recognizer = sr.Recognizer()
            speaker.say('I did not get that')
            speaker.runAndWait()
if __name__ == '__takeInput__':
    takeInput()
if __name__ == '__giveOutput__':
    giveOutput()
if __name__ == '__admission__':
    admission()
if __name__ == '__hello__':
    hello()
if __name__ == '__feedback__':
    feedback()
if __name__ == '__thank__':
    thank()