# 01 Model und CSV-Import

PRD: [losseite-nachbau](../prd/losseite-nachbau.md)

## Ziel

Model `Lot` als Gegenstück zu `mapper.py:20`, im Admin prüfbar, mit den 1000 Losen aus `LOT.csv` befüllt.

## Checkliste

- [x] App `lots` anlegen und in `INSTALLED_APPS` eintragen
- [x] Model `Lot` mit `lotid` als Primärschlüssel
- [x] `null`/`blank` nach Lebenszyklus des Loses (Felder, die beim Anlegen in `los_starten.py:109` fehlen, sind optional)
- [x] `Lot.State` als `TextChoices`, Werte großgeschrieben wie in den Daten, Default `INIT`
- [x] `Meta` (`ordering`, `verbose_name`) und `__str__`
- [x] Migration erzeugen, mit `sqlmigrate` prüfen, anwenden
- [x] Superuser anlegen, Model im Admin registrieren
- [x] `LotAdmin` mit `list_display`, `list_filter`, `search_fields`
- [ ] `"product"` in `list_filter` ergänzen
- [ ] Settings: `LANGUAGE_CODE = 'de-de'`, `TIME_ZONE = 'Europe/Berlin'`
- [ ] Erster Commit (vorher prüfen, dass `db.sqlite3` nicht getrackt wird)
- [ ] Management-Command `import_lots` für `LOT.csv`
- [ ] Commit

## Hinweise zum Import

- Spaltenköpfe der CSV sind großgeschrieben (`LOTID`, `PRIORITY` …)
- Leere Werte kommen als `""`: bei Datums-/Zeitfeldern → `None`, bei Textfeldern (`disptool`) → `""` lassen, weil die Spalte `NOT NULL` ist
- Zeitstempel sind naiv, `USE_TZ = True` → Entscheidung nötig (`make_aware` oder Warnung in Kauf nehmen)
- Import soll mehrfach laufen können, ohne Duplikate
- `choices` werden beim direkten Speichern nicht geprüft
- In der CSV kommen nur `FIN` (999) und `HOLD` (1) vor

## Fertig, wenn

Die 1000 Lose erscheinen im Admin und lassen sich nach State, Kunde, Produkt und Fälligkeit filtern.
