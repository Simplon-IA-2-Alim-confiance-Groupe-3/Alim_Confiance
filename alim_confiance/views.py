from flask import Blueprint, render_template, request, redirect, url_for
from .models import Etablissement, Inspection
from alim_confiance import db
import pandas as pd

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def accueil():
    return render_template("accueil.html")

@views.route('/liste_E', methods=['GET', 'POST'])
def listeEtablissement():
    etablissement_dataframe = requete_database_etablissement()
    return render_template('liste_E.html', liste_etablissement=etablissement_dataframe)

def requete_database_etablissement():
    etablissement_dataframe = pd.read_sql_table('etablissement', db.engine)
    return etablissement_dataframe

@views.route('/ajout_E', methods=['GET', 'POST'])
def ajoutEtablissement():

    if request.method == "POST":
        etablissement_nom = request.form['nom']
        etablissement_adresse = request.form['adresse']
        etablissement_cp = request.form['code postal']
        etablissement_commune = request.form['adresse']
        etablissement_siret = request.form['siret']
        etablissement_activite = request.form['activite']
        etablissement_agrement = request.form['agrement']
        etablissement_longitude_latitude = request.form['longitude_latitude']
        etablissement_categorie_frais = request.form['categorie_frais']
        
    

        nv_etablissement = Etablissement(nom =etablissement_nom, 
        adresse = etablissement_adresse,
        cp = etablissement_cp,
        commune = etablissement_commune,
        siret = etablissement_siret,
        agrement = etablissement_agrement,
        activite = etablissement_activite,
        longitude_latitude = etablissement_longitude_latitude,
        categorie_frais = etablissement_categorie_frais
        )

        try:
            db.session.add(nv_etablissement)
            db.session.commit()
            return redirect("/liste_E")
        except:
            return " Erreur lors de l'enregistrement"
    else :
        etablissements = Etablissement.query.order_by(Etablissement.id)
        return render_template("ajout_E.html")

@views.route('/prediction', methods=['GET', 'POST'])
def prediction():
    return render_template("prediction.html")
    