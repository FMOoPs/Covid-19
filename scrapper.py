from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import re
import sqlite3

conn = sqlite3.connect('WORLD.sqlite')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Id (id INTEGER PRIMARY KEY UNIQUE,ids INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS country (id INTEGER PRIMARY KEY UNIQUE,country TEXT)""")
cur.execute("""CREATE TABLE IF NOT EXISTS total (id INTEGER PRIMARY KEY UNIQUE,total INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS newcases (id INTEGER PRIMARY KEY UNIQUE,newcases INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS totdeath (id INTEGER PRIMARY KEY UNIQUE,totdeath INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS newdeath (id INTEGER PRIMARY KEY UNIQUE,newdeath INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS totrecover (id INTEGER PRIMARY KEY UNIQUE,totrecover INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS activecases (id INTEGER PRIMARY KEY UNIQUE,activecases INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS seriouscases (id INTEGER PRIMARY KEY UNIQUE,seriouscases INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS casespm (id INTEGER PRIMARY KEY UNIQUE,casespm INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS deathpm (id INTEGER PRIMARY KEY UNIQUE,deathpm INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS tests (id INTEGER PRIMARY KEY UNIQUE,tests INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS testpm (id INTEGER PRIMARY KEY UNIQUE,testpm INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS population (id INTEGER PRIMARY KEY UNIQUE,population INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS continent (id INTEGER PRIMARY KEY UNIQUE,continent TEXT)""")

def db(c, t):
    if c == 1:
        cur.execute('INSERT OR IGNORE INTO id (id) VALUES ( ? )', (t,))
        conn.commit()
    if c == 2:
        cur.execute('INSERT OR IGNORE INTO country (country) VALUES ( ? )', (t,))
        conn.commit()
    if c == 3:
        cur.execute('INSERT OR IGNORE INTO total (total) VALUES ( ? )', (t,))
        conn.commit()
    if c == 4:
        cur.execute('INSERT OR IGNORE INTO newcases (newcases) VALUES ( ? )', (t,))
        conn.commit()
    if c == 5:
        cur.execute('INSERT OR IGNORE INTO totdeath (totdeath) VALUES ( ? )', (t,))
        conn.commit()
    if c == 6:
        cur.execute('INSERT OR IGNORE INTO newdeath (newdeath) VALUES ( ? )', (t,))
        conn.commit()
    if c == 7:
        cur.execute('INSERT OR IGNORE INTO totrecover (totrecover) VALUES ( ? )', (t,))
        conn.commit()
    if c == 8:
        cur.execute('INSERT OR IGNORE INTO activecases (activecases) VALUES ( ? )', (t,))
        conn.commit()
    if c == 9:
        cur.execute('INSERT OR IGNORE INTO seriouscases (seriouscases) VALUES ( ? )', (t,))
        conn.commit()
    if c == 10:
        cur.execute('INSERT OR IGNORE INTO casespm (casespm) VALUES ( ? )', (t,))
        conn.commit()
    if c == 11:
        cur.execute('INSERT OR IGNORE INTO deathpm (deathpm) VALUES ( ? )', (t,))
        conn.commit()
    if c == 12:
        cur.execute('INSERT OR IGNORE INTO tests (tests) VALUES ( ? )', (t,))
        conn.commit()
    if c == 13:
        cur.execute('INSERT OR IGNORE INTO testpm (testpm) VALUES ( ? )', (t,))
        conn.commit()
    if c == 14:
        cur.execute('INSERT OR IGNORE INTO population (population) VALUES ( ? )', (t,))
        conn.commit()
    if c == 15:
        cur.execute('INSERT OR IGNORE INTO continent (continent) VALUES ( ? )', (t,))
        conn.commit()

# Get the site html, Extract data
c = 0
count = 0
html = urlopen(
    Request('https://www.worldometers.info/coronavirus/', headers={'User-Agent': 'Mozilla/5.0'})).read().decode()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')
tbody = table.find('tbody')
rows = tbody.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    for col in cols:
        c = c + 1
        if len(col.text) < 1:
            t = 0
            # print(t, 'a')
            db(c, t)
            continue
        else:
            x = re.findall('([0-9]+)', str(col.text))
            if len(x) < 1:
                t = col.text.strip()
                db(c, t)
                # print(t, 'b')
                continue
            if len(x) == 1:
                w = x[0]
                t = int(w)
                db(c, t)
                # print(t, 'c')
                continue
            if len(x) == 2:
                w = x[0] + x[1]
                t = int(w)
                db(c, t)
                # print(t, 'd')
                continue
            if len(x) == 3:
                w = x[0] + x[1] + x[2]
                t = int(w)
                db(c, t)
                # print(t, 'e')
                continue
            if len(x) == 4:
                w = x[0] + x[1] + x[2] + x[3]
                t = int(w)
                db(c, t)
                # print(t, 'f')
                continue
    c = 0
    count = count + 1
    print(count)

