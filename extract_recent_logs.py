import os
import glob

# Define paths
log_dir = "data/logs/"
output_file = "data/logs-recent.txt"

# Get a list of .log files sorted by modification time (newest first)
log_files = sorted(glob.glob(os.path.join(log_dir, "*.log")), key=os.path.getmtime, reverse=True)

# Take the 10 most recent log files
recent_logs = log_files[:10]

# Read the first line of each file
first_lines = []
for log_file in recent_logs:
    with open(log_file, "r", encoding="utf-8") as file:
        first_line = file.readline().strip()
        first_lines.append(first_line)

# Write output to logs-recent.txt
with open(output_file, "w", encoding="utf-8") as out_file:
    out_file.write("\n".join(first_lines) + "\n")

print("Logs extracted successfully to", output_file)
