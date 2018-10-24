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
   
  Maximale Dauer: 2^40 / (5 * 10^12) = 0.2199 Sekunden
  Durchschnittliche Dauer: 0.2199 Sekunden / 2 = 0.10995 Sekunden
  Minimale Dauer: << 1 Sekunde
   
  56 Bit 
  
  Maximale Dauer: 2^56 / (5 * 10^12) = 14411.52 Sekunden
  Durchschnittliche Dauer: 14411.52 Sekunden Sekunden / 2 = 7206 Sekunden
  Minimale Dauer: << 1 Sekunde
  
  64 Bit

  Maximale Dauer: 2^64 / (5 * 10^12) = 3.69 * 10^6 Sekunden = 42.71 Tage
  Durchschnittliche Dauer: 3.69 * 10^6 Sekunden / 2 = 1845000 Sekunden = 21.35 Tage
  Minimale Dauer: << 1 Sekunde
  
  112 Bit

  Maximale Dauer: 2^112 / (5 * 10^12) = 1.04 * 10^21 Sekunden
  Durchschnittliche Dauer:  1.04 * 10^21 Sekunden / 2 = 5.2 * 10^20 Sekunden
  Minimale Dauer: << 1 Sekunde

  128 Bit
  
  Maximale Dauer: 2^128 / (5 * 10^12) = 6.81 * 10^25 Sekunden
  Durchschnittliche Dauer:  6.81 * 10^25 Sekunden / 2 = 3.41 * 10^25 Sekunden
  Minimale Dauer: << 1 Sekunde

  ```


* In wievielen Jahren könnte mit einem Etat von 1 Mrd Euro unter der Annahme der Weitergeltung von Moore's Law eine Schlüsselsuchmaschine gebaut werden, welche eine durchschnittliche Suchzeit von 24 Stunden benötigt?

```
FORMELN:  
Anzahl Prüfungen / Sekunde = (Etat / Preis ASIC-Einheit) * Anzahl Prüfungen pro ASIC-Einheit pro Sekunde
Preis ASIC-Einheit = 100 / 2^x
x = Anzahl Jahre, die vergangen sind
Durchschnittl. Suchzeit = Anzahl Schlüsselkombinationen / Anzahl Prüfungen pro Sekunde
Anzahl Prüfungen pro Sekunde = Anzahl Schlüsselkombinationen / Durchschnittl. Suchzeit

Wir gehen von einer 128 Bit Schlüssellänge aus.

Um eine 128 Bit Schlüssellänge per Brute force in 24 Stunden zu knacken, würde man folgende Rechenkraft benötigen:

Anzahl Prüfungen pro Sekunde = 2^128 / 3.41 * 10^25 Sekunden = 9.97 * 10^62

Unter Annahme von Moore's Law und einem Etat von 1 Mrd. Euro würde man X Jahre warten müssen, um dies zu ermöglichen.

Anzahl Prüfungen / Sekunde = (Etat / Preis ASIC-Einheit) * Anzahl Prüfungen pro ASIC-Einheit pro Sekunde
Preis ASIC-Einheit = 100 / 2^x


RECHNUNG: 
Die erste Formal umgestellt und alle bekannten Variablen eingesetzt ergibt sich folgende Rechnung.

x = log2(100 * (9.97 * 10^62) / (1 * 10^9) *( 5 * 10^8))
x = ~215 Jahre

```
