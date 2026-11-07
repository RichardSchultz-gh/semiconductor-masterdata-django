# 04 Rollen und Rechte

PRD: [losseite-nachbau](../prd/losseite-nachbau.md) · Abhängig von: [02](02-modelform-und-view.md), [03](03-template-und-filter.md)

## Ziel

Mitarbeiter dürfen Lose nur ansehen, Fertigungsleiter dürfen sie bearbeiten (Frau Holle UC04/UC05). Im Original wurde das über feste Benutzernamen geprüft (`Stammdaten.py:18–22`) und das Bearbeitungsformular nur per JavaScript ausgeblendet (`Stammdaten_Los.html:243`). Im Nachbau prüft der Server.

## Checkliste

- [ ] Gruppen „Fertigungsleiter“ und „Mitarbeiter“ anlegen und die passenden Model-Rechte zuordnen (`view_lot`, `change_lot`)
- [ ] Je einen Testbenutzer pro Gruppe
- [ ] Login und Logout für die eigene Losseite (Djangos Auth-Views)
- [ ] Liste nur für angemeldete Benutzer mit Leserecht
- [ ] Bearbeiten-View prüft das Änderungsrecht serverseitig
- [ ] Im Template den Bearbeiten-Link nur bei passendem Recht anzeigen
- [ ] Testen: Mitarbeiter ruft die Bearbeiten-URL direkt auf → abgelehnt
- [ ] Optional: Gruppen per Data-Migration anlegen, damit sie nicht von Hand angelegt werden müssen
- [ ] Commit

## Fertig, wenn

Ein Mitarbeiter sieht die Liste, aber keinen Bearbeiten-Link, und wird auch beim direkten Aufruf der URL abgewiesen. Ein Fertigungsleiter kann bearbeiten.
