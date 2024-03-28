import asyncio
from random import randint


max_array_value = 1000_000
maximum_value = 100 
arr = [randint(1, maximum_value) for _ in range(max_array_value)]
counter = 0
size_threading = 4
num = 1

async def sum_array_async():
    local_sum = 0
    global num
    for i in range(max_array_value):
        local_sum += arr[i]
    print(f"Процесс {num}: {local_sum:_}")
    num += 1
    return local_sum



async def main():
    global counter
    global size_threading
    tasks = []
    for i in range(size_threading):
        task = asyncio.create_task(sum_array_async())
        tasks.append(task)
    for task in tasks:
        counter += await task
    return counter


if __name__ == '__main__':
    asyncio.run(main())
    print(counter)