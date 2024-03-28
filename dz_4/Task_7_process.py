import multiprocessing
from random import randint


max_array_value = 1000_000
maximum_value = 100 
arr = [randint(1, maximum_value) for _ in range(max_array_value)]
counter = multiprocessing.Value('l',0)
size_threading = 4



def get_array(cnt):
    for i in range(max_array_value):
        with cnt.get_lock():
            cnt.value += arr[i]
    print(f"{cnt.value:_}")

def get_result():
    processes = []
    for i in range (size_threading):
        p = multiprocessing.Process(target=get_array, args=(counter, ))
        processes.append(p)
        p.start()
        
        for p in processes:
            p.join()
    return counter


if __name__ == '__main__':
    print(f"""===========
{get_result()}""")