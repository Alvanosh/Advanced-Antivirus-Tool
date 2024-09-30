import sqlite3

# Connect to the database (or create it)
def connect_db():
    try:
        return sqlite3.connect('signatures.db')
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Create the signatures table
def create_database():
    conn = connect_db()
    if conn is None:
        return  # Handle connection error

    cursor = conn.cursor()
    
    # Create a table for storing malware signatures
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS signatures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        md5_hash TEXT NOT NULL UNIQUE
    )
    ''')
    
    conn.commit()
    conn.close()

# Add a signature to the database
def add_signature(name, md5_hash):
    conn = connect_db()
    if conn is None:
        return  # Handle connection error

    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO signatures (name, md5_hash) VALUES (?, ?)", (name, md5_hash))
        conn.commit()
        print(f"Signature for {name} added to the database.")
    except sqlite3.IntegrityError:
        print("MD5 hash already exists in the database.")
    except sqlite3.Error as e:
        print(f"Error adding signature: {e}")
    finally:
        conn.close()

# Check if the MD5 hash exists in the database
def check_hash_in_database(file_md5):
    conn = connect_db()
    if conn is None:
        return False  # Handle connection error

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM signatures WHERE md5_hash=?", (file_md5,))
    result = cursor.fetchone()
    
    conn.close()
    return result is not None

# List all signatures in the database
def list_signatures():
    conn = connect_db()
    if conn is None:
        return  # Handle connection error

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM signatures")
    signatures = cursor.fetchall()
    
    conn.close()
    return signatures

# Delete a signature from the database
def delete_signature(md5_hash):
    conn = connect_db()
    if conn is None:
        return  # Handle connection error

    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM signatures WHERE md5_hash=?", (md5_hash,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Deleted signature with MD5 hash: {md5_hash}")
        else:
            print(f"No signature found with MD5 hash: {md5_hash}")
    except sqlite3.Error as e:
        print(f"Error deleting signature: {e}")
    finally:
        conn.close()
