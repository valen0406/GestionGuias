from app import db
from datetime import datetime

class Guia(db.Document):
    nombreGuia = db.StringField(required=True)
    descripcion  = db.StringField()
    programa = db.StringField(required=True)
    archivo_pdf = db.StringField(required=True)
    fecha_subida = db.DateTimeField(default=datetime.utcnow)
    instructor_id = db.ReferenceField('Instructor')