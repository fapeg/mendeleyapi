#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from pprint import pprint
from mendeley_client import *
import os, sys, json, time


mendeley = create_client()



# aufgabe 1: Wie verteilen sich die in Mendeley abgelegten Publikationen auf die letzten 10 Jahre?
<<<<<<< HEAD
# (Dafür müssen nicht alle Publikationen heruntergeladen werden!)
=======
# (Dafür müssen nicht alle Publikationen heruntergeladen werden!)
>>>>>>> 780ec0119a33586a1f64b65aafad1f8fd678579a
publikationen10 = {}
for jahr in range(2003,2013): # letzte zehn jahre: von 2003 bis 2012 (trotzdem in range 2013 angeben)
    response = mendeley.search('year:'+str(jahr))
    publikationen10[jahr]=response['total_results']
#in json datei speichern
with open("aufgabe1.json", "w") as json_output:
    json.dump(publikationen10, json_output)


# aufgabe 2: Was sind die Top20-Tags in der Kategorie „Computer and Information Science“?
# hole die top 20 tags aus der kategorie "computer and information science"
response = mendeley.tag_stats(6) # 6 ist die kategorie-id
top20 = {}
for tag in response:
    top20[tag['name']]=tag['count']
with open("aufgabe2.json", "w") as json_output:
    json.dump(top20, json_output)


<<<<<<< HEAD
# aufgabe 3: Was sind die 10 populärsten (viele leser) Publikationen die in der Zeitschrift „Nature“ erschienen sind?
=======
# aufgabe 3: Was sind die 10 populärsten (viele leser) Publikationen die in der Zeitschrift „Nature“ erschienen sind?
>>>>>>> 780ec0119a33586a1f64b65aafad1f8fd678579a
# code sollte theoretisch funktionieren, wenn es mit der api klappen würde
# wir haben aber über 200 seiten die durchlaufen werden müssen, also auch mit sleep zu viel...
total_pages = 1
page = 0
nature_readers = {}
while not page > total_pages-1: 
    response = mendeley.search('published_in:Nature', items=500, page=page)
    total_pages = response['total_pages']
    for element in response['documents']:
        response_details = mendeley.details(element['uuid'])
        status = response_details['stats']
        readers = status['readers']
        nature_readers[response_details['title']]=readers
    page += 1
top10_nature = dict(sorted(nature_readers.items(), key=lambda x:x[1])[-10:])
with open("aufgabe3.json", "w") as json_output:
    json.dump(top10_nature0, json_output)



# aufgabe 4: Auflistung aller Publikationen von Prof. Wolfgang G. Stock
# (Extrahiere diese Daten automatisch mit Hilfe von Python!)
#      -Erstelle ein Diagramm der Publikationsanzahl über die vorhandenen Jahre
#      -Erstelle ein Ranking aller Co-Autoren mit denen Prof. Stock
#       zusammengearbeitet hat nach Anzahl der in Mendeley vorhandenen,
#       gemeinsamen Publikationen.
response = mendeley.authored('"Wolfgang G Stock"', items=500)
pub_jahre = {}
coAutoren = {}
for publikation in response['documents']:
    # Aufgabenteil a
    if publikation['year'] in pub_jahre:
        pub_jahre[publikation['year']]+=1
    else:
        pub_jahre[publikation['year']]=1   
    with open("aufgabe4a.json", "w") as json_output:
        json.dump(pub_jahre, json_output)
    #Aufgabenteil b
    for autor in publikation['authors']:
        if autor['forename']!="Wolfgang G." and autor['surname']!="Stock":
            if autor['surname'] in coAutoren:
                coAutoren[autor['surname']]+=1
            else:
                coAutoren[autor['surname']]=1
    with open("aufgabe4b.json", "w") as json_output:
        json.dump(coAutoren, json_output)
<<<<<<< HEAD
=======


>>>>>>> 780ec0119a33586a1f64b65aafad1f8fd678579a



# aufgabe 5: Suche nach dem Tag „ontology“ und bestimme die Häufigkeit für jede Kategorie in Mendeley für das Jahr 2011.
# erster schritt: liste mit allen kategorien holen:
cat_response = mendeley.categories()
ontology_anzahl={}
total_pages = 1
page = 0
for eintrag in cat_response: # jede kategorie durchgehen
    while not page > total_pages-1: 
        response = mendeley.tagged('ontology',cat=eintrag['id'], items = 10,page=page)
        total_pages = response['total_pages']
        for dokument in response['documents']:
            if dokument['year'] == 2011:
                if eintrag['name'] in ontology_anzahl:
                    ontology_anzahl[eintrag['name']]+=1
                else:
                    ontology_anzahl[eintrag['name']]=1
        
        page += 1
#        time.sleep(1200)
    page=0
#    time.sleep(1800) 

with open("aufgabe5.json", "w") as json_output:
    json.dump(ontology_anzahl, json_output)




