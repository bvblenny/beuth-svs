# beuth-svs

## Übung 1

### Aufgabe 1 Substitutionschiffren (42 Punkte)

[ubg_1.py](./ubg_1.py)

### Aufgabe 2 Schlüssellängen (18 Punkte)

Untersuchen Sie die Angriffsdauer von Brute-Force-Angriffen für die Schlüssellängen von 40, 56, 64, 112 und 128 Bit in folgenden Szenarien:
* Der Angreifer verfügt über ASICs, welche 5 * 10^8 Schlüssel pro Sekundeüberprüfen kann und über einen Etat von 1 Mio Euro verfügt. Die Kosten pro ASIC belaufen sich auf 50 Euro und wir nehmen weiter 50 Euro pro Einheit für die Integration an.

  * Wie viele Einheiten können mit dem zur Verfügung stehenden Etat parallel betrieben werden?
  
  ```
  10.000 Einheiten
  ```
  
  * Wie lange dauert die durchschnittliche, die minimale und die maximale Schlüsselsuchzeit?
  
  ```
  40 Bit:
   
  Maximale Dauer: 1099511627776 / (500000000 * 10000) = 0,2199 Sekunden
  Durchschnittliche Dauer: 0,2199 Sekunden / 2 = 0,10995 Sekunden
  Minimale Dauer: < 1 Sekunde
   
  56 Bit 
  
  Maximale Dauer: 1099511627776 / 500000000 = 2199 Sekunden / 60 = 36,65 Minuten
  Durchschnittliche Dauer: 2199 Sekunden / 2 = ~1099.5 Sekunden / 60 = 18,33 Minuten
  Minimale Dauer: < 1 Sekunde
  
  64 Bit
  
  112 Bit
  
  128 Bit
  
  Maximale Dauer: 1099511627776 / 500000000 = 2199 Sekunden / 60 = 36,65 Minuten
  Durchschnittliche Dauer: 2199 Sekunden / 2 = ~1099.5 Sekunden / 60 = 18,33 Minuten
  Minimale Dauer: < 1 Sekunde
  3,4028236692093846346337460743177e+38
  ```


* In wievielen Jahren könnte mit einem Etat von 1 Mrd Euro unter der Annahme der Weitergeltung von Moore's Law eine Schlüsselsuchmaschine gebaut werden, welche eine durchschnittliche Suchzeit von 24 Stunden benötigt?


Gesucht: Jahre

128

x = Anzahlschlüssel
y = Berechnung pro Sekunde

y = (anzahl der geräte) * (5 * 10^8)


anzahl der geräte =  1000000000 / ((preis pro gerät)/ (2* anzahlderJahre))

8 = 4
4 = 2
