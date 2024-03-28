import threading
import time

def worker(num):
    print("Начало")
    time.sleep(3)
    print("Конец")
    
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
    
print("Все ок")