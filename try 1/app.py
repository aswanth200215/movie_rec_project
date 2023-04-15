from flask import Flask,render_template, request

import mysql.connector

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for the search page
@app.route('/search', methods=['POST'])

def search():
    # Get the search keyword from the form data
    keyword = request.form['search']    

    # Connect to the MySQL database
    connection = mysql.connector.connect(host='localhost',
                                         database='movies',
                                         user='root',
                                         password='12345')

    # Define a SQL query to search for the keyword in the database
   
    query = "SELECT * FROM movie WHERE actorname LIKE '%{}%'".format(keyword)
    
    #query=("SELECT * FROM movie WHERE actorname LIKE %{0}% OR title LIKE %{0}% OR actor2name LIKE %{0}% OR directorname LIKE %{0}% OR year LIKE %{0}% OR genre LIKE %{0}%".format(keyword))
    # Execute the query,
    cursor = connection.cursor()
    # Define the columns to search in
    #columns = ["title","actorname", "actor2name","directorname","genre","year","language","keyword"]

# Build the query string dynamically based on the cns to search in
    #query = "SELECT * FROM movie WHERE "
    #for column in columns:
    #    query += f"{column} LIKE '%{keyword}%' OR "
    #    query = query[:-4]  # Remove the trailing " OR "
    cursor.execute(query)
    
    # Get the search results
    result = cursor.fetchall()

    # Close the database connection
    cursor.close()
    connection.close()

    # Render the search results template with the search results
    return render_template('search.html', results=result)

if __name__ == '__main__':
    app.run(debug=True)

