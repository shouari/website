# Interfaces de contrôle AV — Q-SYS

**Stack :** HTML · JavaScript · QSC Q-SYS · Protocole QRC · Fetch API
**Statut :** Bêta fonctionnelle — déploiement en cours

---

## Le point de départ

Lors d'un projet d'intégration pour un espace événementiel,
notre équipe discutait de comment fournir au client
une interface de contrôle simple pour piloter l'ambiance du lieu —
éclairage, audio, sources vidéo — sans avoir besoin d'un technicien.

Un collègue mentionnait qu'il allait utiliser l'éditeur UCI natif de Q-SYS,
mais que pour chaque nouveau projet, il faudrait reprendre le travail
from scratch. Chaque client, une nouvelle interface.
Chaque interface, des heures de développement.

La question que je me suis posée : est-ce qu'on peut industrialiser ça ?

## Ce que j'ai découvert

En explorant la documentation Q-SYS,
j'ai trouvé le protocole QRC — Q-SYS Remote Control.
Une API native qui permet de piloter n'importe quel composant Q-SYS
depuis n'importe quel navigateur web, en JSON via WebSocket.

Pas d'application à installer. Pas de dépendance externe.
Un simple fichier HTML, et on peut lire et écrire
n'importe quel contrôle du système en temps réel.

## Ce que j'ai construit

Trois interfaces HTML standalone, chacune adaptée à un profil d'utilisateur :

**Interface principale** — vue administrative globale.
Contrôle maître de toutes les zones, sélecteur de scènes,
statuts temps réel de chaque espace.
Pensée pour l'opérateur technique qui supervise l'ensemble.

**Interface lounge** — contrôle tactile simplifié.
Ambiance, éclairage, musique.
Pensée pour le personnel de salle qui n'a pas besoin de tout voir —
juste de ce qui change l'atmosphère.

**Interface salle de réunion** — autonomie complète.
Mode présentation, mode visioconférence, gestion des stores,
minuterie de réservation.
Pensée pour l'utilisateur final qui gère sa salle seul.

Les trois interfaces communiquent en temps réel avec le moteur Q-SYS
via fetch automatique. Elles fonctionnent hors-ligne sur tablette.
Zéro dépendance, zéro serveur intermédiaire, zéro installation.

## L'objectif à terme

Un framework de templates réutilisables.
Sur le prochain projet Q-SYS, on part d'une base existante —
on ajuste les boutons, les zones, les noms —
au lieu de recommencer de zéro.

Moins de temps de développement par projet.
Plus de cohérence entre les installations.
Une valeur ajoutée qui se capitalise d'un client à l'autre.
