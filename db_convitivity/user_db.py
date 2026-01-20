import sqlite3
 
 
def connect_db():

    return sqlite3.connect("users.db")
 
 
# -------- CREATE --------

def add_user(name, email, age):

    try:

        conn = connect_db()

        cursor = conn.cursor()
 
        cursor.execute(

            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",

            (name, email, age)

        )
 
        conn.commit()

        print("✅ User added successfully")
 
    except sqlite3.IntegrityError:

        print("❌ Email already exists")
 
    finally:

        conn.close()
 
 
# -------- READ (ALL) --------

def get_all_users():

    conn = connect_db()

    cursor = conn.cursor()
 
    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()
 
    conn.close()

    return users
 
 
# -------- READ (ONE) --------

def find_user_by_email(email):

    conn = connect_db()

    cursor = conn.cursor()
 
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))

    user = cursor.fetchone()
 
    conn.close()

    return user
 
 
# -------- UPDATE --------

def update_user(email, new_name, new_age):

    conn = connect_db()

    cursor = conn.cursor()
 
    cursor.execute(

        "UPDATE users SET name = ?, age = ? WHERE email = ?",

        (new_name, new_age, email)

    )
 
    conn.commit()
 
    if cursor.rowcount:

        print("✅ User updated successfully")

    else:

        print("❌ User not found")
 
    conn.close()
 
 
# -------- DELETE --------

def delete_user(email):

    conn = connect_db()

    cursor = conn.cursor()
 
    cursor.execute("DELETE FROM users WHERE email = ?", (email,))

    conn.commit()
 
    if cursor.rowcount:

        print("✅ User deleted successfully")

    else:

        print("❌ User not found")
 
    conn.close()

 