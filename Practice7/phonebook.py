from connect import connect
import csv

# Connect to the database
conn = connect()
cur = conn.cursor()

# Create the table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(20)
)
""")
conn.commit()

# ------------------ Functions ------------------

def insert_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("CSV data inserted successfully!")

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Contact added!")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    new_name = input("Enter new name (leave blank to skip): ")
    new_phone = input("Enter new phone (leave blank to skip): ")
    if new_name:
        cur.execute("UPDATE phonebook SET name=%s WHERE name=%s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, name))
    conn.commit()
    print("Contact updated!")

def delete_contact():
    choice = input("Delete by (1) Name or (2) Phone? ")
    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))
    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))
    conn.commit()
    print("Contact deleted!")

def query_contacts():
    choice = input("Search by (1) Name, (2) Phone prefix, (3) All: ")
    if choice == "1":
        name = input("Enter name or part of it: ")
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
    elif choice == "2":
        prefix = input("Enter phone prefix: ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"{prefix}%",))
    else:
        cur.execute("SELECT * FROM phonebook")
    results = cur.fetchall()
    if results:
        for r in results:
            print(r)
    else:
        print("No contacts found.")

# ------------------ Menu ------------------

def menu():
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Query contacts")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            query_contacts()
        elif choice == "6":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()

# Close the connection after exit
cur.close()
conn.close()
