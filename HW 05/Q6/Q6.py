import subprocess
import sys 

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
install("psycopg2-binary")

import psycopg2

conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="bhoomikamoorjani", 
                        password="Intelinside3812*", 
                        database="postgres")

cur = conn.cursor()
cur.execute("CREATE TABLE employees(id SERIAL, fname VARCHAR(10),lname VARCHAR(10))")
conn.commit()
cur.close()
conn.close()
