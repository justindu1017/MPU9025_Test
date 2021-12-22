import threading
import recorder
import _9025



if __name__ == "__main__":
    t = threading.Thread(target=_9025.start)
    t2 = threading.Thread(target=recorder.main, args=(t, ))
    t.start()
    t2.start()