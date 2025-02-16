import datetime
from dateutil import parser

# Read the dates from the file
with open("data/final_clean_dates.txt", "r") as f:
    dates = f.readlines()

# Normalize and count Wednesdays
wednesday_count = 0
for date in dates:
    date = date.strip()
    try:
        parsed_date = parser.parse(date)  # Auto-detects the format
        if parsed_date.weekday() == 2:  # 2 means Wednesday
            wednesday_count += 1
    except ValueError:
        print(f"Skipping invalid date: {date}")  # Debugging

# Write the count to a file
with open("data/dates-wednesdays.txt", "w") as f:
    f.write(str(wednesday_count))

print(f"Wednesdays counted: {wednesday_count}")
