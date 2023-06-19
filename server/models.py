from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# class Zookeeper(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     birthday = db.Column(db.Date)
#     animals = db.relationship('Animal', backref='zookeeper', lazy='dynamic')
    
#     def __repr__(self):
#         return f'<Zookeeper {self.name}>'
    

# class Enclosure(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     environment = db.Column(db.String(50))
#     open_to_visitors = db.Column(db.Boolean)
#     animals = db.relationship('Animal', backref='enclosure', lazy='dynamic')
    
#     def __repr__(self):
#         return f'<Enclosure {self.environment}>'

# class Animal(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     species = db.Column(db.String(50))
#     zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeeper.id'))
#     enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosure.id'))
    
#     def __repr__(self):
#         return f'<Animal {self.name}>'

class Zookeeper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    birthday = db.Column(db.Date)
    animals = db.relationship('Animal', backref='zookeeper', lazy='dynamic')
    
    def __repr__(self):
        return f'<Zookeeper {self.name}>'
    
class Enclosure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(50))
    open_to_visitors = db.Column(db.Boolean)
    animals = db.relationship('Animal', backref='enclosure', lazy='dynamic')
    
    def __repr__(self):
        return f'<Enclosure {self.environment}>'

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    species = db.Column(db.String(50))
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeeper.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosure.id'))
    
    def __repr__(self):
        return f'<Animal {self.name}>'

