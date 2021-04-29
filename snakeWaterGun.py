import pyttsx3
import speech_recognition as sr
import random


def speak_male(audio):
    male = pyttsx3.init('sapi5')
    male_voice = male.getProperty('voices')
    male.setProperty('voice', male_voice[0].id)
    male.say(audio)
    male.runAndWait()
def speak_female(audio):
    female = pyttsx3.init('sapi5')
    female_voice = female.getProperty('voices')
    female.setProperty('voice', female_voice[1].id)
    female.say(audio)
    female.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak_female('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        speak_female('Recognising..')
        query = r.recognize_google(audio, language='en-in').lower()
        print(f"User said {query}")
    except Exception as e:
        print(e)
        speak_female("Sorry I couldn't hear you properly")
        return "None"
    return query


total = 0
user_score = 0
comp_score = 0
gameList = ['snake', 'water', 'gun']
speak_female("Welcome to Snake, Water, Gun Game!!")
speak_female("Tell Your Name..")
user_name = takeCommand()
print(user_name)
if user_name == "None":
    user_name = 'User'
speak_female(f"Hello {user_name} let's start the game")
while total < 5:
    speak_female("Choose from snake, water, gun")
    userInput = takeCommand().lower()
    if userInput == "none":
        total = total
    else:
        randomChoice = random.choice(gameList)

        if userInput == 'water' and randomChoice == 'gun' or userInput == 'snake' and randomChoice == 'water' or userInput == 'gun' and randomChoice == 'snake':
            speak_male(randomChoice)
            speak_female(f"{user_name} Won")
            user_score += 1
        elif userInput == 'gun' and randomChoice == 'water' or userInput == 'water' and randomChoice == 'snake' or userInput == 'snake' and randomChoice == 'gun':
            speak_male(randomChoice)
            speak_female("Computer Won")
            comp_score += 1
        elif userInput == randomChoice:
            speak_male(randomChoice)
            speak_female("Match Draw")
        else:
            speak_female("Please say that again")
            total -= 1
        total += 1


speak_female(f"{user_name} Score: {user_score}")
speak_female(f"Computer Score: {comp_score}")
if user_score > comp_score:
    speak_female(f"Congratulation {user_name}")
else:
    speak_female("Computer Won")

