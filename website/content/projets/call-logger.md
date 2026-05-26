# Qualification d'appel SAV

**Stack :** Python · Streamlit · OpenStreetMap · Intégration 3CX
**Statut :** En production — usage quotidien

---

## Le constat de départ

Plusieurs personnes prenaient les appels entrants.
Chacun notait ce qu'il jugeait pertinent, dans l'ordre qui lui convenait.
Résultat : des tickets ouverts dans le logiciel de gestion de service
avec des informations à géométrie variable — parfois complètes,
souvent partielles, rarement comparables entre elles.

En recevant un appel, je me suis posé une question simple :
**quelles sont les informations que je cherche intuitivement,
même sans formulaire, dans les premières 90 secondes d'un appel ?**

Le nom du client. Le contact sur place. Le système en cause.
Depuis quand le problème existe. Ce que le client a déjà tenté.
L'accès sur place. La priorité.

Ces questions, je les posais toujours. Mais pas mes collègues.
Pas de la même façon. Pas dans le même ordre.

## Ce que j'ai construit

Une application qui s'ouvre automatiquement dans le navigateur
dès qu'un appel entre sur le système téléphonique 3CX —
avec le numéro et le nom du client déjà pré-remplis dans les champs.

Le formulaire suit exactement la logique d'un appel réel :
identification du client, problème signalé, systèmes concernés
(réseau, audio, vidéo, contrôle d'accès, alarme, éclairage...),
durée du problème, tentatives déjà faites, conditions d'accès, priorité.

Une barre de progression indique en temps réel le taux de complétion de la fiche.
L'adresse est géolocalisée automatiquement via OpenStreetMap
pour calculer la zone de facturation sans intervention manuelle.

En fin de saisie, un résumé structuré est généré en un clic —
formaté exactement comme les tickets attendus dans le logiciel de gestion,
prêt à coller sans réécriture.

## Ce que ça change

Avant : chaque ticket était une surprise.
Après : tous les tickets ont la même structure, les mêmes champs,
le même niveau d'information — peu importe qui a pris l'appel.

La standardisation n'était pas une contrainte imposée.
C'était juste les bonnes questions, dans le bon ordre,
avec un outil qui ne ralentit pas — il guide.
