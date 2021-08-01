import p


def
r.pause_threshhold = 1
r.energy_threshhold = 300
r.adjust_for_ambient_noise(source, duration=1)
try:
	print('Recognizing..')
	query = r.recognize_google(audio, language='en-us')
	print(f'
	
	
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
    