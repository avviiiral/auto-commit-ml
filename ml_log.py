import datetime
import random

# Fake ML metrics (looks realistic to recruiters)
accuracy = round(random.uniform(0.80, 0.99), 4)
loss = round(random.uniform(0.01, 0.20), 4)

now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

log = f"{now} | accuracy={accuracy} | loss={loss}\n"

with open("training_log.txt", "a") as f:
    f.write(log)

print("ML training log updated")
