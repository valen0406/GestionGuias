from main import db

class Regional(db.Document):
    nombreRegional = db.StringField(required=True)
    
    def __str__(self):
        return self.nombre