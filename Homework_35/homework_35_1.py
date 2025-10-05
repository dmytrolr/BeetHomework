import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

def is_prime(n: int) -> bool:

    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

# --- Threads ---
start = time.time()
with ThreadPoolExecutor() as executor:
    results_threads = list(executor.map(is_prime, NUMBERS))
end = time.time()
print("ThreadPoolExecutor results:")
for n, r in zip(NUMBERS, results_threads):
    print(f"{n}: {r}")
print("Time with threads:", round(end - start, 2), "секунд")

# --- Processes ---
start = time.time()
with ProcessPoolExecutor() as executor:
    results_processes = list(executor.map(is_prime, NUMBERS))
end = time.time()
print("\nProcessPoolExecutor results:")
for n, r in zip(NUMBERS, results_processes):
    print(f"{n}: {r}")
print("Time with processes:", round(end - start, 2), "секунд")


#ThreadPoolExecutor results:
# 2: True
# 1099726899285419: False
# 1570341764013157: True
# 1637027521802551: True
# 1880450821379411: True
# 1893530391196711: True
# 2447109360961063: True
# 3: True
# 2772290760589219: True
# 3033700317376073: True
# 4350190374376723: False
# 4350190491008389: True
# 4350190491008390: False
# 4350222956688319: False
# 2447120421950803: False
# 5: True
# Time with threads: 25.28 секунд
#
# ProcessPoolExecutor results:
# 2: True
# 1099726899285419: False
# 1570341764013157: True
# 1637027521802551: True
# 1880450821379411: True
# 1893530391196711: True
# 2447109360961063: True
# 3: True
# 2772290760589219: True
# 3033700317376073: True
# 4350190374376723: False
# 4350190491008389: True
# 4350190491008390: False
# 4350222956688319: False
# 2447120421950803: False
# 5: True
# Time with processes: 12.06 секунд