from dateutil import parser

input_file = "data/clean_dates.txt"
output_file = "data/final_clean_dates.txt"

cleaned_dates = []
with open(input_file, "r") as infile:
    for line in infile:
        try:
            parsed_date = parser.parse(line.strip())  # Automatically detects format
            cleaned_dates.append(parsed_date.strftime("%Y-%m-%d"))  # Converts to YYYY-MM-DD
        except ValueError:
            print(f"Skipping invalid date: {line.strip()}")

# Save cleaned dates
with open(output_file, "w") as outfile:
    outfile.write("\n".join(cleaned_dates))

print("Date cleaning complete. Check", output_file)
