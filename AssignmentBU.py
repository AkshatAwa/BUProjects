import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567",
    port="3306",
    database="my_songs"
)
class melodyhunt:

    def all_songs(self):
        cn = mydb.cursor()
        cn.execute("select Song_name from songs")
        users = cn.fetchall()
        for a in users:
            print(a)
    def seachsongs(self):
        print(melodyhunt.all_songs(self=1))
        ss = input("Enter the above mentioned song name: ")
        ab = mydb.cursor()
        ab.execute(f"select * from songs where Song_name='{ss}'")
        users2 = ab.fetchall()
        for b in users2:
            print(b)
    def lyrics(self):
        print(melodyhunt.all_songs(self=1))
        l1 = input("Enter the lyrics of the song: ")
        ac = mydb.cursor()
        ac.execute(f"select Song_name,Artist_name from songs where Lyrics='{l1}'")
        users3 = ac.fetchone()
        for j in users3:
            print(j)

melodyhunt.lyrics(self=1)


