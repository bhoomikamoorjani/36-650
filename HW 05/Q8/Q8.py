import psycopg2
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="bhoomikamoorjani", 
                        password="Intelinside3812*", 
                        database="postgres")
cur = conn.cursor()
cur.execute("SELECT * FROM employees ORDER BY RANDOM() LIMIT 10")

for row in cur:
    print(row)

