import random
import timeit
import matplotlib.pyplot as plt


def func(arr):
    even = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    odd = [arr[i] for i in range(len(arr)) if i % 2 != 0]
    return even + odd
#O(n)


sizes = [10000, 20000, 30000, 40000, 50000]
times = []
for size in sizes:
    arr = [random.randint(-size, size) for i in range(size)]
    time = timeit.timeit('func(arr)', number=1000, globals=globals())
    times.append(time)
    print(f'Size: {size}, Time: {time}')

plt.plot(sizes, times)

plt.xlabel("Размер входных данных")
plt.ylabel("Время выполнения (с)")
plt.title("График времени выполнения функции")

plt.show()
