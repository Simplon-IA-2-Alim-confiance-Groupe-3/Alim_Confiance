from csv import reader
from datetime import datetime
from alim_confiance import db
from app import app
from alim_confiance.models import Etablissement, Inspection


# with app.app_context():
#     e = Etablissement(nom = "Boulangerie Amry", adresse = "22 rue de Molsheim", cp = "67000", commune = "Strasbourg", siret = "123456789", activite = "boulangerie-patisserie", agrement = "987654321", longitude_latitude = "7.732310,48.577040", categorie_frais = "")
#     db.session.add(e)
#     i = Inspection(numero = "154861" , date= datetime.utcnow(), niveau_hygiene = "Satisfaisant", etablissement = e)
#     db.session.add(i)
#     db.session.commit()

with app.app_context():
    with open('Alim_confiance_modifie.csv', 'r', encoding='UTF-8', errors='ignore') as file:
        csv_reader = reader(file)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                # print(row[3])
                e = Etablissement(nom = row[0], siret = row[1],adresse = row[2], cp = row[3], commune = row[4], activite = row[7], agrement = row[9], longitude_latitude = row[10], categorie_frais = row[11])
                db.session.add(e)
                i = Inspection(numero = row[5], date = datetime.strptime(row[6], "%Y-%m-%dT%H:%M:%S%z"), niveau_hygiene = row[8], etablissement = e)
                db.session.add(i)
    db.session.commit()