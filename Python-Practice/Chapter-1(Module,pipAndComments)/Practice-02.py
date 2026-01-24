""" go to the website pypi.org/project/pyttsx3/
    To install this we just write in the terminal 
    pip install pyttsx3
"""
import pyttsx3
engine = pyttsx3.init()
engine.say("prabhjot")
engine.runAndWait()