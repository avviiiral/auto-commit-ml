import datetime
import random
import time

# Random delay (10–120 seconds)
delay = random.randint(10, 120)
time.sleep(delay)

# Simulated ML metrics
accuracy = round(random.uniform(0.82, 0.99), 4)
precision = round(random.uniform(0.80, 0.98), 4)
recall = round(random.uniform(0.78, 0.97), 4)
loss = round(random.uniform(0.01, 0.25), 4)

now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

log = (
    f"{now} | "
    f"accuracy={accuracy} | "
    f"precision={precision} | "
    f"recall={recall} | "
    f"loss={loss}\n"
)

with open("training_log.txt", "a") as f:
    f.write(log)

print(f"Logged ML metrics after {delay}s delay")
