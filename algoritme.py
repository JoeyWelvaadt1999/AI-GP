import psycopg2

con = psycopg2.connect(
    host = 'localhost',
    database = 'RecEngine', #database naam
    user = 'postgres',
    password= 'snellestijn') #database wachtwoord
cur = con.cursor()

#stel het productID in
productID = '4269'


def productenZoeken(id):
    #verkrijg de subcategorie en subsubcategorie
    cur.execute(f"select subcategory,subsubcategory from products where \"id\" = '{id}' ")
    cats = cur.fetchall()[0]
    
    #sla de categorien op in variabelen
    subcategory = cats[0]
    subsubcategory = cats[1]
    
    #zoek in de database naar producten die voldoen aan de categorie eisen
    cur.execute(f"select \"id\" from products where subcategory = '{subcategory}' and subsubcategory = '{subsubcategory}' and \"id\" <> '{id}' order by random() limit 4;")
    ids = cur.fetchall()

    #return een overzichtekijke lijst
    return [i[0] for i in ids]


#zoek naar producten met het ingestelde productID (regel 10)
producten = productenZoeken(productID)
print(producten)


cur.close() #sluit de cursor
con.close() #stop de verbinding