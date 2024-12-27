#backend
import sqlite3

def MovieData():
    con=sqlite3.connect("movie1.db") 
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Movie_ID text,Movie_Name text,Release_Date text,Director text,Cast text,Budget text,Duration text,Rating text")
    con.commit()
    con.close()

def AddMovieRec(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating):
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?,?,?,?,?)", (Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    con.commit()
    con.close()
def initialize_db():
    with sqlite3.connect("movie1.db") as con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS book (
                id INTEGER PRIMARY KEY, 
                Movie_ID TEXT,
                Movie_Name TEXT,
                Release_Date TEXT,
                Director TEXT,
                Cast TEXT,
                Budget TEXT,
                Duration TEXT,
                Rating TEXT
            )
        """)

def add_movie(Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating):
    with sqlite3.connect("movie1.db") as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO book (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))

def ViewMovieData():
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()    
    return rows
def view_movies():
    with sqlite3.connect("movie1.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM book")
        return cur.fetchall()

def DeleteMovieRec(id):    
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()  
def delete_movie(movie_id):
    with sqlite3.connect("movie1.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (movie_id,))

def SearchMovieData(Movie_ID="",Movie_Name="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):  
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("SELECT * FROM book WHERE Movie_ID=? OR Movie_Name=? OR Release_Date=? OR Director=? OR Cast=? OR Budget=? OR Duration=? OR Rating=?",(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    rows=cur.fetchall()
    con.close()    
    return rows
def search_movies(Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="", Rating=""):
    query = "SELECT * FROM book WHERE 1=1"
    params = []

    if Movie_ID:
        query += " AND Movie_ID=?"
        params.append(Movie_ID)
    if Movie_Name:
        query += " AND Movie_Name=?"
        params.append(Movie_Name)
    if Release_Date:
        query += " AND Release_Date=?"
        params.append(Release_Date)
    if Director:
        query += " AND Director=?"
        params.append(Director)
    if Cast:
        query += " AND Cast=?"
        params.append(Cast)
    if Budget:
        query += " AND Budget=?"
        params.append(Budget)
    if Duration:
        query += " AND Duration=?"
        params.append(Duration)
    if Rating:
        query += " AND Rating=?"
        params.append(Rating)

    with sqlite3.connect("movie1.db") as con:
        cur = con.cursor()
        cur.execute(query, params)
        return cur.fetchall()

def UpdateMovieData(id,Movie_ID="",Movie_Name="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("UPDATE book SET Movie_ID=?,Movie_Name=?,Release_Date=?,Director=?,Cast=?,Budget=?,Duration=?,Rating=?, WHERE id=?",(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    con.commit()
    con.close()
def update_movie(movie_id, Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="", Rating=""):
    with sqlite3.connect("movie1.db") as con:
        cur = con.cursor()
        cur.execute("""
            UPDATE book 
            SET Movie_ID=?, Movie_Name=?, Release_Date=?, Director=?, Cast=?, Budget=?, Duration=?, Rating=?
            WHERE id=?
        """, (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating, movie_id))

# Initialize the database on first run
initialize_db()