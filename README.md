# Novembre à deux

Appli Android (Capacitor) du planning surprise de novembre : Chloé voit le programme du jour et tire ses cartes, Joh gère tout depuis son espace (code requis).

- La page est dans `src/page.html`. `tools/build_app.py` la transforme en `www/index.html` (polices hors ligne).
- À chaque push sur `main`, GitHub Actions compile l'APK et le publie dans les *Releases* (`novembre-a-deux.apk`).
- Notifications locales programmées sur le téléphone (plugin `@capacitor/local-notifications`), recalculées à chaque modification du programme.
