import atexit
import multiprocessing
import os

def del_cache():
    cache="engine/__pycache__"
    cache1="__pycache__"
    if os.path.exists(cache) and os.path.isdir(cache):
        import shutil
        shutil.rmtree(cache)
        shutil.rmtree(cache1)

atexit.register(del_cache)

def startLappi():
    print("Process 1 is running")
    from main import start
    start()

def listenHotWord():
    print("Process 2 is running")
    from engine.features import hotWord
    hotWord()

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=startLappi)
    p2=multiprocessing.Process(target=listenHotWord)
    p1.start()
    p2.start()
    p1.join()
    if p2.is_alive():
        p2.terminate()
        p2.join()
    print("system stop")