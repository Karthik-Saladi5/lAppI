import os
import eel
import atexit
def del_cache():
    cache="engine/__pycache__"
    if os.path.exists(cache) and os.path.isdir(cache):
        import shutil
        shutil.rmtree(cache)

atexit.register(del_cache)

from engine.features import *
from engine.command import *


eel.init("www")

playAssistantSound()

os.system('start msedge.exe -app="http://localhost:8000/index.html"')

eel.start('index.html',mode=None, host='localhost', block=True)