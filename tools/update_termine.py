#!/usr/bin/env python3
"""Liest die öffentlichen Google-Kalender der Hansekogge und schreibt src/_data/termine.yml.

Benötigt: pip install icalendar recurring-ical-events pyyaml
Aufruf:   python3 tools/update_termine.py
Danach neu bauen/committen. Kalender-IDs und Status-Zuordnung stehen unten.
"""
import datetime as dt
import urllib.parse
import urllib.request
import zoneinfo
from pathlib import Path

import icalendar
import recurring_ical_events
import yaml

CALENDARS = [
    ("13kalender80@hansekogge.de", "intern"),                          # Termine der Kieler Hansekogge
    ("jsnc6bjk0h5tc0vver671v5uto@group.calendar.google.com", "frei"),  # Plätze sind noch frei
    ("s53auiim32fam6mlbcep7o1g8k@group.calendar.google.com", "voll"),  # Ausgebucht
]
MONTHS_AHEAD = 14
BERLIN = zoneinfo.ZoneInfo("Europe/Berlin")
OUT = Path(__file__).resolve().parent.parent / "src" / "_data" / "termine.yml"


def fetch(cal_id):
    url = f"https://calendar.google.com/calendar/ical/{urllib.parse.quote(cal_id)}/public/basic.ics"
    with urllib.request.urlopen(url, timeout=30) as r:
        return icalendar.Calendar.from_ical(r.read())


def main():
    today = dt.date.today()
    begin = dt.date(today.year, 1, 1)  # laufendes Jahr als Rückblick
    end = today + dt.timedelta(days=30 * MONTHS_AHEAD)
    rows = {}
    for cal_id, status in CALENDARS:
        for ev in recurring_ical_events.of(fetch(cal_id)).between(begin, end):
            start, stop = ev["DTSTART"].dt, ev.get("DTEND").dt if ev.get("DTEND") else None
            allday = not isinstance(start, dt.datetime)
            if allday:
                last = (stop - dt.timedelta(days=1)) if stop else start
                time = ""
            else:
                last = (stop.astimezone(BERLIN) if stop.tzinfo else stop).date() if stop else start.date()
                local = start.astimezone(BERLIN) if start.tzinfo else start
                time = local.strftime("%H:%M")
                start = local
                start = start.date()
            title = str(ev.get("SUMMARY", "")).strip()
            key = (start, title.lower())
            rows[key] = {
                "start": start.isoformat(),
                "end": last.isoformat() if last > start else "",
                "time": time,
                "title": title,
                "status": status,
                "location": str(ev.get("LOCATION", "")).split(",")[0].strip(),
            }
    data = [rows[k] for k in sorted(rows)]
    OUT.write_text("# Erzeugt von tools/update_termine.py – nicht von Hand bearbeiten\n"
                   + yaml.safe_dump(data, allow_unicode=True, sort_keys=False))
    print(f"{len(data)} Termine -> {OUT}")


if __name__ == "__main__":
    main()
