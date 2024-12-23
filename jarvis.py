'''1) pip install speechrecognition  
   2) pip install pyaudio
   3) pip install setuptools
   4) pip install pyttsx3'''

import speech_recognition as sr  # Speech listining for use
import webbrowser  # open any in webbrowser
import pyttsx3  # give to answer
import music  # extrnal file attech

people_listning=sr.Recognizer()
speak=pyttsx3.init()

def active(name):
     speak.say(name)
     speak.runAndWait()


def speaks():
    print("Active")
    speak.say("Hello how can i help you?")
    speak.runAndWait()

def play():
    song=command1.lower().split(" ")[1]
    link=music.musics[song]
    webbrowser.open(link)

    
if __name__ == "__main__":   # python main file (if this file is import that not run)
    active("Hello Darshan,Good Morning")
    
    while True:
        try:
            with sr.Microphone() as source:
                print("i am listning............")
                audio=people_listning.listen(source)
            command=people_listning.recognize_google(audio)
            print(command)
            print("plese speak hey dp than this is active") 
            if command.lower()=="hey dp":
                print("Active")
                speak.say("Hello how can i help you?")
                speak.runAndWait()
                with sr.Microphone() as source1:
                    print("i am listning1............")
                    audio=people_listning.listen(source1)
                    command1=people_listning.recognize_google(audio)
                    print(command1)
                    if "opening youtube" in command1.lower():
                        webbrowser.open("https://www.youtube.com/")
                        speak.say("Ok")
                        speak.runAndWait()
                    elif "opening google" in command1.lower():
                        webbrowser.open("https://www.google.com/")
                        speak.say("Ok")
                        speak.runAndWait()
                    elif "opening facebook" in command1.lower():
                        webbrowser.open("https://www.facebook.com/")
                        speak.say("Ok")
                        speak.runAndWait()
                    elif "opening instagram" in command1.lower():
                        webbrowser.open("https://www.instagram.com/")
                        speak.say("Ok")
                        speak.runAndWait()
                    elif "close" in command1.lower() or "exit" in command1.lower():
                        speak.say("Ok")
                        speak.runAndWait()
                        break
                    elif command1.lower().startswith("play"):
                        play()
                            
        except Exception as e:
            print(e)
            

    





