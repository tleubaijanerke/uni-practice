import re
import json

# Read the receipt file
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# convert money string to float (e.g., "1 200,00" -> 1200.00)
def money_to_float(s: str) -> float:
    return float(s.replace(" ", "").replace(",", "."))

# 1) Extract all prices using regex pattern for Kazakhstani format
money_pattern = r"\d{1,3}(?: \d{3})*,\d{2}"
all_prices = re.findall(money_pattern, text)

# 2-3) Extract items with named groups: name, quantity, unit price, line total
item_pattern = (
    r"(?ms)^\d+\.\s*\n"                       # item number + newline
    r"(?P<name>.+?)\n"                         # product name (lazy)
    r"(?P<qty>\d+,\d{3})\s*x\s*"                # quantity (e.g., 2,000 x)
    r"(?P<unit>\d{1,3}(?: \d{3})*,\d{2})\n"     # unit price
    r"(?P<line>\d{1,3}(?: \d{3})*,\d{2})"       # line total
)

items = []
for m in re.finditer(item_pattern, text):
    d = m.groupdict()
    items.append({
        "name": d["name"].strip(),
        "qty": float(d["qty"].replace(",", ".")),         
        "unit_price": money_to_float(d["unit"]),
        "line_total": money_to_float(d["line"]),
    })

# List of just product names
product_names = [it["name"] for it in items]

# 4) Extract total amount after "ИТОГО:"
total_m = re.search(r"(?m)^ИТОГО:\s*\n(?P<total>\d{1,3}(?: \d{3})*,\d{2})$", text)
total = money_to_float(total_m.group("total")) if total_m else None

# 5) Extract date and time
dt_m = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", text)
datetime = {"date": dt_m.group(1), "time": dt_m.group(2)} if dt_m else None

# 6) Extract payment method
pay_m = re.search(r"(?m)^(Банковская карта|Наличные|Карта):", text, flags=re.IGNORECASE)
payment_method = pay_m.group(1) if pay_m else None

# Optional verification: sum line totals and compare with total
calc_sum = round(sum(it["line_total"] for it in items), 2)

# Compile all extracted data into final dictionary
result = {
    "product_names": product_names,
    "items": items,
    "all_prices_raw": all_prices,
    "total": total,
    "total_calculated_from_items": calc_sum,
    "datetime": datetime,
    "payment_method": payment_method,
}

# Output as formatted JSON
print(json.dumps(result, ensure_ascii=False, indent=2))
