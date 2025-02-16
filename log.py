import os
from datetime import datetime, timedelta

# Create logs directory if it doesn't exist
log_dir = "data/logs"
os.makedirs(log_dir, exist_ok=True)

# Generate 10 log files with timestamps
for i in range(10):
    log_filename = os.path.join(log_dir, f"log_{i+1}.log")
    timestamp = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d %H:%M:%S")
    with open(log_filename, "w") as log_file:
        log_file.write(f"Log entry {i+1} - {timestamp}\n")

print(f"10 log files created in {log_dir}")
