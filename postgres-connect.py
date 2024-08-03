import psycopg2
conn = psycopg2.connect(database = "postgres_db", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres123",
                        port = 5432)


cur = conn.cursor()
# Execute a command: create datacamp_courses table
cur.execute("""CREATE TABLE datacamp_courses(
            course_id SERIAL PRIMARY KEY,
            course_name VARCHAR (50) UNIQUE NOT NULL,
            course_instructor VARCHAR (100) NOT NULL,
            topic VARCHAR (20) NOT NULL);
            """)
query="INSERT INTO identity (_name, surname) VALUES ('Michel', 'Palefrois'), ('Renaud', 'Bertop');"
cur.execute(query)

# Make the changes to the database persistent
cur.commit()
# Close cursor and communication with the database
cur.close()
conn.close()