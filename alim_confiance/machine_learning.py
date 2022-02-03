import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold


def my_model_execution():

    df=pd.read_csv("alim_confiance/alim_confiance_ML.csv", encoding = "latin-1", sep=";")

    #Nomination des variables
    X = pd.DataFrame(np.c_[df['cp_e'], df['nom_activite_e']], columns= ['cp_e', 'nom_activite_e'])
    y = df["niveau_hygiene_i"]

    #SPLIT le dataset en données de TRAINING et de TESTING. Nous allons d'abord utiliser celles de training.
    # importer la méthode train_test_split 
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=0)

    #vérification des dimensions
    y_train.shape , y_test.shape

    #Technique de cross_validation
    cv_sets = KFold(n_splits=10, shuffle=True, random_state=42)

    # créer le modèle d'arbre de décision 
    # avec le paramètre max_depth = 3
    # le but est de ne pas laisser l'arbre se développer et sur-apprendre 
    classifier = DecisionTreeClassifier(max_depth=3)

    # entraîner le modèle 
    #Utiliser la méthode *fit* de la classe *DecisionTreeClassifier* pour entraîner le modèle d'arbre de classification *classifier* en utilisant les données d'entraînement *X_train* et *y_train* (algorithme supervisé)
    classifier.fit(X_train,y_train)
    
    # Xnew = [[cp,activite]]
    # ynew = classifier.predict(Xnew)

    return ("result")