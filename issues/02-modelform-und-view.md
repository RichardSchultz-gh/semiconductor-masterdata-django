# 02 ModelForm und View zum Bearbeiten

PRD: [losseite-nachbau](../prd/losseite-nachbau.md) · Abhängig von: [01](01-model-und-import.md)

## Ziel

Ein Los lässt sich auf einer eigenen Seite bearbeiten. Die ModelForm ersetzt die 13 einzelnen `if` + `update()` aus `Stammdaten.py:51–91` und die Hilfsfunktionen `get_args_right` / `get_timestamp_args_right` (`Stammdaten.py:126–139`).

## Checkliste

- [ ] `forms.py` in der App mit einer ModelForm für `Lot`
- [ ] Entscheiden, welche Felder bearbeitbar sind (`lotid` beim Bearbeiten nicht änderbar, wie `readonly` im Original)
- [ ] URL-Konfiguration der App anlegen und in `mysite/urls.py` einbinden
- [ ] View: Los laden (404, wenn es nicht existiert), Formular bei GET anzeigen, bei POST validieren und speichern
- [ ] Template mit Formular, CSRF-Token, Fehlermeldungen
- [ ] Nach erfolgreichem Speichern weiterleiten (Post/Redirect/Get)
- [ ] Optional: `clean()` für die Anmerkung aus `docs/test/Bugtracker.adoc:34` (z. B. INIT ohne `enteroper`/`procstart`, PROC nur mit `procstart`)
- [ ] Commit

## Vergleichen und notieren (für Anschreiben und README)

- Wie viele Zeilen ersetzt die ModelForm?
- Was passiert bei ungültigen Eingaben, verglichen mit dem Original?
- Warum POST statt GET?

## Fertig, wenn

Ein Los kann über die eigene Seite bearbeitet werden, ungültige Eingaben werden mit Meldung abgelehnt, und die Änderung ist im Admin sichtbar.
