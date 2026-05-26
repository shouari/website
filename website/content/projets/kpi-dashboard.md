# Dashboard KPI SAV

**Stack :** Python · Streamlit · Pandas · Plotly · OpenAI API
**Statut :** En production — rapport mensuel, historique 2 ans

---

## Le constat de départ

Je suis coordonnateur de service.
Officiellement, analyser la performance du département n'est pas dans ma fiche de poste.

Mais les données étaient là — dans le logiciel de gestion de service,
accessibles via API. Des centaines d'appels. Des milliers de transactions.
Deux ans d'historique opérationnel que personne ne lisait.

Aucun tableau de bord. Aucun KPI défini. Aucune visibilité
sur ce qui prenait du temps, ce qui coûtait de l'argent,
ce qui méritait d'être amélioré en priorité.

On gérait bien — mais à l'intuition.

## Ce que j'ai construit

J'ai commencé par extraire les données via API,
les triturer avec Python et Pandas,
et en sortir une première lecture : volumes, revenus, délais, gratuité.

Puis j'ai cherché ce que ces chiffres racontaient vraiment.

Cycle moyen de traitement. Taux de gratuité par client.
Coût caché du service non facturé. Distribution de charge par technicien.
Saisonnalité du volume. Clients à risque.

J'ai présenté l'analyse à ma responsable avec une proposition :
4 à 5 indicateurs clés pour piloter le département.
Ces KPI ont été validés et sont suivis depuis.

Le processus mensuel est maintenant automatisé :
un script agrège les nouvelles données avec l'historique existant,
une classification IA enrichit les appels de service
(système, type de problème, marque) pour affiner l'analyse,
et le dashboard produit un rapport complet en quelques minutes.

Résumé exécutif généré automatiquement. Comparaison mois précédent,
même mois l'an passé, tendance 12 mois glissants.
Détection automatique des anomalies et des clients à fort taux de gratuité.

## Ce que ça change

En 2025, le cycle moyen de traitement d'un appel de service était de 35,8 jours.
En 2026, il est à 5,9 jours.

Ce n'est pas le dashboard qui a réduit ce chiffre.
C'est ce que le dashboard a rendu possible : voir le problème,
le mesurer, décider d'agir, et suivre l'effet des décisions.

Des données qui existent et que personne ne lit,
c'est du potentiel qui dort.
