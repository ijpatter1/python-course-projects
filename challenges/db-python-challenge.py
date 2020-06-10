import sqlite3

def createDB():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS roster
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50),
                    species VARCHAR(50),
                    IQ INTEGER)''')
        data = (('Jean-Baptiste Zorg', 'Human', 122),('Korben Dallas', 'Meat Popsicle', 100),("Ak\'not",'Mangalore', -5))
        c.executemany('INSERT INTO roster (name,species,IQ) VALUES (?,?,?)',data)
        c.execute("UPDATE roster SET species = 'Human' WHERE name = 'Korben Dallas'")
        for row in c.execute("SELECT name, IQ FROM roster WHERE species = 'Human' "):
            print(row)
    conn.close()

if __name__ == "__main__":
    createDB()