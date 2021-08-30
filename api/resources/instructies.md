# Malmberg

## Inlezen data TL;DR

### Stap 1

Voorbeeld voor het inlezen van de data in productie. De its-tools cli zal om een
wachtwoord vragen. Voor productie staat het wachtwoord in bitwarden.

```sh
its-tools import csv malmberg data.csv users.csv \
 --username admin@itslanguage.nl \
 --api-url https://api.itslanguage.io \
 --ws-url wss://itslanguage.io
```

Korte uitleg:

- `import` stuurt het importeer commando van de cli aan.
- `csv` geeft aan dat het om csv data gaat, dus twee bestanden!
- `malmberg` is de tenant waarvoor de data ingelezen moet worden.
- `data.csv` bevat de thema, week en opdracht data voor tuto
- `users.csv` bevat de organisaties, gebruikers en groepen voor tuto

Let op: de tenant, `malmberg` in dit geval, moet bestaan voordat het commando
aangeroepen wordt!

Met --password kan het wachtwoord nog meegegeven worden aan het commando maar
dat is voor productie niet aan te bevelen.

Gebruik `its-tools import csv --help` voor meer hulp over het commando.

### Stap 2

De tweede stap bij het voorbereiden van de data is om ook opdrachten voor te
bereiden met de `prepare` functie. Dit zorgt er onder andere voor dat alle wfst
bestanden aangemaakt worden. Voor iedere gebruiker die mogelijk het inladen van
een ander model verzorgt moet dit gedaan worden. Voor Malmberg geldt dat dus
voor een kind gebruiker gedaan moet worden en voor een volwassenen.

Gebruik voor een kind de gebruiker `student9` en voor een volwassenen `adult1`.
Deze gebruikers hebben toegang tot alle benodigde opdrachten.

De commandos.

```sh
its-tools prepare feedback malmberg trial student9 \
 --username admin@itslanguage.nl \
 --api-url https://api.itslanguage.io \
 --ws-url wss://itslanguage.io

its-tools prepare feedback malmberg trial adult1 \
 --username admin@itslanguage.nl \
 --api-url https://api.itslanguage.io \
 --ws-url wss://itslanguage.io
```

Korte uitleg:

- `prepare` stuurt aan dat de cli verbinding gaat maken met de websocket server
  om daar `nl.itslanguage.feedback.prepare` aan te kunnen roepen.
- `feedback` zorgt ervoor dat het specifiek om feedback gaat. De functionaliteit
  zoals beschreven hiervoor is in deze stap geïmplementeerd.
- `malmberg` is de tenant waar de data voor voorbereid moet worden.
- `trial` een organisatie om data bij op te halen.
- `student9` een gebruiker om de data mee voor te bereiden.
- `adult1` een gebruiker om de data mee voor te bereiden.

Met --password kan het wachtwoord nog meegegeven worden aan het commando maar
dat is voor productie niet aan te bevelen.

Gebruik `its-tools prepare feedback --help` voor meer hulp over het commando.

## Data

In de map `Lijn 3` en `Station Zuid` staat de meest actuele data die gebruikt
wordt voor het inlezen. De mappen structuur dient voor alle csv import bronnen
gelijk te zijn want dit is wat de cli verwacht.
