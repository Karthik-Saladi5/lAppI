import re
import struct
import time
import webbrowser
from playsound import playsound
import eel
import pvporcupine
import pyaudio
from engine.command import speak
from engine.config import ASSISTANT_NAME
import os
import pywhatkit as kit
import sqlite3

from datetime import datetime

from engine.helper import extract_yt_term

conn= sqlite3.connect("lappy.db")
cursor=conn.cursor()

@eel.expose
def playAssistantSound():
    music_dir="www/assets/audio/start_sound.mp3"
    playsound(music_dir)

def greet():
    current_hour=datetime.now().hour
    if 5<=current_hour<12:
        speak("Good Morning SK")
    elif 12<=current_hour<17:
        speak("Good Afternoon SK")
    elif 17<=current_hour<20:
        speak("Good Evening SK")
    else:
        speak("Welcome back Mr.Egoist")

def openCommand(query):
    query = query.replace(ASSISTANT_NAME,"")
    query=query.replace("open","")
    query.lower()

    app_name= query.strip()
    if app_name!="":
        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)',(app_name,)
            )
            results=cursor.fetchall()
            
            if len(results)!=0:
                speak("Opening "+query)
                os.startfile(results[0][0])
            elif len(results)==0:
                cursor.execute(
                    'SELECT url from web_command WHERE name IN (?)',(app_name,)
                )
                results=cursor.fetchall()

                if len(results)!=0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("something went wrong")

    # if query!="":
    #     speak("Opening "+query)
    #     os.system('start '+query)
    # else:
    #     speak("not found")

def PlayYoutube(query):
    search_term= extract_yt_term(query)
    speak("Playing "+search_term+" on Youtube")
    kit.playonyt(search_term)

def hotWord():
    porcupine=None
    paud=None
    audio_stream=None
    try:
        porcupine=pvporcupine.create(keywords=["computer","jarvis"])
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)

        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            keyword_index=porcupine.process(keyword)

            if keyword_index>=0:
                print("hotword detected")

                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()