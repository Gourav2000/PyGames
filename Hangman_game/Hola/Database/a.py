import os
import sys
import multiprocessing
import threading
import requests
from bs4 import BeautifulSoup
import sqlite3
import time
Link="https://codeforces.com/problemset"
start =time.perf_counter()
tag="float: left;"

data=requests.get(Link)
assert data.status_code==200
soup=BeautifulSoup(data.content,"html.parser")

L=[]
for i in soup.findAll("td"):
    u=i.find("div",style=tag)
    if u:
        O=u.find("a")
        if O:
            conn=sqlite3.connect("codeforces.db")
            cur=conn.cursor()
            cur.execute(f''' INSERT INTO Cdf ({O.get_text(),f"Link+'/'+O.get('href')")}))
            conn.commit()
            conn.close()
            L.append((O.get_text(),f"{Link}/{O.get('href')}"))
def create_database():
    conn=sqlite3.connect("codeforces.db")
    cur=conn.cursor()
    
    conn.commit()
    conn.close()

    
create_database()
       
    
    



    

    


end=time.perf_counter()
print(end-start)