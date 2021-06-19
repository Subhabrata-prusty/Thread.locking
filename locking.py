import threading
import time
class sub(threading.Thread):
    def __init__(self,name,time):
        threading.Thread.__init__(self)
        self.name=name
        self.time=time
    def run(self):
        t.acquire()
        for i in range(self.time):
            time.sleep(2)
            print(self.name)
        t.release()




t1=sub("T1",4)
t2=sub("T2",6)
t=threading.Lock()
t1.start()
t2.start()