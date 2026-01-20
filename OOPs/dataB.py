import sqlite3
 
# Connect to a database (or create it if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
 
# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')
print("Table 'users' created (or already exists).")
 
# Insert data
cursor.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ("XYZ", 30))
print("Inserted a user: XYZ, 30")
 
# Commit changes
conn.commit()
 
# Query the table to see the result
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Current users in the database:")
for row in rows:
    print(row)
 
# Close connection
conn.close()