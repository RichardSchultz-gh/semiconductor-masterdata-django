# Frau Holle in Django – Nachbau der Los-Stammdatenseite

Nachbau der Seite „Stammdaten → Los“ aus dem HTW-Teamprojekt **Frau Holle** in Django. Im Original war die Anwendung mit Flask und SQLAlchemy umgesetzt. Ziel ist der direkte Vergleich: dieselbe Funktion, einmal so, wie ich sie im Teamprojekt selbst geschrieben habe, und einmal mit den Werkzeugen, die Django dafür mitbringt.

## Hintergrund

Frau Holle war ein Teamprojekt in den Modulen *Software Engineering I & II* an der HTW Dresden: ein Produktionssteuerungssystem für eine fiktive Halbleiterfabrik, entwickelt nach OpenUP mit einem simulierten Auftraggeber. In der Fabrik werden Silizium-Scheiben zu **Losen** zusammengefasst, die nacheinander die Produktionsschritte durchlaufen.

Ich war im Team für **UC04 „Stammdaten anzeigen“** und **UC05 „Stammdaten bearbeiten“** verantwortlich, also genau für die Seite, die hier nachgebaut wird.

- Original (mein Fork): [RichardSchultz-gh/semiconductor-logistics-automation1](https://github.com/RichardSchultz-gh/semiconductor-logistics-automation1)
- Relevante Stellen im Original: `src/mapper.py` (Model), `src/Stammdaten.py` (View), `src/templates/Stammdaten_Los.html` (Template)

## Flask-Original und Django-Nachbau im Vergleich

| Flask-Original | Django-Nachbau |
|---|---|
| 13 einzelne `if` + `update()` pro Attribut, dazu zwei Hilfsfunktionen zum Aufbereiten der Eingaben (`Stammdaten.py:46–95`, `126–139`, zusammen ca. 64 Zeilen) | Eine `ModelForm` (`lots/forms.py`), fast nur Feldliste und Widgets, und eine View mit 12 Zeilen (`lots/views.py`) |
| Keine Prüfung der Eingaben: Jeder Wert geht an die Datenbank. Datenbankfehler führen auf eine allgemeine Fehlerseite, ein falsches Zeitformat zu einem unbehandelten Fehler. Die Eingaben sind danach weg. | Die Form prüft jedes Feld anhand des Models. Bei ungültigen Werten bleibt man auf der Seite, sieht die Meldung am Feld, behält seine Eingaben, und es wird nichts gespeichert. |
| Bearbeiten per GET: Die Änderungen stehen in der URL und verändern beim Aufruf die Datenbank | Bearbeiten per POST mit CSRF-Token, danach Weiterleitung (Post/Redirect/Get) |
| Gültige Zustände doppelt im Template als Datalist gepflegt | `Lot.State` als `TextChoices` im Model, an einer Stelle; die Form baut daraus die Auswahlliste |
| Zeitstempel von Hand mit `strptime`/`strftime` umgewandelt | Django parst die Eingaben selbst; Zeitstempel werden zeitzonenbewusst gespeichert (`Europe/Berlin`) |
| Rollen über feste Benutzernamen, Bearbeitungsformular nur per JavaScript ausgeblendet | *geplant:* Gruppen und Rechte, serverseitig geprüft |
| Filter mit vier Verzweigungen für die Kombinationen aus Lot-ID und State | *geplant:* ein QuerySet, das schrittweise eingeschränkt wird |

### Warum POST statt GET

GET ist zum Abrufen von Daten gedacht und soll laut HTTP nichts verändern. Browser dürfen GET-Anfragen deshalb vorab laden oder wiederholen, und die Parameter landen im Verlauf, in Lesezeichen und in Server-Logs. Daten, die etwas ändern, gehören in einen POST. Nur dort greift auch Djangos CSRF-Schutz, der verhindert, dass eine fremde Seite im Namen eines angemeldeten Benutzers ein Formular abschickt.

### CSV-Import

Die 1000 Beispiellose aus dem Original werden per Management-Command importiert (`lots/management/commands/import_lots.py`). Der Import nutzt `update_or_create` und lässt sich beliebig oft ausführen, ohne Duplikate zu erzeugen. Die Zeitstempel in der CSV haben keine Zeitzone; der Import legt sie ausdrücklich als Berliner Zeit fest (`make_aware`), statt das Django stillschweigend zu überlassen.

## Stand

- [x] Model `Lot`, Admin, CSV-Import
- [x] Bearbeiten-Seite mit ModelForm (`/lots/<lotid>/edit/`)
- [ ] Losliste mit Filter nach Lot-ID und State
- [ ] Rollen „Mitarbeiter“ (nur ansehen) und „Fertigungsleiter“ (bearbeiten)
- [ ] Automatische Tests

Die Planung liegt in [`prd/`](prd/) und [`issues/`](issues/).

## Installation und Start

Voraussetzungen: Python 3.14 und [uv](https://docs.astral.sh/uv/). Alle Befehle im Repo-Root ausführen.

```bash
git clone https://github.com/RichardSchultz-gh/frauholle-django.git
cd frauholle-django

uv venv
uv pip install -r requirements.txt

uv run src/manage.py migrate
uv run src/manage.py import_lots src/lots/testdata/LOT.csv
uv run src/manage.py createsuperuser
uv run src/manage.py runserver
```

Danach:

- Bearbeiten-Seite: <http://127.0.0.1:8000/lots/AP15-0/edit/>
- Admin: <http://127.0.0.1:8000/admin/>

Der `SECRET_KEY` in `src/mysite/settings.py` ist der von Django erzeugte Entwicklungsschlüssel. Das Projekt ist nur für den lokalen Betrieb gedacht; für einen echten Einsatz müsste der Schlüssel aus einer Umgebungsvariable kommen und `DEBUG` ausgeschaltet sein.

## Technik

Python 3.14, Django 6.1, SQLite

## Einsatz von KI

Das Projekt ist ein Lernprojekt: Ich wollte Django nicht nur benutzen, sondern verstehen. Deshalb habe ich mit [Claude Code](https://claude.com/claude-code) so gearbeitet:

- **Selbst geschrieben:** der Code in `src/lots/` (Model, Admin, Import-Command, Form, View, URLs, Template)
- **Mit Claude:** Claude hat mir jedes neue Konzept an einem allgemeinen Beispiel erklärt, das ich dann auf mein Projekt übertragen habe, und meinen Code nach jedem Schritt reviewt. Dabei sind zum Beispiel Fehler im Umgang mit Zeitzonen und das falsche Datumsformat in den Eingabefeldern aufgefallen.
- **Von Claude geschrieben:** die Planung in `prd/` und `issues/` (nach meinen Vorgaben) und dieses README. Commits, an denen Claude beteiligt war, sind mit `Co-Authored-By` gekennzeichnet.
