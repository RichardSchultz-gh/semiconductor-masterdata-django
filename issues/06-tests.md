# 06 Tests

PRD: [losseite-nachbau](../prd/losseite-nachbau.md) · Abhängig von: [01](01-model-und-import.md), [02](02-modelform-und-view.md), für den Rechte-Test [04](04-rollen.md)

## Ziel

Ein paar kleine automatische Tests zeigen, dass Import, Validierung und Rechte funktionieren. Im Flask-Original gab es dafür nur manuelle Tests im Bugtracker.

## Checkliste

- [ ] `src/lots/tests.py` mit `django.test.TestCase` (eigene Test-Datenbank, wird nach jedem Test zurückgesetzt)
- [ ] Kleine Test-CSV mit 3–5 Zeilen in `src/lots/testdata/` (Sonderfälle: leeres `ENTEROPER`, leeres `DISPTOOL`, Zeitstempel mit Uhrzeit)
- [ ] Import: `call_command("import_lots", ...)` zweimal aufrufen → Anzahl bleibt gleich, keine Duplikate
- [ ] Import: leerer Zeitstempel wird `None`, Zeitstempel wird als Berliner Zeit gespeichert
- [ ] Form: ungültiger State und Buchstaben bei `priority` → `is_valid()` ist `False`, Fehler am richtigen Feld
- [ ] View: POST mit gültigen Daten speichert und leitet weiter, unbekannte Lot-ID → 404
- [ ] Optional (nach 04): Mitarbeiter ruft die Bearbeiten-URL auf → 403, Fertigungsleiter → 200
- [ ] Tests laufen mit `python src/manage.py test lots`, Befehl im README erwähnen
- [ ] Commit

## Hinweise

- Pfad zur Test-CSV relativ zur Testdatei bilden (`Path(__file__).parent / "testdata" / ...`), nicht zum Startordner
- Priorität bei Zeitmangel: Import und Form zuerst, View- und Rechte-Test danach

## Fertig, wenn

`python src/manage.py test lots` läuft grün und deckt mindestens Import und Form ab.
