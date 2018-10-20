#Eine Pythondatei ist eine normale und menschenlesbare Testdatei,
# sie bekommt die Dateiendung .py

#Zu Beginn werden die Pakete importiert, welche zusätzliche Funktionalität einbringen

import numpy as np
import matplotlib.pyplot as plt
#Das "as" ist optional und erlaubt es in Zukunft z.B. "np" synonym zu "numpy" zu benutzen.

#Alle Zeilen, die mit "#" beginnen sind nur Kommentare und werden bei der Ausführung übersprungen.

# Es werden 37 Zufallszahlen im Bereich von 0 bis 36 ermittelt
neuePerm = np.random.random_integers(0,36,size=37)

#so wirft man sie auf den Schirm
print("Unsere Rotation ergab folgende Zahlen:\n",neuePerm)
#Es wird eine festgelegte Zeichenkette zwischen den "" ausgegeben und danach die kommaseparierte Variable (Liste)

#die Methode bincount zählt alle 37 Zahlen durch
bc  = np.bincount(neuePerm , minlength=37)
#Nun haben wir alle Treffer sortiert nach Vorkommen 0x, 1x, 2x usw in bc 
#das Ergebnis ist eine Tabelle in der die Treffer auf Zero zuerst stehen,
# gefolgt von den Treffern auf 1 ... 36
print("\nDas ergibt folgendes Trefferbild:\n",bc)

#Wenn "\n" in den Zeichenketten auftaucht, ist das ein Zeilenumbruch

# Graphisch ausgeben als Histogramm
#Erkärung folgt bei Bedarf
plt.hist(bc, color='r')
plt.hist(neuePerm,bins=73, color="g" , alpha=0.4)
plt.show()
