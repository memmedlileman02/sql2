import sqlite3
connection=sqlite3.connect("books")
cursor=connection.cursor()


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS books (ad varchar(50), il int, janr varchar(50) )")
    connection.commit()

def add_table():
    cursor.execute("INSERT INTO books VALUES('cinayet ve ceza',1949,'felsefei psixoloji'),")
    connection.commit()

# ad=input("kitabin adini qeyd edin: ")
# il=int(input("kitabin cixis ilini qeyd edin: "))
# janr=input("kitabin janrini qeyd edin: ")

def dynamic_add_table(ad,il,,janr):
    cursor.execute("INSERT INTO books VALUES(?,?,?,?)",(ad,il,janr))
    connection.commit()

def delete_books(ad):
    cursor.execute("DELETE FROM books WHERE ad=?", (ad,))
    connection.commit()


def show_books_1900():
    cursor.execute("SELECT * FROM books WHERE il >= 1900")
    data = cursor.fetchall()
    for row in data:
        print(row)
        
show_books_1900()
# bookdelete = input("Silmek istediyiniz kitabin adını qeyd edin: ")
# delete_book(bookdelete)
# dynamic_add_table(ad,il,janr)
# create_table()
# add_table()
connection.close()