# Documentation du Projet : Réduction d'Étoiles

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zP0O23M7)

## Auteurs

* **TEITEN Thomas**
* **DUSSAUTOIS Tom**
* **REGNAULT Alex**

---

## Présentation du projet

Ce projet vise à développer une application de traitement d'images astronomiques (fichiers FITS) permettant de réduire la taille des étoiles sans altérer les objets du ciel profond (nébuleuses, galaxies). L'application utilise une architecture MVC (Modèle, Vue, Contrôleur) avec une interface graphique développée avec Qt Creator.

### Méthode choisie (Phase 2 : Masquage Adaptatif)


1.  **Création du masque** : Utilisation de cv2.adaptiveThreshold pour isoler les étoiles du fond du ciel, même en présence de luminosité.

2.  **Traitement du masque** : Application d'une érosion sur le masque pour réduire la taille des étoiles.

3.  **Fusion** : L'image finale est une composition : les zones hors masque conservent l'image originale (fond de ciel intact), alors que les zones sous le masque affichent l'image érodée.

### Difficultés rencontrées

* **Initiation de Qt Creator** : Nous avons du apprendre à utiliser l'outil Qt Creator afin d'aller plus vite.
* **Synchronisation Git** : Gestion des conflits lors des merges et rebases pour maintenir un historique propre.
* **Gestion de la couleur** : Passage de RGB à BGR car OpenCV utilise du BGR.

---

## Installation

**Lancer le programme** : python mainwindow.py

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate