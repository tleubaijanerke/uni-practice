import json
import csv
from connect import get_connection

# --------------------------
# ADD CONTACT
# --------------------------
def add_contact():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group = input("Group: ")

    cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
    res = cur.fetchone()

    if res:
        group_id = res[0]
    else:
        cur.execute("INSERT INTO groups(name) VALUES (%s) RETURNING id", (group,))
        group_id = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (name, email, birthday, group_id))

    conn.commit()
    cur.close()
    conn.close()

# --------------------------
# ADD PHONE (uses procedure)
# --------------------------
def add_phone():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Contact name: ")
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ")

    cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))

    conn.commit()
    cur.close()
    conn.close()

# --------------------------
# SEARCH
# --------------------------
def search():
    conn = get_connection()
    cur = conn.cursor()

    q = input("Search: ")

    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

# --------------------------
# FILTER BY GROUP
# --------------------------
def filter_by_group():
    conn = get_connection()
    cur = conn.cursor()

    group = input("Group: ")

    cur.execute("""
        SELECT c.name, c.email
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (group,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

# --------------------------
# SORT
# --------------------------
def sort_contacts():
    conn = get_connection()
    cur = conn.cursor()

    field = input("Sort by (name/birthday/created_at): ")

    cur.execute(f"SELECT name, email FROM contacts ORDER BY {field}")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

# --------------------------
# PAGINATION
# --------------------------
def paginate():
    conn = get_connection()
    cur = conn.cursor()

    limit = 3
    page = 0

    while True:
        offset = page * limit

        cur.execute("""
            SELECT name, email
            FROM contacts
            ORDER BY id
            LIMIT %s OFFSET %s
        """, (limit, offset))

        rows = cur.fetchall()

        if not rows:
            print("No more data")
            break

        print(f"\n--- PAGE {page + 1} ---")
        for r in rows:
            print(r)

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            page += 1
        elif cmd == "prev" and page > 0:
            page -= 1
        else:
            break

    cur.close()
    conn.close()

# --------------------------
# EXPORT JSON
# --------------------------
def export_json():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    """)

    data = cur.fetchall()

    with open("contacts.json", "w") as f:
        json.dump(data, f, default=str)

    print("Exported!")

    cur.close()
    conn.close()

# --------------------------
# IMPORT JSON
# --------------------------
def import_json():
    conn = get_connection()
    cur = conn.cursor()

    with open("contacts.json") as f:
        data = json.load(f)

    for item in data:
        name = item[0]

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists. skip/overwrite: ")

            if choice == "skip":
                continue
            else:
                cur.execute("DELETE FROM contacts WHERE name=%s", (name,))

        cur.execute("INSERT INTO contacts(name) VALUES (%s)", (name,))

    conn.commit()
    cur.close()
    conn.close()

# --------------------------
# CSV IMPORT
# --------------------------
def import_csv():
    print("IMPORT CSV STARTED")
    conn = get_connection()
    cur = conn.cursor()

    with open("/Users/zhanerketleubay/TSIS/TSIS1/contacts.csv") as f:
        reader = csv.DictReader(f)

        for row in reader:
            name = row["name"]
            email = row["email"]
            birthday = row["birthday"]
            group = row["group"]
            phone = row["phone"]
            ptype = row["type"]

            # group
            cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
            res = cur.fetchone()

            if res:
                gid = res[0]
            else:
                cur.execute("INSERT INTO groups(name) VALUES (%s) RETURNING id", (group,))
                gid = cur.fetchone()[0]

            # contact
            cur.execute("""
                INSERT INTO contacts(name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (name) DO NOTHING
            """, (name, email, birthday, gid))

            # phone
            cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))

    conn.commit()
    cur.close()
    conn.close()

# --------------------------
# MENU
# --------------------------
def menu():
    while True:
        print("""
1 Add contact
2 Add phone
3 Search
4 Filter by group
5 Sort
6 Pagination
7 Export JSON
8 Import JSON
9 Import CSV
0 Exit
""")

        choice = input("Choose: ")

        if choice == "1": add_contact()
        elif choice == "2": add_phone()
        elif choice == "3": search()
        elif choice == "4": filter_by_group()
        elif choice == "5": sort_contacts()
        elif choice == "6": paginate()
        elif choice == "7": export_json()
        elif choice == "8": import_json()
        elif choice == "9": import_csv()
        else: break


if __name__ == "__main__":
    menu()
