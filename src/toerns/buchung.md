---
layout: page
title: Buchungsanfrage
section: Gäste
menu: /toerns/
lead: Schreiben Sie uns – die Geschäftsstelle meldet sich bei Ihnen.
---

Telefonisch erreichen Sie uns unter **+49 431 2190250**, per E-Mail unter [buero@hansekogge.de](mailto:buero@hansekogge.de).

<form class="booking" action="mailto:buero@hansekogge.de" method="post" enctype="text/plain">
  <div class="row">
    <label>Name<input name="name" required></label>
    <label>E-Mail<input type="email" name="email" required></label>
  </div>
  <div class="row">
    <label>Gewünschter Törn
      <select name="toern"><option>Charter</option><option>Einzelbucher</option><option>Event / Stegveranstaltung</option><option>Sommertörn</option></select>
    </label>
    <label>Personenzahl<input type="number" min="1" name="personen"></label>
  </div>
  <label>Telefon (optional)<input type="tel" name="telefon"></label>
  <label>Nachricht (optional)<textarea name="nachricht" rows="5"></textarea></label>
  <button class="btn btn-gold" type="submit">Anfrage senden</button>
</form>

<p class="note">Entwurf: Das Formular öffnet bislang nur das Mailprogramm. Für den Live-Betrieb braucht es einen Formular-Dienst.</p>
