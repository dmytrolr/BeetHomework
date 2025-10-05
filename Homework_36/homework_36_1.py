import asyncio
import time
import math
from multiprocessing import Pool

async def async_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return await async_fibonacci(n - 1) + await async_fibonacci(n - 2)

async def async_factorial(n: int) -> int:
    return math.factorial(n)

async def async_square(n: int) -> int:
    return n * n

async def async_cube(n: int) -> int:
    return n ** 3

async def run_async(numbers):
    start = time.time()
    fibs = await asyncio.gather(*(async_fibonacci(n) for n in numbers))
    facts = await asyncio.gather(*(async_factorial(n) for n in numbers))
    squares = await asyncio.gather(*(async_square(n) for n in numbers))
    cubes = await asyncio.gather(*(async_cube(n) for n in numbers))
    end = time.time()

    print("\n--- Результати Asyncio ---")
    print("Fibonacci:", fibs)
    print("Factorials:", facts)
    print("Squares:", squares)
    print("Cubes:", cubes)
    print("Час виконання (asyncio):", round(end - start, 4), "секунд")

    return end - start

def sync_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return sync_fibonacci(n - 1) + sync_fibonacci(n - 2)

def sync_factorial(n: int) -> int:
    return math.factorial(n)

def sync_square(n: int) -> int:
    return n * n

def sync_cube(n: int) -> int:
    return n ** 3

def run_multiprocessing(numbers):
    start = time.time()
    with Pool() as pool:
        fibs = pool.map(sync_fibonacci, numbers)
        facts = pool.map(sync_factorial, numbers)
        squares = pool.map(sync_square, numbers)
        cubes = pool.map(sync_cube, numbers)
    end = time.time()

    print("\n--- Результати Multiprocessing ---")
    print("Fibonacci:", fibs)
    print("Factorials:", facts)
    print("Squares:", squares)
    print("Cubes:", cubes)
    print("Час виконання (multiprocessing):", round(end - start, 4), "секунд")

    return end - start


def main():
    numbers = list(range(1, 11))


    async_time = asyncio.run(run_async(numbers))
    mp_time = run_multiprocessing(numbers)

    # Порівняння
    print("\n=== Порівняння ===")
    if async_time < mp_time:
        print("Асинхронний підхід швидший у цьому випадку.")
    else:
        print("Multiprocessing швидший у цьому випадку.")

if __name__ == "__main__":
    main()
