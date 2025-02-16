import json

# Load contacts from the JSON file
with open("data/contacts.json", "r") as file:
    contacts = json.load(file)

# Sort contacts by last_name, then first_name
sorted_contacts = sorted(contacts, key=lambda x: (x["last_name"], x["first_name"]))

# Write sorted contacts to a new file
with open("data/contacts-sorted.json", "w") as file:
    json.dump(sorted_contacts, file, indent=4)

print("Contacts sorted and saved to data/contacts-sorted.json")
