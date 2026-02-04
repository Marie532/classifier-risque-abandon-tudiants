README pour le Projet 1 avec Visualisation
# Prédire le salaire en fonction de variables RH

## Objectif

Ce projet utilise le machine learning pour prédire le salaire d'un salarié en fonction de plusieurs variables RH (expérience, niveau d'études, poste, localisation, etc.). Il met en œuvre un modèle XGBoost, qui est particulièrement performant pour les tâches de régression.

## Données

Le dataset `hr_salaries.csv` contient les colonnes suivantes :

- `age` : âge du salarié
- `experience_years` : années d'expérience
- `education_level` : niveau d'études (Licence, Master, Doctorat…)
- `job_title` : intitulé de poste
- `location` : localisation géographique
- `salary` : salaire annuel à prédire

## Méthodologie

1. **Exploration des données** : Inspection du dataset, vérification des valeurs manquantes et des distributions.
2. **Préparation des données** :
   - Séparation des variables explicatives de la variable cible.
   - Encodage des variables catégorielles.
   - Séparation en jeux d'entraînement et de test.
3. **Modélisation** :
   - Utilisation du modèle **XGBoost** pour la régression.
4. **Évaluation** :
   - Calcul du MAE (Mean Absolute Error) et du R².
5. **Visualisation** :
   - Nuage de points comparant les salaires réels aux salaires prédits par le modèle.

## Résultats

Les métriques clés sont :

- **MAE** : erreur moyenne entre le salaire réel et prédit.
- **R²** : proportion de la variance du salaire expliquée par le modèle.

Une visualisation `salary_real_vs_pred_xgboost.png` montre la comparaison entre les salaires réels et les salaires prédits.

## Visualisations

- `salary_real_vs_pred_xgboost.png` : nuage de points montrant la relation entre les salaires réels et les salaires prédits par le modèle XGBoost.

## Compétences mises en avant

- Manipulation de données avec **pandas**
- Prétraitement des variables numériques et catégorielles
- Utilisation de **XGBoost** pour la régression
- Visualisation des résultats avec **seaborn** et **matplotlib**
- Interprétation des métriques de performance (MAE, R²)

## Sites web pour visualisation des données

- [Plotly](https://plotly.com/)
- [Tableau](https://www.tableau.com/)
- [Power BI](https://powerbi.microsoft.com/)
- [Google Data Studio](https://datastudio.google.com/)