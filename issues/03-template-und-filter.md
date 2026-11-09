# 03 Template, Liste und Filter

PRD: [losseite-nachbau](../prd/losseite-nachbau.md) · Abhängig von: [01](01-model-und-import.md)

## Ziel

Eigene Losliste als Gegenstück zu `Stammdaten_Los.html`, mit Filter nach Lot-ID und State. Die vier Verzweigungen aus `Stammdaten.py:109–116` entfallen.

## Checkliste

- [x] View für die Liste
- [x] Template mit Tabelle (Spalten wie im Admin oder Original)
- [x] Filterformular per GET (Lot-ID, State); State-Auswahl aus `Lot.State`, nicht von Hand getippt
- [x] Filter im View über ein QuerySet, das schrittweise eingeschränkt wird (Field Lookups)
- [x] Link von jeder Zeile zur Bearbeiten-Seite aus Teil 2
- [ ] Optional: Sortierung über die URL (serverseitig) oder per JS wie im Original
- [ ] Optional: Basis-Template, von dem Liste und Bearbeiten-Seite erben
- [x] Commit

## Fertig, wenn

Die Liste zeigt die Lose, beide Filter funktionieren einzeln und kombiniert, und jede Zeile führt zur Bearbeiten-Seite.
