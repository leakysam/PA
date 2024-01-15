import speech_recognition as aa
import pyttsx3
import pywhatkit
##to indent use comand and ]


listener = aa.Recognizer()

machine = pyttsx3.init()

def talk(text)
    machine.say(text)
machine.runAndWait()

def input_instruction():
    global instruction

    try:
        with aa.Microphone() as origin:
            print("listening")
            speech= listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "Jarvis" in instruction:
                print(instruction)
            print(instruction)



    except:
        pass   

def play_Jarvis():

    instruction = input_instruction
    print(instruction)
    if "play" in instruction: