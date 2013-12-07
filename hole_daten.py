#!/usr/bin/env python
# encoding: utf-8

from pprint import pprint
from mendeley_client import *
import os, sys, json

mendeley = create_client()


# aufgabe 1: Wie verteilen sich die in Mendeley abgelegten Publikationen auf die letzten 10 Jahre?
# (Dafür müssen nicht alle Publikationen heruntergeladen werden!)
# hier ist vermutlich die api-kategorie "papers" gemeint. "publications" gibt einem zeitschriften zurück
# muss noch verbessert werden:
# man bekommt ein dicitionary mit publikationsnamen und jahreszahl zurück (brauchen wir)
# aber bisher nur für die top-publikationen, das sind 20 oder so
response = mendeley.paper_stats()
print "Papers:\n\n"
pprint (response)
print "\n ---------------------- \n"


# aufgabe 2: Was sind die Top20-Tags in der Kategorie „Computer and Information Science“?
# hole die top 20 tags aus der kategorie "computer and information science"
response = mendeley.tag_stats(6) # 6 ist die kategorie-id
print "Top 20 Tags in Kategorie 'Computer and information science'\n\n"
pprint(response)
print "\n ---------------------- \n"


# aufgabe 3: Was sind die 10 populärsten Publikationen die in der Zeitschrift „Nature“ erschienen sind?
# das ist sehr schwierig. paper_stats gibt die 50 populärsten Zeitschriften aus,
# allerdings ist da nur eine publikation aus Nature dabei.
# wir könnten über search danach suchen, haben dann aber kein ranking nach popularität
response = mendeley.search('published_in:Nature', items=100)
print "Top 10 Publikationen in Zeitschrift 'Nature'\n\n"
pprint(response)
print "\n ---------------------- \n"


# aufgabe 4: Auflistung aller Publikationen von Prof. Wolfgang G. Stock
# (Extrahiere diese Daten automatisch mit Hilfe von Python!)
response = mendeley.authored('"Wolfgang G Stock"', items=500)
print "Publikationen von Stock\n\n"
pprint(response)
print "\n ---------------------- \n"


# aufgabe 5: Suche nach dem Tag „ontology“ und bestimme die Häufigkeit für jede Kategorie in Mendeley für das Jahr 2011.
# erster schritt: liste mit allen kategorien holen:
cat_response = mendeley.categories()
for eintrag in cat_response: # jede kategorie durchgehen
    response = mendeley.tagged('ontology', cat=eintrag['id'])
    print eintrag['name'] + " (ID " + str(eintrag['id']) + "): "
    print "    "+ str(response['total_results']) + " Ergebnisse\n" 


