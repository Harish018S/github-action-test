import re

# Read email content
with open("C:/Users/hsent/project_/data/email.txt", "r", encoding="utf-8") as file:
    email_content = file.read().replace("\r", "")

# Extract email using regex
match = re.search(r'From:\s*".+?"\s*<([\w\.-]+@[\w\.-]+\.\w+)>', email_content)

# Write extracted email to file
if match:
    extracted_email = match.group(1)
    with open("C:/Users/hsent/project_/data/email_sender.txt", "w", encoding="utf-8") as output_file:
        output_file.write(extracted_email)
    print("Extracted Email:", extracted_email)
else:
    print("No email found")
