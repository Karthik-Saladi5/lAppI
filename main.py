import os
import eel

from engine.features import *
from engine.command import *

cache="engine/__pycache__"
if os.path.exists(cache) and os.path.isdir(cache):
    import shutil
    shutil.rmtree(cache)

eel.init("www")

playAssistantSound()

os.system('start msedge.exe -app="http://localhost:8000/index.html"')

eel.start('index.html',mode=None, host='localhost', block=True)