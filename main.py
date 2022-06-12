import csv, sqlite3

if __name__ == "__main__":
    con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE polaczenia (from_subscriber data_type INTEGER, 
                    to_subscriber data_type INTEGER, 
                    datetime data_type timestamp, 
                    duration data_type INTEGER , 
                    celltower data_type INTEGER);''')

    with open ("polaczenia.csv", 'r') as a:
        file = csv.reader(a, delimiter=';')
        next(file, None)
        num_rows = [var for var in file]
        cursor.executemany("INSERT INTO polaczenia (from_subscriber, to_subscriber, datetime, duration , celltower) VALUES (?, ?, ?, ?, ?);", num_rows)
        

con
c = con.cursor()
c.execute("SELECT SUM(DURATION) FROM POLACZENIA")
result = c.fetchone()[0]

print(int(result))