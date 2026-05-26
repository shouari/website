# Suivi RMA — Gestion des retours produits

**Stack :** Python · Streamlit · PostgreSQL · Brevo API · Plotly
**Statut :** Déployé — approbation déploiement client en cours

---

## Le constat de départ

Dans l'intégration AV haut de gamme, les retours produits existent.
Amplificateurs défectueux, modules à remplacer, équipements sous garantie.

Ce qu'on avait pour les gérer : des emails et un fichier Excel.

Aucune traçabilité du cycle complet. Pas de statuts définis.
Pas de relance automatique quand un dossier dormait depuis 10 jours.
Pas d'historique des actions effectuées. Pas de procédure documentée.
Quand quelqu'un quittait l'équipe, la mémoire du dossier partait avec lui.

En regardant comment les grands fabricants traitent leurs propres RMA —
des processus qui se règlent en quelques heures —
puis en regardant notre façon de faire, le contraste était saisissant.

Ce n'était pas un problème de volume. C'était un problème de structure.

## Ce que j'ai construit

J'ai d'abord rédigé la procédure dans un document Word
et modélisé le flux dans Camunda BPMN — clarifier avant d'outiller.
Puis j'ai transformé cette procédure en application.

L'App RMA génère automatiquement un identifiant unique pour chaque dossier
(`RMA-ANNÉE-XXXX`), structure le cycle complet à travers des statuts définis :
*À soumettre → Soumis → En attente → Équipement renvoyé → Fermé.*

Chaque transition déclenche une notification email automatique via Brevo
aux parties prenantes concernées — technicien, coordination, comptabilité
— selon le statut atteint.

Un système de relances périodiques surveille les dossiers qui stagnent :
2 jours sans mouvement sur un dossier "À soumettre",
7 jours sur un dossier "Soumis",
3 jours sur un dossier "En attente" —
et envoie une relance automatique sans intervention humaine.

Chaque action sur un dossier est journalisée avec horodatage.
Les pièces jointes (photos, documents fabricant) sont stockées en base.
Un tableau de bord analytique donne la vue d'ensemble en temps réel.

## Ce que ça change

Un dossier RMA ne peut plus tomber dans les mailles du filet.
La procédure est dans l'outil — pas dans la tête de quelqu'un.
Les relances partent seules. Les escalades sont visibles.
Et quand l'équipe change, l'historique reste.
