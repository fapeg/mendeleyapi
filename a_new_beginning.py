#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mendeley Open API Example Client

Copyright (c) 2010, Mendeley Ltd. <copyright@mendeley.com>

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

For details of the Mendeley Open API see http://dev.mendeley.com/

Example usage:

python example.py

"""

from collections import defaultdict
from operator import itemgetter
from mendeley_client import *
import matplotlib.pyplot as mpl
import numpy
import os
import sys, time

# edit config.json first
mendeley = create_client()
total_pages = 1
page = 0
gesamtanzahl = 0

jahre, autoren, titel_liste = [], [], []
anzahl_jahre, anzahl_autoren = defaultdict(int), defaultdict(int)


while not page > total_pages-1:
    response = mendeley.authored('Wolfgang G Stock', items = 500)
    total_pages = response['total_pages']
    page += 1
    print str(page) + ". Seite"


    for more_detailed in response['documents']:
                print "bin in for schleife"
                print more_detailed
                all_authors = more_detailed["authors"]
                if all_authors == None:
                    all_authors = [{"surname": "NO", "forename": "NAME"}]
                jahr = more_detailed["year"]

                for element in all_authors:
                    print element["forename"]
                    print more_detailed["title"]
                    stock_ist_autor = False
                    co_autor_liste = []

                    if (element["surname"] == "Stock"):
                        if (element["forename"] == "Wolfgang G") or (element["forename"] == "Wolfgang G."):
                            print "\n\nVorname:", element["forename"]
                            print "Nachname:", element["surname"]
                            titel = more_detailed["title"].encode("utf8")

                            if titel not in titel_liste:
                                print "Titel:", titel
                                print "Jahr:", jahr
                                gesamtanzahl += 1
                                stock_ist_autor = True
                                co_anzahl = 1
                                jahre.append(jahr)
                                titel_liste.append(titel)

                            for element2 in all_authors:
                                if ((stock_ist_autor) and ((element2["surname"] != "Stock") or ((element2["forename"] != "Wolfgang G") and (element2["forename"] != "Wolfgang G.")))):
                                    co_autor_vorname = element2["forename"].encode("utf8")
                                    co_autor_nachname = element2["surname"].encode("utf8")
                                    if (co_autor_vorname == "Mechthild"):
                                        co_autor_vorname = "Mechtild"
                                    if ((co_autor_nachname == "Schlogl") or (co_autor_nachname == "Schloegl")):
                                        co_autor_nachname = "Schlögl"
                                    autor = co_autor_vorname + " " + co_autor_nachname
                                    if (autor not in co_autor_liste):
                                        print "\nCo-Autor %s" % co_anzahl
                                        print "Vorname:", co_autor_vorname
                                        print "Nachname:", co_autor_nachname
                                        co_anzahl += 1
                                        autoren.append(autor)
                                        co_autor_liste.append(autor)


response = mendeley.tag_stats("6")
print '\n\nTOP 20 Tags in der Kategorie "Computer and Information Science"\n'
tag_rank = 1
tag_rank_string = "1."
for element in response:
    print tag_rank_string, element["count"], "Mal", element["name"]
    tag_rank+=1
    tag_rank_string = str(tag_rank) + "."


print "\n\nTOP Co-Autoren von Prof. Wolgang G. Stock\n"
for autor in autoren:
    anzahl_autoren[autor] += 1

sorted_autoren = sorted(anzahl_autoren.items(), key=itemgetter(1), reverse=True)
for x in range (len(sorted_autoren)):
    print sorted_autoren[x][1],"Publikationen mit", sorted_autoren[x][0]

print "\nAnzahl aller Co-Autoren:", len(sorted_autoren)

print "\n\nPublikationen pro Jahr\n"
for jahr in jahre:
    anzahl_jahre[jahr] += 1

sorted_jahre = sorted(anzahl_jahre.items(), key=itemgetter(0), reverse=False)
for x in range (len(sorted_jahre)):
    print sorted_jahre[x][1],"Publikationen im Jahr",sorted_jahre[x][0]

print "\nAnzahl aller Publikationen:", gesamtanzahl

n = len(sorted_jahre)
bar_height, bar_years = (), ()
for x in range(n):
    bar_height = bar_height + (sorted_jahre[x][1],)
    bar_years = bar_years + (sorted_jahre[x][0],)

fig, ax = mpl.subplots()
index = numpy.arange(n)
bar_width = 0.35

rects1 = mpl.bar(index, bar_height, bar_width, color= "#4EFF8D")

mpl.xlabel("Jahre")
mpl.ylabel("Anzahl der Publikationen")
mpl.title("Alle Publikationen von Prof. Wolfgang G. Stock")
mpl.xticks(index + bar_width, bar_years)

mpl.tight_layout()
mpl.show()

