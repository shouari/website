# Préparateur d'intervention

**Stack :** Python · Streamlit · OpenAI API · Brevo · API interne
**Statut :** En production — 12 techniciens, dispatch automatique quotidien

---

## Le constat de départ

Avant d'envoyer un technicien sur le terrain, je faisais toujours la même chose :
la veille ou l'avant-veille, je lui transmettais le contexte.
Ce que le client avait signalé. Ce que j'avais tenté à distance.
Mes hypothèses sur la cause probable. Ce qu'il faudrait apporter.

C'était utile. Mais c'était informel.
Certains techniciens préféraient un appel téléphonique.
D'autres un message Teams. D'autres un courriel.
Pas de format standard. Pas d'heure fixe. Pas de garantie que l'information
était complète ou que le technicien l'avait reçue avant de partir.

Et pour les interventions complexes — systèmes QSC, Crestron, Unifi,
Control4, Lutron — la préparation pouvait facilement prendre une à deux heures.
Aller chercher la documentation du système, reconstituer l'historique client,
formuler les hypothèses techniques. Du temps de coordination
que j'ai cherché à réduire sans sacrifier la qualité.

## Ce que j'ai construit

Une application de préparation d'intervention structurée en trois étapes.

**Étape 1 — Saisie du contexte**
Les informations de l'appel de service : client, technicien assigné,
systèmes concernés (13 options couvrant l'ensemble du parc),
problème signalé, tentatives déjà effectuées, notes terrain.

**Étape 2 — Génération IA**
Un moteur IA — configuré spécifiquement pour le contexte AV/domotique/réseaux
et la réalité terrain des techniciens expérimentés —
produit un plan d'intervention structuré :
analyse technique, hypothèses priorisées, étapes recommandées,
commandes CLI ou chemins de configuration précis selon le système,
questions à valider sur place.

La piste suggérée par le technicien dans ses notes prime toujours
sur l'analyse générale. L'IA travaille pour lui, pas à sa place.

**Étape 3 — Dispatch automatique**
Le courriel de préparation part automatiquement à 16h30 la veille
de chaque intervention planifiée — pour tous les techniciens concernés.
Si des changements surviennent après l'envoi initial,
un second courriel différentiel est envoyé automatiquement.

En parallèle, une intégration avec l'API interne du logiciel de gestion
récupère chaque matin les interventions planifiées pour le lendemain
et les charge directement dans l'application —
il ne reste plus qu'à valider les informations et lancer la préparation.

## Ce que ça change

La préparation d'un appel de service complexe est passée
d'une heure ou deux de travail manuel à quelques minutes.
12 techniciens reçoivent leur brief la veille, au même format,
à la même heure, sans que j'aie à m'en souvenir.

Et depuis que c'est en place, je prépare des appels
une semaine à l'avance quand le calendrier le permet.
Le technicien arrive avec le contexte complet.
Pas avec la moitié.
