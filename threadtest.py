import threading
import time
import random

class TestThread(threading.Thread):
    def run(self):
        while True:
            print('[{0}] Thread{1:3d}'.format(self.getName(),random.randrange(1,999) ))
            time.sleep(1)

th = []
for i in range(3):
    th.append(TestThread())

for i in th:
    i.start()

for i in th:
    i.join()

if __name__ == "__main__":
    pass