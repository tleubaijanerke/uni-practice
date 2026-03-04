import re
import json

with open("raw.txt", "r", encoding="utf-8") as file:
    data = file.read()

# 1. Extract all prices from the receipt
# \d{1,3}        → 1–3 digits
# (?:\s\d{3})*   → optional groups like " 200"
# ,\d{2}         → comma + 2 digits (decimal part)
price_pattern = r"\d{1,3}(?:\s\d{3})*,\d{2}"
prices_raw = re.findall(price_pattern, data)

prices = [float(p.replace(" ", "").replace(",", ".")) for p in prices_raw]


# 2. Find all product names
# \d+\.          → item number like "1."
# \n             → next line
# (.+)           → product name line

product_pattern = r"\d+\.\n(.+)"
products = re.findall(product_pattern, data)


# 3. Calculate total amount
# We take the value after "ИТОГО:"

total_pattern = r"ИТОГО:\n([\d\s]+,\d{2})"
total_match = re.search(total_pattern, data)

if total_match:
    total = float(total_match.group(1).replace(" ", "").replace(",", "."))
else:
    total = sum(prices)  # fallback calculation


# 4. Extract date and time information
# dd.mm.yyyy hh:mm:ss

datetime_pattern = r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}"
datetime_match = re.search(datetime_pattern, data)

datetime_value = datetime_match.group() if datetime_match else None


# 5. Find payment method
# In this receipt it says:
# "Банковская карта:"
payment_pattern = r"Банковская карта|Наличные"
payment_match = re.search(payment_pattern, data)

payment_method = payment_match.group() if payment_match else "Unknown"


# 6. Create structured output
items = []

for i in range(len(products)):
    if i < len(prices):
        items.append({
            "name": products[i],
            "price": prices[i]
        })

receipt_data = {
    "date_time": datetime_value,
    "payment_method": payment_method,
    "items": items,
    "total": total
}

print(json.dumps(receipt_data, indent=4, ensure_ascii=False))