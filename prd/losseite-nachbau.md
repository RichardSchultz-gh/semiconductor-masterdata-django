# PRD: Nachbau der Frau-Holle-Losseite in Django

## Ziel

Die Stammdaten-Losseite aus dem HTW-Teamprojekt „Frau Holle“ (Flask + SQLAlchemy) wird in Django nachgebaut. Das Repo dient als Arbeitsprobe für die Bewerbung bei descript GmbH (Werkstudent Backend Django/Python).

Abgabe: **Montag, 09.11.2026**. Danach wird der letzte Satz von Absatz 2 im Anschreiben (`~/Bewerbung/descript/Anschreiben_Richard_Schultz.tex`) durch das tatsächlich Erlebte ersetzt und der Repo-Link ins Portalfeld „Arbeitsproben“ gesetzt.

## Warum

descript schreibt: „Zeig uns, dass du Django und Python nicht nur kennst, sondern nutzen willst.“ Django ist die größte Lücke im Profil. Der Nachbau zeigt den direkten Vergleich zu Code, den ich selbst geschrieben habe.

## Vorbild (Flask-Original)

Repo `~/semiconductor-logistics-automation`:

| Datei | Inhalt |
|---|---|
| `src/mapper.py:20` | SQLAlchemy-Klasse `Lot` |
| `src/Stammdaten.py:32–124` | View: Rollenprüfung, Bearbeiten, Filter |
| `src/templates/Stammdaten_Los.html` | Tabelle, Filterformular, Bearbeitungsformular, JS-Sortierung |
| `docs/development/DB_Tabellen_erstellen/CSV-Data/LOT.csv` | 1000 Beispiellose |
| `docs/requirements/glossary.adoc` | Bedeutung der Los-Zustände |
| `docs/test/Bugtracker.adoc:34` | Anmerkung Auftraggeber zur Validierung der Zustände |

## Was der Nachbau besser machen soll

| Flask-Original | Django-Nachbau |
|---|---|
| 13 einzelne `if` + `update()` pro Attribut (`Stammdaten.py:51–91`) | ModelForm |
| `get_args_right`, Timestamp-Parsing von Hand | Formular-Validierung von Django |
| Bearbeiten per GET | POST mit CSRF-Schutz |
| States doppelt als Datalist im Template | `TextChoices` im Model, eine Stelle |
| Rollen über festen Benutzernamen `user1`/`user2`, Formular per JS ausgeblendet | Gruppen und Rechte, serverseitig geprüft |
| Filter mit vier Verzweigungen (`Stammdaten.py:109–116`) | QuerySet, Filter nacheinander angewendet |
| Datenbank akzeptiert jeden State | `choices`, optional DB-Constraints und `clean()` |

## Aufteilung

1. [Model und CSV-Import](../issues/01-model-und-import.md)
2. [ModelForm und View zum Bearbeiten](../issues/02-modelform-und-view.md)
3. [Template, Liste und Filter](../issues/03-template-und-filter.md)
4. [Rollen und Rechte](../issues/04-rollen.md)
5. [README, Veröffentlichung, Anschreiben](../issues/05-readme-und-veroeffentlichen.md)

Priorität bei Zeitmangel: Teil 2 ist am wichtigsten, weil genau das im Anschreiben steht. Teil 3 und 4 dürfen schlanker ausfallen. Ein kleines, sauberes Repo ist besser als ein großes, halb fertiges.

## Rahmen

- Python 3.14, Django 6.1, SQLite
- Projekt in `src/mysite`, App `src/lots`
- Virtuelle Umgebung `.venv` im Repo-Root, nutzbar mit `uv run`
- Lernprojekt: Code selbst schreiben, Claude erklärt Grundlagen und reviewt
