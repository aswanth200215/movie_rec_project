import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='movies',
                                         user='root',
                                         password='12345')
except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)

cursor = connection.cursor(buffered=True)


class searchmovie:
    def search(self, keyword, cursor):
        intornot = (str(keyword).isdigit())
        results = []
        if not intornot:
            cursor.execute("select * from movie where title LIKE '%{}%' ".format(keyword))
            a = cursor.fetchall()
            if len(a) != 0:
                results.append((len(a), a))
            cursor.execute("select * FROM movie WHERE actorname LIKE '%{}%' ".format(keyword))
            b = cursor.fetchall()
            if len(b) != 0:
                results.append((len(b), b))
            cursor.execute("select * FROM movie WHERE actor2name LIKE '%{}%'  ".format(keyword))
            c = cursor.fetchall()
            if len(c) != 0:
                results.append((len(c), c))
            cursor.execute("select * FROM movie WHERE director_name LIKE '%{}%' ".format(keyword))
            d = cursor.fetchall()
            if len(d) != 0:
                results.append((len(d), d))
            cursor.execute("select * FROM movie WHERE genres LIKE '%{}%' ".format(keyword))
            f = cursor.fetchall()
            if len(f) != 0:
                results.append((len(f), f))
            cursor.execute("select * FROM movie WHERE keyword LIKE '%{}%' ".format(keyword))
            g = cursor.fetchall()
            if len(g) != 0:
                results.append((len(g), g))
            total_count = sum(count for count, _ in results)
            return total_count, results
        else:
            if intornot:
                cursor.execute("select * FROM movie WHERE year LIKE '%{}%' ".format(keyword))
                e = cursor.fetchall()
                return len(e), e

obj = searchmovie()
keyword = input("Enter the keyword: ")
count, results = obj.search(keyword, cursor)
print(f"Total count: {count}")
for count, rows in results:
    print(f"Count: {count}")
    for row in rows:
        print(row)
