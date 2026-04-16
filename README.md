# V4Pro

Repo inițializat pentru BetAnalytics Pro V4.

Conține:
- structură GitHub Pages
- workflow pentru refresh automat la 15 minute
- workflow keep-alive
- fișiere JSON placeholder pentru prima pornire

## Ce mai trebuie
1. Adaugă în repo secretul `BSD_TOKEN`
2. Rulează workflow-ul **Fetch BetAnalytics Data** o dată din Actions
3. Activează GitHub Pages din branch `main`, folder `/ (root)`

După primul run, fișierele din `data/` vor fi populate automat.
