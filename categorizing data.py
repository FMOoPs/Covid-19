import sqlite3

conn = sqlite3.connect('WORLD.sqlite')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Africa (id INTEGER PRIMARY KEY UNIQUE,country TEXT,total INTEGER,newcases INTEGER,totdeath INTEGER,newdeath INTEGER,totrecover INTEGER,activecases INTEGER,seriouscases INTEGER,casespm INTEGER,deathpm INTEGER,tests INTEGER,testpm INTEGER,population INTEGER,continent TEXT)""")
cur.execute("""CREATE TABLE IF NOT EXISTS Asia (id INTEGER PRIMARY KEY UNIQUE,country TEXT,total INTEGER,newcases INTEGER,totdeath INTEGER,newdeath INTEGER,totrecover INTEGER,activecases INTEGER,seriouscases INTEGER,casespm INTEGER,deathpm INTEGER,tests INTEGER,testpm INTEGER,population INTEGER,continent TEXT)""")
cur.execute("""CREATE TABLE IF NOT EXISTS Europe (id INTEGER PRIMARY KEY UNIQUE,country TEXT,total INTEGER,newcases INTEGER,totdeath INTEGER,newdeath INTEGER,totrecover INTEGER,activecases INTEGER,seriouscases INTEGER,casespm INTEGER,deathpm INTEGER,tests INTEGER,testpm INTEGER,population INTEGER,continent TEXT)""")
cur.execute("""CREATE TABLE IF NOT EXISTS NorthAmerica (id INTEGER PRIMARY KEY UNIQUE,country TEXT,total INTEGER,newcases INTEGER,totdeath INTEGER,newdeath INTEGER,totrecover INTEGER,activecases INTEGER,seriouscases INTEGER,casespm INTEGER,deathpm INTEGER,tests INTEGER,testpm INTEGER,population INTEGER,continent TEXT)""")
cur.execute("""CREATE TABLE IF NOT EXISTS SouthAmerica (id INTEGER PRIMARY KEY UNIQUE,country TEXT,total INTEGER,newcases INTEGER,totdeath INTEGER,newdeath INTEGER,totrecover INTEGER,activecases INTEGER,seriouscases INTEGER,casespm INTEGER,deathpm INTEGER,tests INTEGER,testpm INTEGER,population INTEGER,continent TEXT)""")
cur.execute("""CREATE TABLE IF NOT EXISTS Australia_Oceania (id INTEGER PRIMARY KEY UNIQUE,country TEXT,total INTEGER,newcases INTEGER,totdeath INTEGER,newdeath INTEGER,totrecover INTEGER,activecases INTEGER,seriouscases INTEGER,casespm INTEGER,deathpm INTEGER,tests INTEGER,testpm INTEGER,population INTEGER,continent TEXT)""")
cur.execute("""CREATE TABLE IF NOT EXISTS WORLD (id INTEGER PRIMARY KEY UNIQUE,country TEXT,total INTEGER,newcases INTEGER,totdeath INTEGER,newdeath INTEGER,totrecover INTEGER,activecases INTEGER,seriouscases INTEGER,casespm INTEGER,deathpm INTEGER,tests INTEGER,testpm INTEGER,population INTEGER,continent TEXT)""")
cur.execute("""CREATE TABLE IF NOT EXISTS continents (continent TEXT, cases INTEGER, recovery INTEGER, tests INTEGER)""")

cur.execute('SELECT continent FROM continent')
x = cur.fetchall()
l = []
for i in x:
    for e in i:
        if e in l: continue
        if len(e) < 4: continue
        l.append(e)


cur.execute('SELECT id FROM country')
c = cur.fetchall()
for i in range(len(c)):
    cur.execute('SELECT continent FROM continent WHERE id=?', (i,))
    a = cur.fetchall()
    for x in range(len(a)):
        if str(a[x][x]) not in l: continue
        country = cur.execute('SELECT country FROM country WHERE id=?', (i,)).fetchall()[x][x]
        total = cur.execute('SELECT total FROM total WHERE id=?', (i,)).fetchall()[x][x]
        newcases = cur.execute('SELECT newcases FROM newcases WHERE id=?', (i,)).fetchall()[x][x]
        totdeath = cur.execute('SELECT totdeath FROM totdeath WHERE id=?', (i,)).fetchall()[x][x]
        newdeath = cur.execute('SELECT newdeath FROM newdeath WHERE id=?', (i,)).fetchall()[x][x]
        totrecover = cur.execute('SELECT totrecover FROM totrecover WHERE id=?', (i,)).fetchall()[x][x]
        activecases = cur.execute('SELECT activecases FROM activecases WHERE id=?', (i,)).fetchall()[x][x]
        seriouscases = cur.execute('SELECT seriouscases FROM seriouscases WHERE id=?', (i,)).fetchall()[x][x]
        casespm = cur.execute('SELECT casespm FROM casespm WHERE id=?', (i,)).fetchall()[x][x]
        deathpm = cur.execute('SELECT deathpm FROM deathpm WHERE id=?', (i,)).fetchall()[x][x]
        tests = cur.execute('SELECT tests FROM tests WHERE id=?', (i,)).fetchall()[x][x]
        testpm = cur.execute('SELECT testpm FROM testpm WHERE id=?', (i,)).fetchall()[x][x]
        population = cur.execute('SELECT population FROM population WHERE id=?', (i,)).fetchall()[x][x]
        if country in l: continue
        cur.execute(
            "INSERT OR IGNORE INTO World (country,total,newcases,totdeath,newdeath,totrecover,activecases,seriouscases,casespm,deathpm,tests,testpm,population) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (country, total, newcases, totdeath, newdeath, totrecover, activecases, seriouscases, casespm, deathpm,
             tests, testpm, population))
        conn.commit()
        if str(a[x][x]) == 'North America':
            cur.execute("INSERT OR IGNORE INTO NorthAmerica (country,total,newcases,totdeath,newdeath,totrecover,activecases,seriouscases,casespm,deathpm,tests,testpm,population) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (country,total,newcases,totdeath,newdeath,totrecover,activecases,seriouscases,casespm,deathpm,tests,testpm,population))
            conn.commit()
            print('Done North America')
        if str(a[x][x]) == 'South America':
            cur.execute(
                "INSERT OR IGNORE INTO SouthAmerica (country,total,newcases,totdeath,newdeath,totrecover,activecases,seriouscases,casespm,deathpm,tests,testpm,population) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (country, total, newcases, totdeath, newdeath, totrecover, activecases, seriouscases, casespm, deathpm,
                 tests, testpm, population))
            conn.commit()
            print('Done South America')
        if str(a[x][x]) == 'Europe':
            cur.execute(
                "INSERT OR IGNORE INTO Europe (country,total,newcases,totdeath,newdeath,totrecover,activecases,seriouscases,casespm,deathpm,tests,testpm,population) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (country, total, newcases, totdeath, newdeath, totrecover, activecases, seriouscases, casespm, deathpm,
                 tests, testpm, population))
            conn.commit()
            print('Done Europe')
        if str(a[x][x]) == 'Africa':
            cur.execute(
                "INSERT OR IGNORE INTO Africa (country,total,newcases,totdeath,newdeath,totrecover,activecases,seriouscases,casespm,deathpm,tests,testpm,population) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (country, total, newcases, totdeath, newdeath, totrecover, activecases, seriouscases, casespm, deathpm,
                 tests, testpm, population))
            conn.commit()
            print('Done Africa')
        if str(a[x][x]) == 'Australia/Oceania':
            cur.execute(
                "INSERT OR IGNORE INTO Australia_Oceania (country,total,newcases,totdeath,newdeath,totrecover,activecases,seriouscases,casespm,deathpm,tests,testpm,population) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (country, total, newcases, totdeath, newdeath, totrecover, activecases, seriouscases, casespm, deathpm,
                 tests, testpm, population))
            conn.commit()
            print('Done Austrialia')
        if str(a[x][x]) == 'Asia':
            cur.execute(
                "INSERT OR IGNORE INTO Asia (country,total,newcases,totdeath,newdeath,totrecover,activecases,seriouscases,casespm,deathpm,tests,testpm,population) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (country, total, newcases, totdeath, newdeath, totrecover, activecases, seriouscases, casespm, deathpm,
                 tests, testpm, population))
            conn.commit()
            print('Done Asia')

#Cases Counter
af = cur.execute('SELECT total FROM Africa').fetchall()
counteraf = 0
for i in range(len(af)):
    if af[i][0] == 'N/A': continue
    counteraf = counteraf + af[i][0]

asia = cur.execute('SELECT total FROM Asia').fetchall()
counterasia = 0
for i in range(len(asia)):
    if asia[i][0] == 'N/A': continue
    counterasia = counterasia + asia[i][0]

eu = cur.execute('SELECT total FROM Europe').fetchall()
countereu = 0
for i in range(len(eu)):
    if eu[i][0] == 'N/A': continue
    countereu = countereu + eu[i][0]

na = cur.execute('SELECT total FROM NorthAmerica').fetchall()
counterna = 0
for i in range(len(na)):
    if na[i][0] == 'N/A': continue
    counterna = counterna + na[i][0]

sa = cur.execute('SELECT total FROM SouthAmerica').fetchall()
countersa = 0
for i in range(len(sa)):
    if sa[i][0] == 'N/A': continue
    countersa = countersa + sa[i][0]

aus = cur.execute('SELECT total FROM Australia_Oceania').fetchall()
counteraus = 0
for i in range(len(aus)):
    if aus[i][0] == 'N/A': continue
    counteraus = counteraus + aus[i][0]



#Tests Counter
aff = cur.execute('SELECT tests FROM Africa').fetchall()
testaf = 0
for i in range(len(aff)):
    if aff[i][0] == 'N/A': continue
    testaf = testaf + aff[i][0]

asiaa = cur.execute('SELECT tests FROM Asia').fetchall()
testasia = 0
for i in range(len(asiaa)):
    if asiaa[i][0] == 'N/A': continue
    testasia = testasia + asiaa[i][0]

euu = cur.execute('SELECT tests FROM Europe').fetchall()
testeu = 0
for i in range(len(euu)):
    if euu[i][0] == 'N/A': continue
    testeu = testeu + euu[i][0]

naa = cur.execute('SELECT tests FROM NorthAmerica').fetchall()
testna = 0
for i in range(len(naa)):
    if naa[i][0] == 'N/A': continue
    testna = testna + naa[i][0]

saa = cur.execute('SELECT tests FROM SouthAmerica').fetchall()
testsa = 0
for i in range(len(saa)):
    if saa[i][0] == 'N/A': continue
    testsa = testsa + saa[i][0]

auss = cur.execute('SELECT tests FROM Australia_Oceania').fetchall()
testaus = 0
for i in range(len(auss)):
    if auss[i][0] == 'N/A': continue
    testaus = testaus + auss[i][0]


#Recovery Counter
afff = cur.execute('SELECT totrecover FROM Africa').fetchall()
recaf = 0
for i in range(len(afff)):
    if afff[i][0] == 'N/A': continue
    recaf = recaf + afff[i][0]

asiaaa = cur.execute('SELECT totrecover FROM Asia').fetchall()
recasia = 0
for i in range(len(asiaaa)):
    if asiaaa[i][0] == 'N/A': continue
    recasia = recasia + asiaaa[i][0]

euuu = cur.execute('SELECT totrecover FROM Europe').fetchall()
receu = 0
for i in range(len(euuu)):
    if euuu[i][0] == 'N/A': continue
    print(type(euuu[i][0]))
    print(euuu[i][0])
    receu = receu + euuu[i][0]

naaa = cur.execute('SELECT totrecover FROM NorthAmerica').fetchall()
recna = 0
for i in range(len(naaa)):
    if naaa[i][0] == 'N/A': continue
    recna = recna + naaa[i][0]

saaa = cur.execute('SELECT totrecover FROM SouthAmerica').fetchall()
recsa = 0
for i in range(len(saaa)):
    if saaa[i][0] == 'N/A': continue
    recsa = recsa + saaa[i][0]

ausss = cur.execute('SELECT totrecover FROM Australia_Oceania').fetchall()
recaus = 0
for i in range(len(ausss)):
    if ausss[i][0] == 'N/A': continue
    recaus = recaus + ausss[i][0]

cur.execute("INSERT OR IGNORE INTO continents (continent, cases, recovery, tests) VALUES ('Africa', ?, ? ,?)", (counteraf,recaf,testaf))
conn.commit()
cur.execute("INSERT OR IGNORE INTO continents (continent, cases, recovery, tests) VALUES ('Europe', ?, ? ,?)", (countereu,receu,testeu))
conn.commit()
cur.execute("INSERT OR IGNORE INTO continents (continent, cases, recovery, tests) VALUES ('NorthAmerica', ?, ? ,?)", (counterna,recna,testna))
conn.commit()
cur.execute("INSERT OR IGNORE INTO continents (continent, cases, recovery, tests) VALUES ('SouthAmerica', ?, ? ,?)", (countersa,recsa,testsa))
conn.commit()
cur.execute("INSERT OR IGNORE INTO continents (continent, cases, recovery, tests) VALUES ('Asia', ?, ? ,?)", (counterasia,recasia,testasia))
conn.commit()
cur.execute("INSERT OR IGNORE INTO continents (continent, cases, recovery, tests) VALUES ('Australia', ?, ? ,?)", (counterasia,recaus,testaus))
conn.commit()

