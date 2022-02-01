from alim_confiance import db
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class Etablissement(db.Model):
    __tablename__ = 'etablissement'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nom = Column(String(50))
    adresse = Column(String(50))
    cp = Column(String(10))
    commune = Column(String(50))
    siret = Column(String(15))
    activite = Column(String(50))
    agrement = Column(String(15))
    longitude_latitude = Column(String(50))
    categorie_frais = Column(String(50))

    def __str__(self):
        return self.nom
 
class Inspection(db.Model):
    __tablename__ = 'inspection'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    numero = Column(String(50))
    date = Column(DateTime,default=func.now())
    niveau_hygiene = Column(String(50))
    etablissement_id = Column(Integer, ForeignKey('etablissement.id'))
    etablissement = relationship(Etablissement)

    def __str__(self):
        return self.numero