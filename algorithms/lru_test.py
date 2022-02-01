import time
import functools
import random

@functools.lru_cache
def slow_square(number):
    print(f"Sleeping {number} seconds.")
    time.sleep(number)
    return number**2


@functools.lru_cache
def fibon_recur(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibon_recur(number - 1) + fibon_recur(number - 2)

@functools.lru_cache
def fibon_loop(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    current = 1
    prev = 1
    for i in range(1, number-1):
        temp = current
        current += prev
        prev = temp
    return current

def lights(light_array):
    if len(light_array) == 0:
        return 0
    current_num = light_array[0]
    count = 1
    for i in light_array[1:]:
        print(current_num, i)
        if current_num > i:
            count += 1
            current_num = i
        else:
            current_num = i
    return count

print(lights([1,3,4,2,5]))
# start = time.time()
# print(fibon_loop(3))
# for i in range(10000000):
#     num = random.randint(1,10)
#     #fibon_loop(num)
#     fibon_recur(num)
#     #pass
# end = time.time()
# print(end-start)
#print(slow_square(3))
#print(slow_square(3))