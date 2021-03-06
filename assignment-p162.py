

import sqlite3
from os import path

"""
    This script creates a database and adds qualifying
    data from a list of file names into that database. 
"""

fileList = ("information.docx","Hello.txt","myImage.png", \
            "myMovie.mpg","World.txt","data.pdf","myPhoto.jpg")
txtFiles = []
for file in fileList:
    # iterates through fileList, determines which items end
    # with the .txt extention and adds them to a new list.
    root,ext = path.splitext(file)
    if ext == '.txt':
        txtFiles.append(file)

conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_file VARCHAR(50))")
    for file in txtFiles:
        cur.execute("INSERT INTO tbl_files(col_file) VALUES (?)", [file])
    print("The following files were added to the database: \n")
    for row in cur.execute("SELECT col_file FROM tbl_files"):
        msg = "".join(row)
        print(msg)
conn.close()
