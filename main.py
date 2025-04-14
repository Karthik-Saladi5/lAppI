import os
import threading
import eel

from engine.features import *
from engine.command import *

def start():

    eel.init("www")

    playAssistantSound()

    os.system('start msedge.exe -app="http://localhost:8000/index.html"')

    greet_thread = threading.Thread(target=greet)
    greet_thread.start()

    eel.start('index.html',mode=None, host='localhost', block=True)