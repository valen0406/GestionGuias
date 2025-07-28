from main import db


class Instructor(db.Document):
    nombreInstructor = db.StringField(required=True)
    correo = db.StringField(required=True, unique=True)
    usuario = db.StringField(required=True, unique=True)
    clave = db.StringField(required=True)
    regional = db.reference_field('Regional', required=True)