from connect import connect
import csv

# connect to database
conn = connect()
cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(20)
)
""")
conn.commit()

# insert from CSV
with open('contacts.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cur.execute(
            "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
            (row['name'], row['phone'])
        )
conn.commit()

# insert from console
name = input("Enter name: ")
phone = input("Enter phone: ")

cur.execute(
    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
    (name, phone)
)
conn.commit()

# select all
cur.execute("SELECT * FROM phonebook")
print("Contacts:")
for row in cur.fetchall():
    print(row)

# update example
cur.execute(
    "UPDATE phonebook SET phone=%s WHERE name=%s",
    ("111222333", "Alice")
)
conn.commit()

# delete example
cur.execute(
    "DELETE FROM phonebook WHERE name=%s",
    ("Bob",)
)
conn.commit()

# close
cur.close()
conn.close()

