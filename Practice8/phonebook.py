from connect import connect

conn = connect()
cur = conn.cursor()

print("1 - Search")
print("2 - Add/Update contact")
print("3 - Delete contact")
print("4 - Show contacts (pagination)")

choice = input("Choose option: ")

# SEARCH (function)
if choice == "1":
    pattern = input("Enter search pattern: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# UPSERT (procedure)
elif choice == "2":
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    print("Done")

# DELETE (procedure)
elif choice == "3":
    value = input("Enter name or phone: ")
    cur.execute("CALL delete_contact(%s)", (value,))
    print("Deleted")

# PAGINATION (function)
elif choice == "4":
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur.execute("SELECT * FROM get_contacts(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

else:
    print("Invalid choice")

cur.close()
conn.close()