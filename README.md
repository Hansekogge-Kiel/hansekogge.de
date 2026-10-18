# hansekogge.de
Webseite der Kieler Hanse Kogge

## Entwicklung

- Seite bauen: `cd src && bundle install && bundle exec jekyll serve`
- Entwurfs-Banner abschalten: in `src/_config.yml` `draft_banner: false`
- Termine aktualisieren: `pip install icalendar recurring-ical-events pyyaml` und `python3 tools/update_termine.py` (liest die öffentlichen Google-Kalender, schreibt `src/_data/termine.yml`); danach committen. Ob ein Termin als „kommend" oder „Rückblick" erscheint, entscheidet das Datum beim Bauen der Seite.
- Download-Dateien (Preisliste, Aufnahmeantrag): `src/assets/downloads/`
