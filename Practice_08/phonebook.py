from connect import get_connection


def setup_database():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                surname VARCHAR(50) NOT NULL,
                phone VARCHAR(20) UNIQUE NOT NULL,
                CONSTRAINT unique_name_surname UNIQUE (name, surname)
            );
        """)

        try:
            with open("functions.sql", "r", encoding="utf-8") as f:
                functions_sql = f.read()
            print("functions.sql read successfully")
        except Exception as e:
            print("Error reading functions.sql:", e)
            return

        try:
            with open("procedures.sql", "r", encoding="utf-8") as f:
                procedures_sql = f.read()
            print("procedures.sql read successfully")
        except Exception as e:
            print("Error reading procedures.sql:", e)
            return

        cur.execute(functions_sql)
        cur.execute(procedures_sql)

        conn.commit()
        print("Database objects created successfully.")

    except Exception as e:
        print("Setup error:", e)

    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


def insert_or_update_contact():
    name = input("Enter name: ").strip()
    surname = input("Enter surname: ").strip()
    phone = input("Enter phone: ").strip()

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("CALL upsert_contact(%s, %s, %s);", (name, surname, phone))
        conn.commit()

        print("Contact inserted/updated successfully.")

    except Exception as e:
        print("Insert/update error:", e)

    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


def search_contacts():
    pattern = input("Enter search pattern: ").strip()

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
        rows = cur.fetchall()

        if rows:
            print("\nFound contacts:")
            for row in rows:
                print(row)
        else:
            print("No contacts found.")

    except Exception as e:
        print("Search error:", e)

    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


def insert_many_contacts():
    try:
        count = int(input("How many contacts do you want to add? ").strip())
        if count <= 0:
            print("Count must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    names = []
    surnames = []
    phones = []

    for i in range(count):
        print(f"\nContact {i + 1}")
        names.append(input("Name: ").strip())
        surnames.append(input("Surname: ").strip())
        phones.append(input("Phone: ").strip())

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "CALL insert_many_contacts(%s, %s, %s);",
            (names, surnames, phones)
        )

        cur.execute("SELECT * FROM incorrect_data;")
        incorrect_rows = cur.fetchall()

        conn.commit()

        if incorrect_rows:
            print("\nIncorrect data:")
            for row in incorrect_rows:
                print(row)
        else:
            print("\nAll contacts inserted successfully.")

    except Exception as e:
        print("Bulk insert error:", e)

    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


def show_paginated_contacts():
    try:
        limit_value = int(input("Enter limit: ").strip())
        offset_value = int(input("Enter offset: ").strip())

        if limit_value <= 0 or offset_value < 0:
            print("Limit must be greater than 0 and offset must be 0 or greater.")
            return

    except ValueError:
        print("Please enter valid integer values.")
        return

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM get_contacts_paginated(%s, %s);",
            (limit_value, offset_value)
        )
        rows = cur.fetchall()

        if rows:
            print("\nPaginated contacts:")
            for row in rows:
                print(row)
        else:
            print("No contacts found.")

    except Exception as e:
        print("Pagination error:", e)

    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


def delete_contact():
    value = input("Enter username, surname, full name, or phone to delete: ").strip()

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("CALL delete_contact(%s);", (value,))
        conn.commit()

        print("Delete request completed.")

    except Exception as e:
        print("Delete error:", e)

    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


def show_all_contacts():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM contacts ORDER BY id;")
        rows = cur.fetchall()

        if rows:
            print("\nAll contacts:")
            for row in rows:
                print(row)
        else:
            print("PhoneBook is empty.")

    except Exception as e:
        print("Display error:", e)

    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


def main():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Setup database objects")
        print("2. Insert or update one contact")
        print("3. Search contacts by pattern")
        print("4. Insert many contacts")
        print("5. Show contacts with pagination")
        print("6. Delete contact")
        print("7. Show all contacts")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            setup_database()
        elif choice == "2":
            insert_or_update_contact()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            insert_many_contacts()
        elif choice == "5":
            show_paginated_contacts()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            show_all_contacts()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()