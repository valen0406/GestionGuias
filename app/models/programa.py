from main import db

class Programa(db.Document):
    programa = db.StringField(required=True , unique=True)
    
    def __str__(self):
        return self.programa