from app import db
app = create_app()

class Instructir(db.Document):
    nombreInstructor = db.StringField(required=True)
    correo = db.StringField(required=True, unique=True)
    regional = db.StringField(required=True)
    usuario = db.StringField(required=True, unique=True)
    clave = db.StringField(required=True)