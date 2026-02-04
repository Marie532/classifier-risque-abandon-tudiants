# classifier-risque-abandon-tudiants
Classifier des élèves selon leur risque d’abandon scolaire
Objectif

Ce projet vise à prédire le risque d'abandon scolaire d'un élève à partir de différentes variables académiques et socio-éducatives. L'idée est d’identifier les élèves les plus à risque afin de mettre en place des actions préventives et de les aider à rester dans le système scolaire. Le modèle utilisé pour cette tâche est un classificateur LightGBM, une méthode de machine learning efficace pour traiter des données complexes et déséquilibrées.

Données

Le dataset utilisé pour ce projet est fictif, mais représente des données typiques qu'un service scolarité pourrait collecter sur les élèves. Le fichier students_dropout.csv contient les informations suivantes pour chaque élève :

Variable	Description
age	Âge de l'élève
gender	Genre de l'élève (Male/Female)
attendance_rate	Taux de présence aux cours (%)
avg_grade	Moyenne générale de l'élève
parents_education	Niveau d’études des parents (High School, Bachelor's Degree, Master’s Degree)
support_hours	Nombre d’heures de soutien / tutorat fourni
dropped_out	Cible à prédire : 1 si l’élève a abandonné, 0 sinon (valeur cible pour la classification)

Le dataset contient des informations sur un certain nombre d'élèves, dont une proportion a abandonné ses études.

Méthodologie
1. Exploration des données

Inspection initiale des données pour comprendre les distributions des variables.

Vérification de la présence de valeurs manquantes et des anomalies dans les données.

Analyse de la distribution des classes : étant donné que le nombre d’élèves ayant abandonné peut être inférieur à ceux qui ne l’ont pas fait, nous avons vérifié et pris en compte le déséquilibre de la classe cible.

2. Préparation des données

Séparation des variables explicatives (features) de la variable cible (dropped_out).

Encodage des variables catégorielles (comme gender et parents_education) à l'aide d'un OneHotEncoder, afin de les convertir en variables numériques.

Division des données en deux ensembles : un pour l’entraînement du modèle et un autre pour les tests (train/test split).

Gestion des classes déséquilibrées en utilisant l’option class_weight="balanced" dans le modèle LightGBM pour ajuster l'importance de chaque classe.

3. Modélisation

LightGBM (Light Gradient Boosting Machine) a été choisi pour ce projet. C'est un algorithme de boosting qui est particulièrement efficace pour les problèmes de classification avec de grandes quantités de données et des classes déséquilibrées. Le modèle a été configuré pour optimiser la performance tout en prenant en compte le déséquilibre des classes.

4. Évaluation du modèle

Le modèle a été évalué à l’aide du rapport de classification, qui mesure des indicateurs comme la précision, le rappel, et le F1 score.

Une matrice de confusion a été générée pour mieux visualiser les faux positifs et faux négatifs du modèle.

5. Visualisation

Une matrice de confusion a été visualisée à l’aide de Seaborn pour illustrer les performances du modèle et comprendre où il fait des erreurs.

Résultats

Le modèle a été entraîné et évalué sur le dataset, et voici les résultats clés de la classification :

Classification Report :

Précision : Mesure la proportion de prédictions correctes pour la classe positive (élèves ayant abandonné).

Rappel : Mesure la capacité du modèle à identifier correctement les élèves ayant abandonné (le cas des faux négatifs).

F1 Score : Moyenne harmonique entre précision et rappel, qui est une bonne mesure lorsque les classes sont déséquilibrées.

Matrice de confusion :

La matrice de confusion permet de visualiser la performance du modèle en montrant le nombre de prédictions correctes et incorrectes, en distinguant entre faux positifs et faux négatifs. Un faux positif se produit lorsque le modèle prédit qu'un élève abandonne alors qu'il ne l'a pas fait. Un faux négatif est l'inverse : prédire qu'un élève reste alors qu'il abandonne.

Visualisations

Le projet contient une visualisation de la matrice de confusion sous forme de heatmap, ce qui permet de mieux comprendre les erreurs de classification du modèle.

dropout_confusion_matrix_lightgbm.png : Cette visualisation montre la matrice de confusion de l'algorithme LightGBM pour la prédiction du risque d'abandon scolaire.

Code

Le fichier principal du projet est dropout_classification_lightgbm.py, qui implémente l'ensemble du processus, depuis le prétraitement des données jusqu'à l'évaluation du modèle.

Structure du code :

Chargement et exploration des données :

Chargement du fichier CSV avec Pandas.

Inspection des premières lignes du dataset et des statistiques descriptives.

Prétraitement des données :

Séparation des variables explicatives et de la cible.

Encodage des variables catégorielles avec OneHotEncoder de Scikit-learn.

Séparation des données en ensembles d'entraînement et de test.

Modélisation avec LightGBM :

Utilisation du modèle LightGBMClassifier pour entraîner un modèle de classification.

Ajustement des poids des classes déséquilibrées avec class_weight="balanced".

Évaluation du modèle :

Utilisation du rapport de classification pour obtenir la précision, le rappel et le F1 score.

Visualisation de la matrice de confusion avec Seaborn.

Installation

Clonez le repository sur votre machine locale :

git clone https://github.com/ton-utilisateur/projet-risque-abandon-scolaire.git


Installez les dépendances :
Ce projet nécessite les bibliothèques suivantes :

pandas

seaborn

matplotlib

lightgbm

scikit-learn

Vous pouvez installer ces bibliothèques via pip :

pip install pandas seaborn matplotlib lightgbm scikit-learn


Exécutez le code :
Une fois les dépendances installées, vous pouvez exécuter le fichier Python pour entraîner et évaluer le modèle :

python dropout_classification_lightgbm.py
