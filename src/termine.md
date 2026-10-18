---
layout: page
title: Termine
lead: Gästefahrten, Törns und Vereinsveranstaltungen.
---

{% assign heute = site.time | date: "%Y-%m-%d" %}
{% assign kommend = site.data.termine | where_exp: "e", "e.start >= heute or e.end >= heute" %}
{% assign vergangen = site.data.termine | where_exp: "e", "e.start < heute and e.end < heute" %}

<ul class="legend">
  <li><span class="tag gruen">grün</span> weitere Gäste willkommen</li>
  <li><span class="tag rot">rot</span> keine Gästeplätze mehr frei</li>
  <li><span class="tag blau">blau</span> vereinsintern</li>
</ul>

## Kommende Termine

{% if kommend.size > 0 %}
{% include termine-list.html events=kommend group=true %}
{% else %}
Zurzeit sind keine weiteren Termine eingetragen.
{% endif %}

<p class="note">Die Termine der Saison 2027 werden nach der Jahresplanung ergänzt. Wer rechtzeitig informiert werden möchte, <a href="mailto:newsletter1380@hansekogge.de?subject=Newsletter-Anmeldung">fragt den Newsletter an</a>. Charter und weitere Termine sind nach Absprache möglich. Alle Angaben ohne Gewähr.</p>

{% if vergangen.size > 0 %}
<details class="archive past">
<summary>Rückblick: Saison {{ site.time | date: "%Y" }} ({{ vergangen.size }} Termine)</summary>
{% include termine-list.html events=vergangen group=true %}
</details>
{% endif %}

<p>Eine Fahrt buchen? <a class="btn btn-gold" href="{{ '/toerns/buchung/' | relative_url }}">Buchungsanfrage stellen</a></p>
