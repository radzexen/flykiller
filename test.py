import random
import time

start_time = time.time()
duration = 30

score = 0

while time.time() - start_time < duration:
    result = random.choice([True, False])
    print(result)
    if result == 1:
        score +=1
    time.sleep(1)

print(f"Score: {score}")






