import datetime
import random
import time
import os

# -----------------------------
# Random delay (simulate real training)
# -----------------------------
delay = random.randint(10, 120)
time.sleep(delay)

# -----------------------------
# Simulated ML metrics
# -----------------------------
metrics = {
    "accuracy": round(random.uniform(0.82, 0.99), 4),
    "precision": round(random.uniform(0.80, 0.98), 4),
    "recall": round(random.uniform(0.78, 0.97), 4),
    "loss": round(random.uniform(0.01, 0.25), 4),
}

# -----------------------------
# Timestamp (UTC – GitHub friendly)
# -----------------------------
timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

# -----------------------------
# Log format
# -----------------------------
log_entry = (
    f"{timestamp} | "
    f"accuracy={metrics['accuracy']} | "
    f"precision={metrics['precision']} | "
    f"recall={metrics['recall']} | "
    f"loss={metrics['loss']}\n"
)

# -----------------------------
# Write to log file (guaranteed change)
# -----------------------------
LOG_FILE = "training_log.txt"

with open(LOG_FILE, "a") as file:
    file.write(log_entry)

# -----------------------------
# Console output (for Actions logs)
# -----------------------------
print("ML training metrics logged successfully")
print(f"Delay simulated : {delay} seconds")
print(f"Metrics         : {metrics}")
print(f"Log file        : {os.path.abspath(LOG_FILE)}")
