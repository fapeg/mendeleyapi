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
