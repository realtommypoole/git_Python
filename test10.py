
import sqlite3

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_1(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fName TEXT \
        )")
    conn.commit()
conn.close()


def rdFiles():
    fileList = ('information.docx','Hello.txt','myImage.png', \
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    for items in fileList:
        if items.endswith(".txt"):
            print(items)
            insFiles(items)
            
def insFiles(items): 
    conn = sqlite3.connect('test2.db')

    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_1(col_fName) VALUES (?)",(items,))           
        conn.commit()
    conn.close()




if __name__ == "__main__":
    rdFiles()
