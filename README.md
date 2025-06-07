# Dessineur automatique pour Gartic Phone

Ce projet est un **script Python** qui utilise la bibliothèque [`pynput`](https://pynput.readthedocs.io/en/latest/) pour **contrôler automatiquement la souris** afin de simuler des clics et des déplacements sur l’écran.

Il est spécialement conçu pour aider à dessiner des formes ou sélectionner des couleurs dans le jeu **Gartic Phone**.

---

## Fonctionnalités

- Déplace la souris vers des positions prédéfinies correspondant à des couleurs.
- Effectue des clics pour sélectionner ces couleurs.
- Simule des clics supplémentaires à des coordonnées fixes.
- Gère des délais entre les actions pour respecter le rythme du jeu.

---

## Technologies utilisées

- **Python 3.x**
- **pynput** : pour contrôler la souris (déplacement, clics)

---

## Prérequis

- Python installé (version 3.x recommandée)
- Installer pynput via pip :

```bash
pip install pynput
