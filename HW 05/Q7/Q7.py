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
cur.execute("INSERT INTO employees(SELECT generate_series(1,500) AS id, ('{Alpha,Beta,Gamma}'::text[])[ceil(random()*3)] AS fname, ('{Delta,Lambda,Theta}'::text[])[ceil(random()*3)] AS lname)")
conn.commit()
cur.close()
conn.close()

