
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy = 'dynamic')  #lazy mode means it doesn't check items every time a store object is created

    def __init__(self,name):
        self.name=name


    def jason(self):
        return {'name':self.name,'items':[item.jason() for item in self.items.all()]} #it checks items every time jason() is called

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name = name).first()  #return a Item object select * from items where name = name limit 1
    
    
    def save_to_db(self):  #insert or update
        db.session.add(self)
        db.session.commit()
    

    def delete(self):
        db.session.delete(self)
        db.session.commit()
