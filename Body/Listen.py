# Hindi or English - Command
# English

# Step - 1
# pip install googletrans==3.1.0a0

# Step - 2
# Three Functions
# 1 - Listen Function 
# 2 - English Translation
# 3 - Connect

import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans==3.1.0a0
from numba import njit

njit()
# 1 - Listen : Hindi or English

njit()
def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")

    except:
        return ""
    
    query = str(query).lower()
    return query

# 2 - Translation
njit()
def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}.")
    return data

# 3 - Connect
njit()
def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data
