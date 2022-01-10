import pyttsx3                        
import speech_recognition as sr         
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 

# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak('Good Morning!')
    elif (hour >= 12 and hour < 18):
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('I am Jarvis Sir, I am working for Waqar bhai. Please tell me how may I help you')


def takeCommand():
    # It takes microphone input from the user and returns string output, microphone input requires PyAudio
    # pip install pyaudio

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1  # Means it can have a 1 second gap while speaking
        r.energy_threshold = 300  # minimum audio energy to consider for recording
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)                               #instance of AudioData

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-US')
            print(f'User Said: {query}\n')
        except Exception as e:
            print(e)
            print('Say that again please...')
            query = takeCommand().lower()
            return query;
        return query;

	
if __name__ =='__main__':
	wishMe()
	while True:
	query= takeCommand().lower()
	
	if 'your name' in query:
		speak("I am Jarvis')
	elif 'who are you' in query:
		speak("I am Jarvis working for Maansi')
	elif 'wikipidea' in query:
		speak('Searching Wikipedia')
		query = query.replace('wikipedia', '')
		results =wikipedia.summary(query, sentences=2)
		speak('Acoording to wikipedia')
		print(results)
		speak(results)
	elif 'open google' in query:
		webbrowser.open('googgle.com')
	elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'Sir the time is {strTime}')
    elif 'open code' in query:
        codePath = " code path "  //codepath
        os.startfile(codePath)
    elif 'open song' in query :
        music_dir ="
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[random.randrange(0,3)]))
        
    elif 'add' in query:
        speak('Enter first no:')
        num1 = float(input("enter first number"))
        speak('Enter Second no:')
        num2 = float(input("Enter second number"))
        print(f'Sum={num1+num2}')
        speak(f'The addition of {num} and {num2} is {num1+num2}'
    
