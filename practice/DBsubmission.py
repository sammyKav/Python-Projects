
import sqlite3

conn = sqlite3.connect('DBAssignment.db') #creates a connection with dB in sqlite. creates dB if it DNE. 

with conn:  
    cur = conn.cursor() # create cursor to execute SQL commands 
    cur.execute("create table if not exists tbl_TXT(\
                id integer primary key autoincrement,\
                file_name text)")
    conn.commit()
conn = sqlite3.connect('DBAssignment.db')

#tuple
fileList = ( 'information.docx','Hello.txt','myImage.png',\
          'myMovie.mp3','World.txt','data.pdf','myPhoto.jpg')


#loop through the tuple to find filex that endswith('txt')

for file in fileList:
    if file.endswith('txt'):
        with conn:
            cur = conn.cursor()
            #adds values if txt file
            cur.execute("INSERT INTO tbl_TXT (file_name) VALUES (?)",(file,))
            print(file)
conn.close()
        
