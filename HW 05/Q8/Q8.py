"""
#Already installed in Q6
import subprocess
import sys 
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
install("psycopg2-binary")
"""
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

