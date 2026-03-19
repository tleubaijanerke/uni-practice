import json

# Open and load JSON file
with open("sample-data.json") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU':6}")
print("-" * 80)

# Iterate through JSON data
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]

    dn = attributes["dn"]
    descr = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:50} {descr:20} {speed:8} {mtu:6}")

# This program opens and loads a JSON file using json.load().
# It accesses the imdata list inside the JSON structure.
# Each element contains a dictionary with interface attributes.

# The program extracts:
# dn
# descr
# speed
# mtu

# It prints them in formatted columns using f-strings with alignment.
# Output: formatted table showing interface status.
