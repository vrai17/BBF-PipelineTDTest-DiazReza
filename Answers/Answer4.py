import os
import xml.etree.ElementTree as ET
import sqlite3

xml_file = 'animations.xml'
db_name = 'animations.db'

def parse_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    animations = []

    for animation in root.findall('animation'):
        name = animation.find('name').text
        total_episodes = int(animation.find('total_episodes').text)
        average_duration = int(animation.find('average_duration').text)
        director = animation.find('director').text
        characters = ', '.join([char.text for char in animation.find('characters').findall('character')])
        
        animations.append((name, total_episodes, average_duration, director, characters))

    return animations

def create_database(db_name):
    # Check if the database file already exists
    db_exists = os.path.exists(db_name)
    
    if db_exists:
        print(f"Modifying existing database file '{db_name}'. . .")
    else:
        print(f"Creating new database file '{db_name}'. . .")
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS animations (
        id INTEGER PRIMARY KEY,
        name TEXT,
        total_episodes INTEGER,
        average_duration INTEGER,
        director TEXT,
        characters TEXT
    )
    ''')

    conn.commit()
    
    return conn

def clear_data(conn):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM animations')
    conn.commit()
    print("Cleared existing data from the animations table")

def insert_data(conn, animations):
    cursor = conn.cursor()

    cursor.executemany('''
    INSERT INTO animations (name, total_episodes, average_duration, director, characters)
    VALUES (?, ?, ?, ?, ?)
    ''', animations)

    conn.commit()
    print(f"Inserted {len(animations)} animations data into the database")

def print_database(conn):
    #conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Select all data from animations table
    cursor.execute('SELECT * FROM animations')
    animations = cursor.fetchall()

    # Print all animations
    print("\nanimations.db data:")
    for animation in animations:
        print(animation)

def main():
    animations = parse_xml(xml_file)
    conn = create_database(db_name)
    clear_data(conn)
    insert_data(conn, animations)

    db_exported = os.path.exists(db_name)
    if db_exported:
        print(f"'{db_name}' successfully updated.")
        print_database(conn)
    else:
        print(f"Failed to process the database.")

    conn.close()
    print("\nDatabase connection closed")

if __name__ == '__main__':
    main()
