import threading
from random import randint


max_array_value = 1000_000
maximum_value = 100 
arr = [randint(1, maximum_value) for _ in range(max_array_value)]
counter = 0
size_threading = 4
threads = []
num = 1

def get_array():
    global counter
    global num
    for i in range(max_array_value):
        counter += arr[i]
    print(f"Процесс {num}: {counter:_}")
    num += 1

def get_result():
    for i in range (size_threading):
        thread = threading.Thread(target=get_array)
        threads.append(thread)
        thread.start()
        
        for thread in threads:
            thread.join()
    return counter


if __name__ == '__main__':
    print(f"""======================
Итог: {get_result()}""")