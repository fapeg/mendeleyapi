Code
====

Für das Projekt wurden zwei Pythondateien angefertigt: Die eine für das Abrufen der Daten (hole_daten.py)
und die andere für die Erstellung der Grafiken (plotten.py). Die anderen Dateien, wie z.B. mendeley_client.py
werden zum Verständnis dieser Projektarbeit vorausgesetzt.

hole_daten.py
*************

Folgende Module bzw. Methoden werden für die Bearbeitung der Aufgaben angewendet:

.. code-block:: python

    #!/usr/bin/env python
    # encoding: utf-8

    from pprint import pprint
    from mendeley_client import *
    import os, sys, json, time


    mendeley = create_client()


Aufgabe 1
---------

Die Verteilung der Publikationen in Mendeley über die letzten 10 Jahre wird mittels einer for-Schleife 
ermittelt. Dabei wird für jedes Jahr die Suche mendeley.search('year:'+str(jahr) ausgeführt und in das
dictionary publikationen10 mit dem jeweiligen Jahr als key gespeichert. Die Gesamtanzahl für das jeweilige
Jahr wird am Ende des Durchlaufs der for-Schleife durch 'total_results' definiert und ist zugleich der 
Wert des jeweiligen keys. Das dictionary publikationen10 wird als json-Datei (aufgabe1.json) gespeichert:

.. code-block:: python

    # aufgabe 1: Wie verteilen sich die in Mendeley abgelegten Publikationen auf die letzten 10 Jahre?
    # (Dafür müssen nicht alle Publikationen heruntergeladen werden!)
    publikationen10 = {}
    for jahr in range(2003,2013): # letzte zehn jahre: von 2003 bis 2012 (trotzdem in range 2013 angeben)
        response = mendeley.search('year:'+str(jahr))
        publikationen10[jahr]=response['total_results']
    #in json datei speichern
    with open("aufgabe1.json", "w") as json_output:
        json.dump(publikationen10, json_output)

Aufgabe 2
---------

Bei der Abfrage der Tags (mendeley.tag_stats(6)) werden in der API standartisiert die Top 20 Tags ausgegeben.
Die ID der Kategorie "Computer and Information Science" lautet 6. In das Dictionary top20 werden die Tags mit
der Anzahl an Vorkommnissen ('count') gespeichert. Das Dictionary wird, wie in Aufgabe 1, in eine json-Datei
gespeichert:

.. code-block:: python

    # aufgabe 2: Was sind die Top20-Tags in der Kategorie „Computer and Information Science“?
    # hole die top 20 tags aus der kategorie "computer and information science"
    response = mendeley.tag_stats(6) # 6 ist die kategorie-id
    top20 = {}
    for tag in response:
        top20[tag['name']]=tag['count']
    with open("aufgabe2.json", "w") as json_output:
        json.dump(top20, json_output)


Aufgabe 3
---------

Diese Aufgabe ist nicht lösbar, sodass wir Sie bewusst nicht bearbeitet haben! :)

.. code-block:: python
	# aufgabe 3: Was sind die 10 populärsten (viele leser) Publikationen die in der Zeitschrift „Nature“ erschienen sind?
	# das ist sehr schwierig. paper_stats gibt die 50 populärsten Zeitschriften aus,
	# allerdings ist da nur eine publikation aus Nature dabei.
	# wir könnten über search danach suchen, haben dann aber kein ranking nach popularität


Aufgabe 4
---------

Für die Bearbeitung dieser Aufgabe ist die Methode authored notwendig. Wir suchen in unserem
Beispiel nach "Wolfgang G Stock" und geben uns die ersten 500 Dokumente mit diesem Autor aus.
Wie in den vorherigen Aufgaben werden die Treffer mit einer for-Schleife durchsucht und in das
jeweilige dictionary kontinuierlich gespeichert, welches als json-Datei gespeichert wird. Das
Publikationsjahr steht in pub_jahre der Dokumente. Bei den Co-Autoren werden in der for-Schleife
alle Autoren, welche nicht den Vornamen "Wolfgang G." und Nachnamen "Stock" haben, auch als 
Co-Autoren identifiziert. Leider werden falsche Einträge der Autoren wie z.B. bei dem Vornamen
"Wolfgang" und dem Nachnamen "G. Stock" auch als Co-Autoren gefiltert. Der Code sieht wie folgt aus:

.. code-block:: python

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


Aufgabe 5
---------
Zunächst muss jeder Eintrag in den Kategorien (cat_response) durchsucht werden. Das Zählen der Vorkommnisse in den
jeweiligen Kategorien verläuft ähnlich wie in den vorherigen Aufgaben. Der Code sieht wie folgt aus:

.. code-block:: python

    # aufgabe 5: Suche nach dem Tag „ontology“ und bestimme die Häufigkeit für jede Kategorie in Mendeley für das Jahr 2011.
    # erster schritt: liste mit allen kategorien holen:
    total_pages = 1
    page = 0
    cat_response = mendeley.categories()
    ontology_anzahl={}
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



plotten.py
**********

Für das Erstellen eines Diagramms werden jeweils die json-Datein als json_input für die Grafiken verwendet.
Der Code für die Erstellung der Balkendiagramme sieht wie folgt aus:

.. code-block:: python

    # -*- coding: utf-8 -*- 

    import numpy as np
    import matplotlib.pyplot as plt
    import json

    # plotten der Ergebnisse
    # Vorlage: http://matplotlib.org/users/screenshots.html
    def plot_balken(dict_daten, titel, name_x, name_y):
        x_werte, y_werte = tuple(dict_daten.values()), tuple(dict_daten.keys())
        n = len(x_werte)
        fig, ax = plt.subplots()
        index = np.arange(n)
        bar_width = 0.35
        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        rects1 = plt.bar(index, x_werte, bar_width,
                         alpha=opacity,
                         color='b',
                         error_kw=error_config)
        plt.xlabel(name_x)
        plt.ylabel(name_y)
        plt.title(titel)
        plt.xticks(index + bar_width, y_werte)
        plt.legend()
        fig.autofmt_xdate()
        plt.tight_layout()
        plt.show()
        

    # Aufgabe 1
    with open("aufgabe1.json", "r") as json_input:
        publikationen10 = json.load(json_input)
    plot_balken(publikationen10, 'Verteilung der Mendeley-Publikationen auf die letzten 10 Jahre', 'Jahr', 'Anzahl Publikationen')

    # Aufgabe 2
    with open("aufgabe2.json", "r") as json_input:
        top20 = json.load(json_input)
    plot_balken(top20, 'Top20 Tags in der Kategorie "Computer and Information Science"', 'Tags', 'Anzahl Tags')

    # Aufgabe 4a
    with open("aufgabe4a.json", "r") as json_input:
        pub_jahre = json.load(json_input)
    plot_balken(pub_jahre, 'Publikationsanzahl nach Jahren von Wolfgang G Stock', 'Jahr', 'Anzahl Publikationen')

    # Aufgabe 4b
    with open("aufgabe4b.json", "r") as json_input:
        coAutoren = json.load(json_input)
    plot_balken(coAutoren, 'Co-Autoren von Wolfgang G Stock', 'Co-Autor', 'Anzahl gemeinsamer Publikationen')

    # Aufgabe 5
    with open("aufgabe5.json", "r") as json_input:
        ontology_anzahl = json.load(json_input)
    plot_balken(ontology_anzahl, 'Tag "ontology" in den verschiedenen Kategorien', 'Kategorie', 'Vorkommen des Tags "Ontology"')
